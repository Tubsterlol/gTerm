from pathlib import Path


def banner():
    ascii_art = Path(__file__).parent.parent / "ascii_art.txt"
    return ascii_art.read_text()
