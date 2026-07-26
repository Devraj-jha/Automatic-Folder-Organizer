
# 🗂️ Folder Organizer (Python Automation Tool)

## 📖 Overview

The **Folder Organizer** is a lightweight Python automation tool that automatically sorts files in a directory based on their type.
It gives the user the ability to provide any folder path — and with one command, it organizes the entire folder neatly by moving each file into its appropriate category (e.g., all `.jpg` → `Images`, `.pdf` → `Documents`, etc.).

No more messy Downloads folders — one script keeps your workspace clean and structured.

---

## ✨ Features

* ✅ Automatically detects file types (images, documents, videos, code, fonts, and more)
* ✅ Creates categorized folders automatically if they don't exist
* ✅ Safely moves files to their respective categories
* ✅ **Dry Run** mode — preview moves without actually touching files
* ✅ **Undo** — reverse the last organize operation with one command
* ✅ Handles duplicate filenames gracefully (appends a counter)
* ✅ Error handling for permission issues and locked files
* ✅ Works seamlessly on **macOS**, **Windows**, and **Linux**
* ✅ Fully customizable — easily add or edit file types in `categories.py`
* ✅ Modular design with clear separation of logic across files
* ✅ Built-in unit tests

---

## 📂 Project Structure

```
folder_organizer/
│
├── main.py              # Entry point – CLI interface
├── file_utils.py        # Core organization logic, undo, logging
├── categories.py        # File categories and extension mappings
├── test_organizer.py    # Unit tests
└── README.md            # This file
```

---

## ⚙️ How It Works

1. Run the program in your terminal with a folder path.
2. The program scans all files in that folder.
3. Based on each file's extension (`.jpg`, `.pdf`, `.mp3`, etc.), it moves the file into:

   | Category | Extensions |
   |----------|-----------|
   | `Images/` | .jpg, .png, .gif, .svg, .webp, .heic, ... |
   | `Documents/` | .pdf, .docx, .txt, .csv, .md, .epub, ... |
   | `Audio/` | .mp3, .wav, .flac, .aac, .ogg, ... |
   | `Videos/` | .mp4, .mov, .avi, .mkv, .webm, ... |
   | `Archives/` | .zip, .rar, .tar, .7z, .iso, ... |
   | `Code/` | .py, .js, .ts, .html, .css, .json, ... |
   | `Fonts/` | .ttf, .otf, .woff, .woff2, ... |
   | `Others/` | Anything not matching the above |

4. A `.organize_log.json` is saved so you can undo the operation later.

---

## 💻 Requirements

* Python **3.8+** (recommended)
* No external dependencies — uses only the standard library
* Works on:
  * 🪟 **Windows**
  * 🍎 **macOS**
  * 🐧 **Linux**

---

## 🧠 How to Run

### 1️⃣ Clone or Download the Project

```bash
git clone https://github.com/Devraj-jha/Automatic-Folder-Organizer.git
cd Automatic-Folder-Organizer
```

### 2️⃣ Organize a Folder

```bash
python3 main.py ~/Downloads
```

Output:

```
Files found: 5

Organizing files...

  Moved: photo.jpg -> Images/
  Moved: resume.pdf -> Documents/
  Moved: song.mp3 -> Audio/
  Moved: movie.mp4 -> Videos/
  Moved: script.py -> Code/

Organized 5 file(s). Log saved for undo.
```

### 3️⃣ Preview Without Moving (Dry Run)

```bash
python3 main.py ~/Downloads --dry-run
```

```
Files found: 5

[DRY RUN] Organizing files...

  [dry-run] photo.jpg -> Images/
  [dry-run] resume.pdf -> Documents/
  [dry-run] song.mp3 -> Audio/

5 file(s) would be moved.
```

### 4️⃣ Undo the Last Organize

```bash
python3 main.py ~/Downloads --undo
```

```
Undoing last organize...

  Restored: photo.jpg
  Restored: resume.pdf
  Restored: song.mp3

Undone 3 move(s). Log removed.
```

### 5️⃣ Just Count Files

```bash
python3 main.py ~/Downloads --count
```

```
Files found: 5
```

### 6️⃣ Interactive Mode (No Arguments)

```bash
python3 main.py
```

```
Enter the full path of the folder to organize: ~/Downloads
```

---

## 🧩 Customize Categories

Open **`categories.py`** and edit the `CATEGORIES` dictionary:

```python
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".txt", ".docx", ".csv"],
    "Code": [".py", ".js", ".cpp"],
    "3D Models": [".stl", ".obj", ".fbx"],  # add your own!
}
```

---

## 🧰 Example: Before & After

### Before

```
Downloads/
├── photo.jpg
├── song.mp3
├── resume.pdf
├── movie.mp4
├── script.py
├── font.ttf
├── backup.zip
```

### After

```
Downloads/
├── Images/
│   └── photo.jpg
├── Audio/
│   └── song.mp3
├── Documents/
│   └── resume.pdf
├── Videos/
│   └── movie.mp4
├── Code/
│   └── script.py
├── Fonts/
│   └── font.ttf
├── Archives/
│   └── backup.zip
```

---

## 🧪 Running Tests

```bash
python3 -m unittest test_organizer -v
```

---

## 🧩 Future Improvements

* Add a **GUI version** using Tkinter
* Add **recursive mode** to organize sub-folders too
* Add **watch mode** to auto-organize new files
* Add colored terminal output

---

## 👨‍💻 Author

**Devraj Jha**
A Python learner focused on writing clean, modular, and practical automation tools.

> "Don't organize your files manually — let your code do it."

---

### ✅ License

This project is open-source and free to use for learning and personal automation purposes.
