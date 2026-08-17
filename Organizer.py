

import argparse
import logging
from pathlib import Path
import shutil
from typing import Dict, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DEFAULT_EXTENSION_MAP: Dict[str, List[str]] = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".m4a"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv"],
    "Archives": [".zip", ".tar", ".gz", ".7z", ".rar"],
    "Executables": [".exe", ".msi", ".dmg", ".sh"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".json"]
}
