# FileFlow

FileFlow is a lightweight command-line file organization utility written in Python.

It allows users to select any folder on their local system and automatically organizes the files inside it into categories based on their file extensions.

---

## Features

- Organize files from any local folder
- Automatically classify files by extension
- Create category folders automatically
- Prevent accidental file overwrites
- Handle uppercase and lowercase extensions
- Handle unsupported file types safely
- Generate an organization summary
- Preview changes using dry-run mode
- No external Python packages required

---

## Project Structure

```text
FileFlow/
│
├── main.py
├── file_manager.py
├── file_utils.py
└── README.md
```

### main.py

The main entry point of the application.

Responsible for:

- Starting FileFlow
- Reading user input
- Handling command-line arguments
- Displaying information and results
- Coordinating the organization process

### file_manager.py

Contains the main file-system operations.

Responsible for:

- Scanning directories
- Creating organization plans
- Creating category folders
- Moving files
- Handling duplicate filenames
- Generating file statistics

### file_utils.py

Contains reusable file-related utilities.

Responsible for:

- File extension handling
- File classification
- Supported file types
- File size utilities
- Category validation
- Safe filename handling

---

## Requirements

- Python 3.9 or newer
- No external Python packages are required

Check your Python version:

```bash
python --version
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/pramathi-sujay/FileFlow.git
```

### 2. Enter the project directory

```bash
cd FileFlow
```

### 3. Run FileFlow

```bash
python main.py
```

FileFlow will ask:

```text
Enter the folder path you want to organize:
>
```

Enter the path of any folder on your computer.

For example:

```text
E:\PROJECTS\MyFiles
```

or:

```text
C:\Users\YourName\Downloads
```

---

## Example

Suppose the selected folder contains:

```text
MyFiles/
├── report.pdf
├── photo.jpg
├── notes.txt
├── sales.csv
├── presentation.pptx
└── unknown.xyz
```

After running FileFlow:

```text
MyFiles/
├── Documents/
│   ├── report.pdf
│   └── notes.txt
│
├── Images/
│   └── photo.jpg
│
├── Data/
│   └── sales.csv
│
├── Presentations/
│   └── presentation.pptx
│
└── Others/
    └── unknown.xyz
```

FileFlow also displays a summary:

```text
==========================================================
              FILE ORGANIZATION SUMMARY
==========================================================
Documents           : 2
Images              : 1
Data                : 1
Presentations       : 1
Archives            : 0
Others              : 1
----------------------------------------------------------
Files processed     : 6
Files skipped       : 0
Total files found   : 6
==========================================================
```

---

## Supported File Categories

| Category | Supported Extensions |
|---|---|
| Documents | `.txt`, `.pdf`, `.doc`, `.docx`, `.rtf` |
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp` |
| Data | `.csv`, `.json`, `.xml`, `.xlsx` |
| Presentations | `.ppt`, `.pptx` |
| Archives | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| Others | Unsupported or unrecognized extensions |

File extensions are normalized before classification.

For example:

```text
report.pdf
REPORT.PDF
Report.Pdf
```

are treated as the same file type.

---

## Dry Run Mode

FileFlow provides a dry-run mode so you can preview the changes before any files are moved.

Run:

```bash
python main.py --dry-run
```

Or specify a folder directly:

```bash
python main.py --folder "E:\PROJECTS\MyFiles" --dry-run
```

Dry-run mode displays the organization plan without modifying the selected folder.

---

## Command-Line Usage

### Interactive mode

```bash
python main.py
```

FileFlow asks for the folder path.

### Direct folder mode

```bash
python main.py --folder "E:\PROJECTS\MyFiles"
```

### Dry-run mode

```bash
python main.py --dry-run
```

### Direct folder with dry-run

```bash
python main.py --folder "E:\PROJECTS\MyFiles" --dry-run
```

---

## File Safety

FileFlow takes several precautions while organizing files:

- Hidden files are ignored.
- Existing files are not overwritten.
- Duplicate filenames receive a unique name.

For example:

```text
report.pdf
report_1.pdf
report_2.pdf
```

FileFlow only scans files directly inside the selected folder. It does not recursively process files inside unrelated subdirectories.

---

## Testing

To test FileFlow, create or select a folder containing different types of files and run:

```bash
python main.py --dry-run
```

Review the organization plan first.

After confirming the plan:

```bash
python main.py
```

---

## Important

FileFlow moves files into category folders when run normally.

Always use:

```bash
python main.py --dry-run
```

first if you are unsure about the changes that will be made.

---

## License

This project is created for educational and workshop purposes.
