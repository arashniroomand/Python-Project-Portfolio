from pathlib import Path

# Path to the root of the project (2 levels up from info.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# Folder where the files are stored
FILES_DIR = BASE_DIR / "files"

# PDF and image paths
FILE_PATH = str(FILES_DIR / "Report.pdf")
IMAGE_PATH = str(FILES_DIR / "image.jpg")
