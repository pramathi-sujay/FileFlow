"""
FileFlow - File Utility Functions

Contains reusable helpers for classifying files and safely handling
file-system operations.
"""

from pathlib import Path
from typing import Dict, Optional


# The order in which categories appear in FileFlow reports.
CATEGORY_ORDER = [
    "Documents",
    "Images",
    "Data",
    "Presentations",
    "Archives",
    "Others",
]


# Maps file extensions to their corresponding categories.
FILE_CATEGORIES: Dict[str, str] = {

    # Documents
    ".txt": "Documents",
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".rtf": "Documents",

    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".webp": "Images",

    # Data
    ".csv": "Data",
    ".json": "Data",
    ".xml": "Data",
    ".xlsx": "Data",

    # Presentations
    ".ppt": "Presentations",
    ".pptx": "Presentations",

    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
}


def normalize_extension(file_path: Path) -> str:
    """
    Return a normalized, lowercase extension.

    Example:
        REPORT.PDF -> .pdf
        photo.JPEG -> .jpeg
    """
    return file_path.suffix.lower()


def classify_file(file_path: Path) -> str:
    """Return the category assigned to a file."""

    extension = normalize_extension(file_path)

    return FILE_CATEGORIES.get(
        extension,
        "Others"
    )


def is_supported_file(file_path: Path) -> bool:
    """Return True when the file has a recognized extension."""

    extension = normalize_extension(file_path)

    return extension in FILE_CATEGORIES


def is_hidden_file(file_path: Path) -> bool:
    """Return True when a filename starts with a dot."""

    return file_path.name.startswith(".")


def get_file_size(file_path: Path) -> int:
    """Return the file size in bytes."""

    try:
        return file_path.stat().st_size

    except OSError:
        return 0


def format_file_size(
    size_in_bytes: int
) -> str:
    """Convert a byte count into a readable size."""

    units = [
        "B",
        "KB",
        "MB",
        "GB"
    ]

    size = float(size_in_bytes)

    for unit in units:

        if size < 1024 or unit == units[-1]:
            return f"{size:.1f} {unit}"

        size /= 1024

    return "0.0 B"


def create_unique_path(
    destination: Path
) -> Path:
    """
    Return a unique destination path.

    If report.pdf already exists, the next available name becomes:

        report_1.pdf

    If that also exists:

        report_2.pdf

    and so on.
    """

    if not destination.exists():
        return destination

    stem = destination.stem
    suffix = destination.suffix
    parent = destination.parent

    counter = 1

    while True:

        candidate = (
            parent /
            f"{stem}_{counter}{suffix}"
        )

        if not candidate.exists():
            return candidate

        counter += 1


def get_category_extensions(
    category: str
):
    """Return all extensions associated with a category."""

    return [
        extension
        for extension, mapped_category
        in FILE_CATEGORIES.items()
        if mapped_category == category
    ]


def describe_file(
    file_path: Path
) -> Optional[Dict[str, object]]:
    """Return useful information about a file."""

    if not file_path.exists():
        return None

    if not file_path.is_file():
        return None

    file_size = get_file_size(file_path)

    return {
        "name": file_path.name,
        "extension": normalize_extension(file_path),
        "category": classify_file(file_path),
        "size": file_size,
        "readable_size": format_file_size(
            file_size
        ),
    }


def get_category_description(
    category: str
) -> str:
    """Return a short description for a category."""

    descriptions = {

        "Documents":
            "Text documents and PDF files",

        "Images":
            "Common image files",

        "Data":
            "Structured data and spreadsheet files",

        "Presentations":
            "Presentation files",

        "Archives":
            "Compressed archive files",

        "Others":
            "Files without a recognized type",
    }

    return descriptions.get(
        category,
        "Uncategorized files"
    )


def validate_category(
    category: str
) -> bool:
    """Check whether a category is part of FileFlow."""

    return category in CATEGORY_ORDER