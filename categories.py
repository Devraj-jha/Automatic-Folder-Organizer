# categories.py

# This dictionary maps each folder name to a list of file extensions.
# When the organizer sees a file ending with one of these extensions,
# it will move it into that folder.

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".m4a"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    "Others": []  # if it doesn't match any above
}
