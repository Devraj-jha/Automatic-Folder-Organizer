Automatically sort files in a directory by type (e.g., move all .jpg → “Images” folder)
The goal of this programme is to give the use ability to path folder. 
then they can automatically orgainze the files. 

we are trying to break down programms into simple logical chunks so each file does one job. 

🗂️ Folder Organizer (Python Automation Tool)
📖 Overview

The Folder Organizer is a simple Python automation tool that helps you clean up messy folders like your Downloads, Desktop, or Documents.
It automatically sorts files into categorized folders (like Images, Documents, Videos, etc.) based on their file extensions.

No more hunting for lost files — one command organizes your entire folder neatly in seconds.

=>  Features

✅ Automatically detects file types (images, documents, videos, code, etc.)
✅ Creates folders automatically if they don’t exist
✅ Moves files safely to their correct categories
✅ Works on macOS, Windows, and Linux
✅ Easy to customize — add your own file types in categories.py
✅ Modular structure (code split into multiple files for clarity)

📂 Project Structure
folder_organizer/
│
├── main.py              # Entry point – runs the program
├── file_utils.py        # Contains file organization logic
└── categories.py        # Defines file categories and extensions

⚙️ How It Works

You run the program in your terminal.

It asks for the path of the folder you want to organize.

It checks all files inside the folder.

Based on each file’s extension (.jpg, .pdf, .mp3, etc.), it moves it into:

Images/

Documents/

Videos/

Audio/

Code/

Archives/

Others/

It prints out what it’s moving in real-time.

💻 Requirements

Python 3.8 or above (recommended)

Works on:

=> Windows
=> macOS
=> Linux

🧠 How to Run
1️⃣ Clone or Download the Project

If you have git:

git clone https://github.com/yourusername/folder-organizer.git
cd folder-organizer


Or just manually download and unzip it.

2️⃣ Run the Program

In your terminal:

python3 main.py

3️⃣ Enter Folder Path

When asked:

Enter the full path of the folder to organize:


Example (macOS):

/Users/DJ/Downloads


Example (Windows):

C:\Users\DJ\Downloads


The program will start moving files into their respective folders and show results like:

✅ Moved: photo.jpg → Images/
✅ Moved: notes.txt → Documents/
✅ Moved: song.mp3 → Audio/
🎉 Folder organization complete!

🧩 How to Customize Categories

Open the file categories.py and edit the CATEGORIES dictionary.

Example:

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Code": [".py", ".js", ".cpp"],
    "Others": []
}


You can add your own file types or categories easily.

🧰 Example Before & After
Before:
Downloads/
├── photo.jpg
├── song.mp3
├── resume.pdf
├── movie.mp4
├── script.py

After:
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

⚠️ Tips

Try it first on a test folder (to avoid moving important files by accident).

Always enter the full path (not just the folder name).

The program skips existing folders — it only moves files.

