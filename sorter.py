from pathlib import Path
from categories import CATEGORY_EXTENSIONS


def get_file_category(file_path):
    extension = file_path.suffix.lower()
    for category, extensions in CATEGORY_EXTENSIONS.items():
        if extension in extensions:
            return category
    return "Other"


def get_sortable_files(folder_path):
    files = []
    entries = folder_path.iterdir()
    for entry in entries:
        if entry.is_file():
            if not entry.is_symlink():
                files.append(entry)
    return files