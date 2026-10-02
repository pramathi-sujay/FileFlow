# FileFlow

**FileFlow** is a small command-line file organization utility written in Python.

It scans a folder, identifies files by their extensions, places them into
category folders, and displays a summary of the operation.

## Features

- Scan files in a directory
- Classify files by extension
- Organize files into category folders
- Handle duplicate filenames safely
- Ignore hidden files
- Generate an organization summary
- Support dry-run mode
- No external Python packages required

## Project Structure

```text
FileFlow/
├── main.py
├── file_manager.py
├── file_utils.py
├── README.md
└── test_files/
```

### Python files

- **main.py** - application entry point and command-line interface
- **file_manager.py** - scanning, planning, moving, and reporting
- **file_utils.py** - file classification and reusable file-system helpers

## Requirements

- Python 3.9 or newer
- No external packages are required

## Running FileFlow

From the project directory:

```bash
python main.py
```

By default, FileFlow scans the `test_files` directory.

You can also specify another folder:

```bash
python main.py --folder my_files
```

## Dry Run

To see what FileFlow would do without moving any files:

```bash
python main.py --dry-run
```

## Supported Categories

| Category | Example extensions |
|---|---|
| Documents | `.txt`, `.pdf`, `.doc`, `.docx`, `.rtf` |
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp` |
| Data | `.csv`, `.json`, `.xml`, `.xlsx` |
| Presentations | `.ppt`, `.pptx` |
| Archives | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| Others | Unrecognized extensions |

## Example

Before running:

```text
test_files/
├── report.pdf
├── photo.jpg
├── notes.txt
├── data.csv
├── presentation.pptx
└── unknown.xyz
```

After running:

```text
test_files/
├── Documents/
│   ├── notes.txt
│   └── report.pdf
├── Images/
│   └── photo.jpg
├── Data/
│   └── data.csv
├── Presentations/
│   └── presentation.pptx
└── Others/
    └── unknown.xyz
```

## Notes

FileFlow only processes files directly inside the selected input folder.
It does not recursively scan already-created category folders.
