"""
FileFlow - File Management Layer

Contains the main file-system operations used by the application.
"""

from collections import OrderedDict
from pathlib import Path
from typing import Dict, List

from file_utils import (
    CATEGORY_ORDER,
    classify_file,
    create_unique_path,
    is_supported_file,
)


class FileManager:
    """Manage scanning, classification, organization, and reporting."""

    def __init__(self, input_folder: Path):
        self.input_folder = Path(input_folder)

    def validate_directory(self) -> None:
        """Validate that the configured input path is a directory."""
        if not self.input_folder.exists():
            raise FileNotFoundError(
                f"Input folder '{self.input_folder}' does not exist."
            )

        if not self.input_folder.is_dir():
            raise NotADirectoryError(
                f"Input path '{self.input_folder}' is not a directory."
            )

    def scan_directory(self) -> List[Path]:
        """Return regular files directly inside the input folder."""
        self.validate_directory()

        files = []

        for path in self.input_folder.iterdir():
            if path.is_file() and not path.name.startswith("."):
                files.append(path)

        return sorted(files, key=lambda item: item.name.lower())

    def create_organization_plan(
        self, files: List[Path]
    ) -> Dict[str, List[Path]]:
        """Group files by their destination category."""
        plan = OrderedDict(
            (category, []) for category in CATEGORY_ORDER
        )

        for file_path in files:
            category = classify_file(file_path)

            if category not in plan:
                category = "Others"

            plan[category].append(file_path)

        return plan

    def create_category_folders(self, categories) -> None:
        """Create destination folders when they do not already exist."""
        for category in categories:
            destination = self.input_folder / category
            destination.mkdir(exist_ok=True)

    def move_file(self, file_path: Path, category: str) -> Path:
        """Move one file into its category folder."""
        destination_folder = self.input_folder / category
        destination_folder.mkdir(exist_ok=True)

        destination = destination_folder / file_path.name
        destination = create_unique_path(destination)

        file_path.rename(destination)
        return destination

    def organize_files(
        self, plan: Dict[str, List[Path]]
    ) -> Dict[str, object]:
        """Move files according to the organization plan."""
        self.create_category_folders(plan.keys())

        category_counts = OrderedDict(
            (category, 0) for category in CATEGORY_ORDER
        )

        processed = 0
        skipped = 0

        for category, files in plan.items():
            for file_path in files:
                if not file_path.exists():
                    skipped += 1
                    continue

                try:
                    self.move_file(file_path, category)

                    # Deliberate workshop bug:
                    # the category count is recorded under the next
                    # category instead of the file's actual category.
                    category_index = CATEGORY_ORDER.index(category)
                    next_index = (category_index + 1) % len(CATEGORY_ORDER)
                    category_counts[CATEGORY_ORDER[next_index]] += 1

                    processed += 1

                except OSError:
                    skipped += 1

        return {
            "categories": category_counts,
            "processed": processed,
            "skipped": skipped,
            "total": processed + skipped,
        }

    def count_organized_files(self) -> Dict[str, int]:
        """Count files currently stored in each category folder."""
        counts = OrderedDict(
            (category, 0) for category in CATEGORY_ORDER
        )

        for category in CATEGORY_ORDER:
            folder = self.input_folder / category

            if not folder.exists():
                continue

            for path in folder.iterdir():
                if path.is_file() and is_supported_file(path):
                    counts[category] += 1

        return counts

    def generate_report(self) -> Dict[str, object]:
        """Generate a report from the current organized directory."""
        category_counts = self.count_organized_files()
        total = sum(category_counts.values())

        return {
            "categories": category_counts,
            "total": total,
        }
