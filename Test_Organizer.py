# An automated test suite using pytest and temporary directories.

import pytest
from pathlib import Path
from organizer import FileOrganizer

@pytest.fixture
def sample_directory(tmp_path):
    """Creates temporary files for testing."""
    (tmp_path / "photo.jpg").write_text("fake image")
    (tmp_path / "doc.pdf").write_text("fake pdf")
    (tmp_path / "notes.txt").write_text("fake text")
    (tmp_path / "unknown.xyz").write_text("fake extension")
    return tmp_path

def test_organization(sample_directory):
    organizer = FileOrganizer(sample_directory)
    moved_count = organizer.organize()

    assert moved_count == 4
    assert (sample_directory / "Images" / "photo.jpg").exists()
    assert (sample_directory / "Documents" / "doc.pdf").exists()
    assert (sample_directory / "Documents" / "notes.txt").exists()
    assert (sample_directory / "Others" / "unknown.xyz").exists()

def test_dry_run(sample_directory):
    organizer = FileOrganizer(sample_directory)
    moved_count = organizer.organize(dry_run=True)

    assert moved_count == 4
    assert (sample_directory / "photo.jpg").exists()  # File stayed in place
    assert not (sample_directory / "Images").exists()
