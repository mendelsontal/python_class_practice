#!/usr/bin/env bash
############################################################
# Developed by: Tal & Baruch 
# Description: Verify if python3 is installed
# Date:07/03/2025                                                                                                                                   #
# Version: 1.0.0
############################################################

[[ $(which python3s) == "" ]] && printf "Error: Python3 is not installed.\nSuggestion: sudo apt-get install python3\n"
