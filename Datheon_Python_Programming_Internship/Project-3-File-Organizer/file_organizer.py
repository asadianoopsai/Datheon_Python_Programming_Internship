
import os
import shutil
from pathlib import Path


# File categories and their extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".webm"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Python": [".py"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}


def get_category(file_path):
    """Return a category based on the file extension."""
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_path(destination):
    """Avoid overwriting a file with the same name."""
    if not destination.exists():
        return destination

    parent = destination.parent
    stem = destination.stem
    suffix = destination.suffix
    counter = 1

    while True:
        new_destination = parent / f"{stem}_{counter}{suffix}"

        if not new_destination.exists():
            return new_destination

        counter += 1


def organize_files(folder_path):
    """Organize files inside the selected folder."""
    folder = Path(folder_path).expanduser().resolve()

    if not folder.exists():
        print("Error: The folder does not exist.")
        return

    if not folder.is_dir():
        print("Error: The supplied path is not a folder.")
        return

    organized = 0
    skipped = 0
    errors = 0

    print(f"\nOrganizing files in: {folder}\n")

    try:
        items = list(folder.iterdir())
    except OSError as error:
        print(f"Error reading folder: {error}")
        return

    for item in items:
        # Skip subfolders and this script itself.
        if not item.is_file() or item.resolve() == Path(__file__).resolve():
            continue

        category = get_category(item)
        destination_folder = folder / category

        try:
            destination_folder.mkdir(exist_ok=True)
            destination = get_unique_path(destination_folder / item.name)

            # Move the file without overwriting an existing file.
            shutil.move(str(item), str(destination))
            print(f"Moved: {item.name} -> {category}/{destination.name}")
            organized += 1

        except FileNotFoundError:
            print(f"Skipped: {item.name} (file or folder no longer exists)")
            skipped += 1

        except (PermissionError, OSError, shutil.Error) as error:
            print(f"Error moving {item.name}: {error}")
            errors += 1

    print("\n========== ORGANIZATION SUMMARY ==========")
    print(f"Files organized: {organized}")
    print(f"Files skipped:   {skipped}")
    print(f"Errors:          {errors}")
    print("==========================================")

    # Confirm that the folder is still accessible.
    if not os.access(folder, os.R_OK):
        print("Warning: The folder may no longer be readable.")


def main():
    print("======================================")
    print("   AUTOMATED FILE ORGANIZER")
    print("======================================")
    print("Safety tip: Use a test folder first.")

    folder_path = input(
        "\nEnter the full path of the folder to organize: "
    ).strip().strip('"')

    if not folder_path:
        print("No folder path provided. Exiting.")
        return

    confirmation = input(
        f"\nFiles inside this folder may be moved:\n"
        f"{folder_path}\n"
        "Continue? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        organize_files(folder_path)
    else:
        print("Operation cancelled. No files were moved.")


if __name__ == "__main__":
    main()
