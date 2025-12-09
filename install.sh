#!/usr/bin/bash

if [ -e $HOME/.local/bin/gp ]; then
    echo "'gitpush' already installed."
elif [ -e ./gp ]; then
    echo "Installing 'gitpush'"
    cp ./gp $HOME/.local/bin
fi

echo "'gitpush' successfully installed."
echo "To use:"
echo "'gp [[add] [repo.git]]'"
echo "For more information, see: https://github.com/elliethepuppy/gitpush"
