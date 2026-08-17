

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

class FileOrganizer:
    """Handles organizing files in a given directory based on extensions."""

    def __init__(self, target_dir: Path, custom_map: Dict[str, List[str]] = None):
        self.target_dir = target_dir.resolve()
        self.extension_map = custom_map or DEFAULT_EXTENSION_MAP

    def _get_category(self, extension: str) -> str:
        """Determines category for a given file extension."""
        ext_lower = extension.lower()
        for category, extensions in self.extension_map.items():
            if ext_lower in extensions:
                return category
        return "Others"

    def organize(self, dry_run: bool = False) -> int:
        """Organizes all loose files in target_dir into category folders."""
        if not self.target_dir.exists() or not self.target_dir.is_dir():
            logging.error(f"Target path '{self.target_dir}' does not exist or is not a directory.")
            return 0

        moved_count = 0

        for item in self.target_dir.iterdir():
            # Skip subdirectories and system files
            if item.is_dir() or item.name.startswith("."):
                continue

            category = self._get_category(item.suffix)
            destination_dir = self.target_dir / category
            destination_path = destination_dir / item.name

