import os
import json
import shutil

from categories import CATEGORIES

LOG_FILENAME = ".organize_log.json"


def get_category(file_name):
    """Return the category folder name for a file based on its extension."""
    _, ext = os.path.splitext(file_name)
    ext = ext.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"


def _unique_dest(dest_path):
    """If dest_path already exists, append a counter to avoid overwriting."""
    if not os.path.exists(dest_path):
        return dest_path
    base, ext = os.path.splitext(dest_path)
    counter = 1
    while os.path.exists(f"{base} ({counter}){ext}"):
        counter += 1
    return f"{base} ({counter}){ext}"


def organize_folder(folder_path, dry_run=False):
    """Sort files in folder_path into category sub-folders.

    Args:
        folder_path: Directory containing files to organize.
        dry_run: If True, preview moves without actually moving files.

    Returns:
        List of dicts with 'from' and 'to' keys for each moved file.
    """
    moves = []

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # Skip directories and the log file itself
        if os.path.isdir(item_path) or item == LOG_FILENAME:
            continue

        category = get_category(item)
        category_folder = os.path.join(folder_path, category)
        dest = _unique_dest(os.path.join(category_folder, item))

        if dry_run:
            print(f"  [dry-run] {item} -> {category}/")
        else:
            try:
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                shutil.move(item_path, dest)
                print(f"  Moved: {item} -> {category}/")
            except PermissionError:
                print(f"  Skipped: {item} (permission denied)")
                continue
            except shutil.Error as e:
                print(f"  Skipped: {item} ({e})")
                continue

        moves.append({"from": item_path, "to": dest})

    return moves


def save_log(moves, folder_path):
    """Append a move log to .organize_log.json inside the folder."""
    if not moves:
        return
    log_path = os.path.join(folder_path, LOG_FILENAME)
    existing = []
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            existing = json.load(f)
    existing.extend(moves)
    with open(log_path, "w") as f:
        json.dump(existing, f, indent=2)


def undo_moves(folder_path):
    """Reverse the last organize operation using the log file."""
    log_path = os.path.join(folder_path, LOG_FILENAME)
    if not os.path.exists(log_path):
        print("No undo log found. Nothing to undo.")
        return False

    with open(log_path, "r") as f:
        moves = json.load(f)

    if not moves:
        print("Undo log is empty. Nothing to undo.")
        return False

    # Undo in reverse order
    undone = 0
    for entry in reversed(moves):
        src = entry["to"]
        dest = entry["from"]
        if not os.path.exists(src):
            print(f"  Skipped: {os.path.basename(src)} (no longer at organized location)")
            continue
        try:
            # Recreate original parent directory if needed
            dest_dir = os.path.dirname(dest)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            shutil.move(src, dest)
            print(f"  Restored: {os.path.basename(src)}")
            undone += 1
        except (PermissionError, shutil.Error) as e:
            print(f"  Skipped: {os.path.basename(src)} ({e})")

    # Remove empty category folders
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            try:
                if not os.listdir(item_path):
                    os.rmdir(item_path)
            except OSError:
                pass

    # Remove the log file
    os.remove(log_path)
    print(f"\nUndone {undone} move(s). Log removed.")
    return True


def count_files(folder_path):
    """Print and return the number of files (not directories) in the folder."""
    total = sum(
        1 for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f)) and f != LOG_FILENAME
    )
    print(f"\nFiles found: {total}")
    return total
