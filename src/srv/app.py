#!/usr/bin/env python3
############################################################
# Developed by: Tal & Baruch 
# Description: try and play with project structure and module import
# Date:07/03/2025                                                                                                                                   #
# Version: 1.0.1
############################################################

import os, sys, time

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.lib import lib

user_name = input('[?] Please provide name, habibi: ')

hello_user_name_value = lib.hello_name(user_name)
goodbye_user_name_value = lib.goodbye_name(user_name)

print(f'[+] {hello_user_name_value}')
time.sleep(2)
print('[+] Running computing jobs')
time.sleep(2)
print('[+] Still computing')
time.sleep(2)
print('[+] Computations completed successfully')
time.sleep(2)
print(f'[+] {goodbye_user_name_value}')
