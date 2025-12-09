# Purpose

To make my life a little easier

# Installation

## First

Before installing, you'll have to download the repo. From your `$HOME` directory, run: `git clone https://github.com/elliethepuppy/gitpush.git`

## Okay, onward

Installation can be performed two ways:

1. Copy the `gp` file to `$HOME/.local/bin`, either with a GUI file manager or with `cp gp $HOME/local/bin`.

2. An install script, `install.sh`, has been created to make things a little easier. All it does is check for the presence of `gp` in `$HOME/.local/bin`, and if it does not already exist, copies `gp` from the current dir to `$HOME/.local/bin`, which is all that's required\*. Simply invoke `./install.sh` from the gitpush directory.

# Uninstallation

`rm $HOME/.local/bin/gp`

# Usage

Calling `gp` invokes `git push -u origin main` using python's `subprocess` module. If you haven't yet set the upstream, you can call `gp add [link@yourremote.xxx:username/repo.git]`

\>-------------------------------------------------------------------------------<

<sub>let me know if it sucks</sub>

<sup>*: you need python, obvs</sup>
