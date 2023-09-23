import os
from pathlib import Path


def baseDir():
    return f"{Path(__file__).resolve().parent.parent}"

def appDir():
    baseDir = f"{Path(__file__).resolve().parent.parent}"
    # come back one segment:
    return f"{baseDir[:baseDir.rindex(os.path.sep)]}{os.path.sep}history"

