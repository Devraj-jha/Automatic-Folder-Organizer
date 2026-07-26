import os
import json
import shutil
import tempfile
import unittest

from file_utils import get_category, organize_folder, save_log, undo_moves, count_files, LOG_FILENAME
from categories import CATEGORIES


class TestGetCategory(unittest.TestCase):
    """Tests for the get_category helper."""

    def test_known_extensions(self):
        self.assertEqual(get_category("photo.jpg"), "Images")
        self.assertEqual(get_category("resume.pdf"), "Documents")
        self.assertEqual(get_category("song.mp3"), "Audio")
        self.assertEqual(get_category("movie.mp4"), "Videos")
        self.assertEqual(get_category("backup.zip"), "Archives")
        self.assertEqual(get_category("app.py"), "Code")
        self.assertEqual(get_category("font.ttf"), "Fonts")

    def test_case_insensitive(self):
        self.assertEqual(get_category("Photo.JPG"), "Images")
        self.assertEqual(get_category("SONG.MP3"), "Audio")

    def test_unknown_extension(self):
        self.assertEqual(get_category("file.xyz"), "Others")
        self.assertEqual(get_category("noext"), "Others")

    def test_new_extensions(self):
        self.assertEqual(get_category("photo.webp"), "Images")
        self.assertEqual(get_category("data.csv"), "Documents")
        self.assertEqual(get_category("track.flac"), "Audio")
        self.assertEqual(get_category("clip.webm"), "Videos")
        self.assertEqual(get_category("disk.7z"), "Archives")
        self.assertEqual(get_category("main.ts"), "Code")
        self.assertEqual(get_category("icon.woff2"), "Fonts")


class TestOrganizeFolder(unittest.TestCase):
    """Tests for organize_folder with real temp directories."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def _create_files(self, names):
        for name in names:
            path = os.path.join(self.tmpdir, name)
            with open(path, "w") as f:
                f.write("test")

    def test_dry_run_does_not_move(self):
        self._create_files(["a.jpg", "b.pdf", "c.mp3"])
        moves = organize_folder(self.tmpdir, dry_run=True)
        self.assertEqual(len(moves), 3)
        # Files should still be in root
        self.assertTrue(os.path.exists(os.path.join(self.tmpdir, "a.jpg")))
        self.assertTrue(os.path.exists(os.path.join(self.tmpdir, "b.pdf")))
        self.assertTrue(os.path.exists(os.path.join(self.tmpdir, "c.mp3")))
        # No category folders created
        self.assertFalse(os.path.exists(os.path.join(self.tmpdir, "Images")))

    def test_organize_creates_folders(self):
        self._create_files(["a.jpg", "b.pdf", "c.mp3"])
        moves = organize_folder(self.tmpdir, dry_run=False)
        self.assertEqual(len(moves), 3)
        self.assertTrue(os.path.isdir(os.path.join(self.tmpdir, "Images")))
        self.assertTrue(os.path.isdir(os.path.join(self.tmpdir, "Documents")))
        self.assertTrue(os.path.isdir(os.path.join(self.tmpdir, "Audio")))
        self.assertTrue(os.path.exists(os.path.join(self.tmpdir, "Images", "a.jpg")))
        self.assertTrue(os.path.exists(os.path.join(self.tmpdir, "Documents", "b.pdf")))
        self.assertTrue(os.path.exists(os.path.join(self.tmpdir, "Audio", "c.mp3")))

    def test_skips_directories(self):
        os.makedirs(os.path.join(self.tmpdir, "subfolder"))
        self._create_files(["a.jpg"])
        moves = organize_folder(self.tmpdir, dry_run=False)
        self.assertEqual(len(moves), 1)
        # subfolder should remain untouched
        self.assertTrue(os.path.isdir(os.path.join(self.tmpdir, "subfolder")))

    def test_others_category(self):
        self._create_files(["mystery.xyz"])
        moves = organize_folder(self.tmpdir, dry_run=False)
        self.assertEqual(len(moves), 1)
        self.assertTrue(os.path.exists(os.path.join(self.tmpdir, "Others", "mystery.xyz")))

    def test_duplicate_filename_handling(self):
        # Pre-create a category folder with a conflicting file
        os.makedirs(os.path.join(self.tmpdir, "Images"))
        with open(os.path.join(self.tmpdir, "Images", "photo.jpg"), "w") as f:
            f.write("existing")
        self._create_files(["photo.jpg"])
        moves = organize_folder(self.tmpdir, dry_run=False)
        self.assertEqual(len(moves), 1)
        # Original file should be renamed to avoid overwrite
        self.assertTrue(
            os.path.exists(os.path.join(self.tmpdir, "Images", "photo.jpg"))
        )


class TestUndo(unittest.TestCase):
    """Tests for the undo functionality."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def _create_files(self, names):
        for name in names:
            path = os.path.join(self.tmpdir, name)
            with open(path, "w") as f:
                f.write("test")

    def test_undo_restores_files(self):
        self._create_files(["a.jpg", "b.pdf"])
        moves = organize_folder(self.tmpdir, dry_run=False)
        save_log(moves, self.tmpdir)

        # Files are now organized
        self.assertTrue(os.path.exists(os.path.join(self.tmpdir, "Images", "a.jpg")))

        result = undo_moves(self.tmpdir)
        self.assertTrue(result)

        # Files should be back in root
        self.assertTrue(os.path.exists(os.path.join(self.tmpdir, "a.jpg")))
        self.assertTrue(os.path.exists(os.path.join(self.tmpdir, "b.pdf")))
        # Log should be deleted
        self.assertFalse(os.path.exists(os.path.join(self.tmpdir, LOG_FILENAME)))

    def test_undo_no_log(self):
        result = undo_moves(self.tmpdir)
        self.assertFalse(result)

    def test_undo_removes_empty_dirs(self):
        self._create_files(["a.jpg"])
        moves = organize_folder(self.tmpdir, dry_run=False)
        save_log(moves, self.tmpdir)
        undo_moves(self.tmpdir)
        self.assertFalse(os.path.exists(os.path.join(self.tmpdir, "Images")))


class TestCountFiles(unittest.TestCase):
    """Tests for count_files."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def test_count(self):
        for name in ["a.txt", "b.jpg", "c.pdf"]:
            with open(os.path.join(self.tmpdir, name), "w") as f:
                f.write("test")
        os.makedirs(os.path.join(self.tmpdir, "subdir"))
        count = count_files(self.tmpdir)
        self.assertEqual(count, 3)


if __name__ == "__main__":
    unittest.main()
