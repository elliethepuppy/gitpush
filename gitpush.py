#!/usr/bin/python

import sys
import subprocess


def push() -> None:
    subprocess.run(["git", "push", "-u", "origin", "main"])

def add(repo: str) -> None:
    subprocess.run(["git", "remote", "add", "origin", repo])

def main(args) -> None:
    if len(args) == 1:
        push()
        return None

    if args[1] == "add":
        if len(args) == 2:
            raise Exception("Too few arguments for `gp add`\
            USAGE: `gp add [link to github repo]`\
            EXAMPLE: `gp add git@github.com:<username>/<repo>.git`")
        elif "@" and ".git" not in args[2]:
            raise Exception(f"ERROR: {args[2]} is not a valid git repo")
        else:
            add(args[2])
            answer = input("Push now? y/[n] > ")
            if answer == "y":
                push()


if __name__ == "__main__":
    main(sys.argv)
