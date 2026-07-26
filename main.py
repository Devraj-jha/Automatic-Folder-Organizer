import os
import argparse

from file_utils import organize_folder, count_files, save_log, undo_moves


def parse_args():
    parser = argparse.ArgumentParser(
        description="Organize files in a folder by type (images, documents, audio, etc.)"
    )
    parser.add_argument(
        "folder",
        nargs="?",
        default=None,
        help="Full path to the folder to organize (prompts interactively if omitted)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be moved without actually moving files",
    )
    parser.add_argument(
        "--undo",
        action="store_true",
        help="Reverse the last organize operation",
    )
    parser.add_argument(
        "--count",
        action="store_true",
        help="Just count files without organizing",
    )
    return parser.parse_args()


def get_folder_path(prompt_text="Enter the full path of the folder to organize: "):
    """Get folder path from user, either via argument or interactive prompt."""
    folder = input(prompt_text).strip()
    if not os.path.exists(folder):
        print(f"Error: '{folder}' does not exist.")
        return None
    if not os.path.isdir(folder):
        print(f"Error: '{folder}' is not a directory.")
        return None
    return folder


def main():
    args = parse_args()

    # Resolve folder path: CLI arg or interactive prompt
    folder_path = args.folder
    if folder_path is None:
        folder_path = get_folder_path()
        if folder_path is None:
            return
    else:
        if not os.path.exists(folder_path):
            print(f"Error: '{folder_path}' does not exist.")
            return
        if not os.path.isdir(folder_path):
            print(f"Error: '{folder_path}' is not a directory.")
            return

    # --undo: reverse last organize
    if args.undo:
        print("\nUndoing last organize...\n")
        undo_moves(folder_path)
        return

    # --count: just count files
    if args.count:
        count_files(folder_path)
        return

    # Normal organize (with optional dry-run)
    count_files(folder_path)

    mode_label = "[DRY RUN] " if args.dry_run else ""
    print(f"\n{mode_label}Organizing files...\n")

    moves = organize_folder(folder_path, dry_run=args.dry_run)

    if not moves:
        print("\nNo files to organize.")
    elif not args.dry_run:
        save_log(moves, folder_path)
        print(f"\nOrganized {len(moves)} file(s). Log saved for undo.")
    else:
        print(f"\n{len(moves)} file(s) would be moved.")


if __name__ == "__main__":
    main()
