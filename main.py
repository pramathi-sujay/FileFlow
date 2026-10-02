"""
FileFlow - Smart File Organizer

Application entry point.
"""

import argparse
from pathlib import Path

from file_manager import FileManager


def print_banner():
    """Display the FileFlow application banner."""
    print("=" * 58)
    print("                 FILEFLOW")
    print("           Smart File Organizer")
    print("=" * 58)


def get_folder_from_user():
    """Ask the user for the folder they want to organize."""
    print("\nEnter the folder path you want to organize:")
    folder_path = input("> ").strip().strip('"')

    if not folder_path:
        raise ValueError("No folder path was provided.")

    return Path(folder_path)


def print_file_list(files):
    """Display the files discovered in the input directory."""
    if not files:
        print("\nNo files found in the selected folder.")
        return

    print("\nFiles discovered:")
    print("-" * 58)

    for index, file_path in enumerate(files, start=1):
        print(f"{index:>3}. {file_path.name}")


def print_plan(plan):
    """Display the organization plan before files are moved."""
    print("\nOrganization plan:")
    print("-" * 58)

    for category, files in plan.items():
        print(f"\n{category}/")

        if not files:
            print("  └── No files")

        for file_path in files:
            print(f"  └── {file_path.name}")


def print_summary(summary):
    """Display the final organization summary."""
    print("\n")
    print("=" * 58)
    print("              FILE ORGANIZATION SUMMARY")
    print("=" * 58)

    for category, count in summary["categories"].items():
        print(f"{category:<20}: {count}")

    print("-" * 58)

    print(f"{'Files processed':<20}: {summary['processed']}")
    print(f"{'Files skipped':<20}: {summary['skipped']}")
    print(f"{'Total files found':<20}: {summary['total']}")

    print("=" * 58)


def build_parser():
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Organize files in a directory by file type."
    )

    parser.add_argument(
        "--folder",
        help="Folder to organize. If omitted, FileFlow will ask for it.",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show the organization plan without moving files.",
    )

    return parser


def main():
    """Run the FileFlow application."""
    print_banner()

    parser = build_parser()
    args = parser.parse_args()

    try:
        # Use the command-line path if provided.
        if args.folder:
            input_folder = Path(args.folder)
        else:
            # Otherwise, ask the user interactively.
            input_folder = get_folder_from_user()

        print(f"\nSelected folder: {input_folder}")

        manager = FileManager(input_folder)

        # Step 1: Scan the directory
        files = manager.scan_directory()
        print_file_list(files)

        if not files:
            return

        # Step 2: Create an organization plan
        plan = manager.create_organization_plan(files)
        print_plan(plan)

        # Step 3: Support dry-run mode
        if args.dry_run:
            print("\nDry run complete. No files were moved.")
            return

        # Step 4: Organize the files
        print("\nOrganizing files...")
        summary = manager.organize_files(plan)

        # Step 5: Display the final report
        print_summary(summary)

        print("\nFile organization completed successfully!")

    except ValueError as error:
        print(f"\nInput error: {error}")

    except FileNotFoundError as error:
        print(f"\nError: {error}")

    except NotADirectoryError as error:
        print(f"\nError: {error}")

    except PermissionError as error:
        print(f"\nPermission error: {error}")

    except OSError as error:
        print(f"\nFile system error: {error}")


if __name__ == "__main__":
    main()
    