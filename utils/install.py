#!/usr/bin/env python

# Python 3 Standard Library
import pathlib
import shutil


def install():
    root = pathlib.Path.cwd().parent
    dirs = [path for path in root.iterdir() if path.is_dir()]
    dirs = [dir_ for dir_ in dirs if (dir_ / "build").exists()]
    for dir_ in dirs:
        print(f"installing build in {dir_}")
        shutil.copy("build.py", dir_ / "build")


if __name__ == "__main__":
    install()
