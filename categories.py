# categories.py

# This dictionary maps each folder name to a list of file extensions.
# When the organizer sees a file ending with one of these extensions,
# it will move it into that folder.

CATEGORIES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp",
        ".tiff", ".tif", ".heic", ".heif", ".ico",
    ],
    "Documents": [
        ".pdf", ".docx", ".doc", ".txt", ".pptx", ".ppt",
        ".xlsx", ".xls", ".csv", ".md", ".odt", ".epub", ".rtf",
    ],
    "Audio": [
        ".mp3", ".wav", ".m4a", ".flac", ".aac", ".ogg", ".wma",
    ],
    "Videos": [
        ".mp4", ".mov", ".avi", ".mkv", ".wmv", ".webm", ".flv",
    ],
    "Archives": [
        ".zip", ".rar", ".tar", ".gz", ".7z", ".bz2", ".xz", ".iso",
    ],
    "Code": [
        ".py", ".js", ".ts", ".html", ".css", ".cpp", ".c", ".h",
        ".java", ".rb", ".go", ".rs", ".sh", ".json", ".xml",
        ".sql", ".php", ".swift", ".kt",
    ],
    "Fonts": [
        ".ttf", ".otf", ".woff", ".woff2", ".eot",
    ],
}
