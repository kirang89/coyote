#!/usr/bin/env bash
#
# The setup script
#

sh ~/workspace/coyote/scripts/install_pylibmc.sh
echo "Pylibmc installed"
echo "alias search='~/workspace/coyote/search.py'" >> ~/.bashrc
