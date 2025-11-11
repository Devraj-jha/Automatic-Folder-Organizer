
---

# 🗂️ Folder Organizer (Python Automation Tool)

## 📖 Overview

The **Folder Organizer** is a lightweight Python automation tool that automatically sorts files in a directory based on their type.
It gives the user the ability to provide any folder path — and with one command, it organizes the entire folder neatly by moving each file into its appropriate category (e.g., all `.jpg` → `Images`, `.pdf` → `Documents`, etc.).

This project was designed with a focus on **clarity and structure** — breaking the program into simple, logical chunks so that each file has one specific job.

No more messy Downloads folders — one script keeps your workspace clean and structured.

---

## ✨ Features

*  Automatically detects file types (images, documents, videos, code, etc.)
*  Creates categorized folders automatically if they don’t exist
*  Safely moves files to their respective categories
*  Works seamlessly on **macOS**, **Windows**, and **Linux**
*  Fully customizable — easily add or edit file types in `categories.py`
*  Modular design with clear separation of logic across files

---

## 📂 Project Structure

```
folder_organizer/
│
├── main.py          # Entry point – runs the program
├── file_utils.py    # Contains file organization logic
└── categories.py    # Defines file categories and extensions
```

---

## ⚙️ How It Works

1. Run the program in your terminal.
2. Enter the full path of the folder you want to organize.
3. The program scans all files in that folder.
4. Based on each file’s extension (`.jpg`, `.pdf`, `.mp3`, etc.), it moves the file into:

   * `Images/`
   * `Documents/`
   * `Videos/`
   * `Audio/`
   * `Code/`
   * `Archives/`
   * `Others/`
5. Each file moved is displayed in real-time with confirmation messages.

---

## 💻 Requirements

* Python **3.8+** (recommended)
* Works on:

  * **Windows**
  *  **macOS**
  *  **Linux**

---

## 🧠 How to Run

### 1️⃣ Clone or Download the Project

If you have **Git**:

```bash
git clone https://github.com/Devraj-jha/Automatic-Folder-Organizer.git
cd Automatic-Folder-Organizer
```

Or manually download and unzip the project.

---

### 2️⃣ Run the Program

```bash
python3 main.py
```

---

### 3️⃣ Enter the Folder Path

When prompted:

```
Enter the full path of the folder to organize:
```

**Example (macOS):**

```
/Users/DJ/Downloads
```

**Example (Windows):**

```
C:\Users\DJ\Downloads
```

The program will begin organizing your files and show output like:

```
✅ Moved: photo.jpg → Images/
✅ Moved: notes.txt → Documents/
✅ Moved: song.mp3 → Audio/
🎉 Folder organization complete!
```

---

## 🧩 Customize Categories

Open **`categories.py`** and edit the `CATEGORIES` dictionary to include your own file types or categories.

Example:

```python
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Code": [".py", ".js", ".cpp"],
    "Others": []
}
```

You can add new types easily — for example, add `"Videos": [".mp4", ".mov"]` or `"Audio": [".mp3", ".wav"]`.

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
```

---

## ⚠️ Tips

* 🧪 Test it first on a **dummy folder** to see how it works before using it on important files.
* 📁 Always provide the **full path** (not just folder name).
* 🚫 The program skips folders — it only moves files.
* 🧠 The code is modular, so you can easily extend it to support logging, GUI, or undo functionality later.

---

---

### ✅ License

This project is open-source and free to use for learning and personal automation purposes.

---
