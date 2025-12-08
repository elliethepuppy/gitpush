#!/usr/bin/python

import subprocess

def main() -> None:
    subprocess.run(["git", "push", "-u", "origin", "main"])

if __name__ == "__main__":
    main()
