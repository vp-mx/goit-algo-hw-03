import argparse
import shutil
import sys
from pathlib import Path


def copy_files_recursively(src_dir: Path, dest_dir: Path) -> None:
    """
    Recursively copies files from the source directory to the destination directory,
    organizing them into subdirectories based on their file extensions.

    :param: src_dir (Path): The source directory path.
    :param: dest_dir (Path): The destination directory path.
    """
    try:
        for item in src_dir.iterdir():
            if item.is_dir():
                copy_files_recursively(item, dest_dir)
            else:
                file_extension = item.suffix[1:]  # Get file extension without dot
                if file_extension:
                    dest_path = dest_dir / file_extension
                    dest_path.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(item, dest_path / item.name)
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    """
    Main function to parse command-line arguments and initiate the file copying process.
    """
    parser = argparse.ArgumentParser(
        description="Recursively copy and sort files by extension."
    )
    parser.add_argument("--src-dir", type=Path, help="The source directory path.")
    parser.add_argument(
        "--dest-dir",
        type=Path,
        nargs="?",
        default=Path("dist"),
        help="The destination directory path (default: 'dist').",
    )
    args = parser.parse_args()

    src_dir: Path = args.src_dir
    dest_dir: Path = args.dest_dir

    if not src_dir.exists():
        print(f"Source directory '{src_dir}' does not exist.")
        sys.exit(1)

    dest_dir.mkdir(parents=True, exist_ok=True)
    copy_files_recursively(src_dir, dest_dir)
    print(f"Files copied and sorted in '{dest_dir}'.")


if __name__ == "__main__":
    main()
