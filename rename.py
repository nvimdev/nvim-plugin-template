#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys
pdir = os.getcwd()

# ANSI color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

def print_colored(message, color):
    print(color + message + Colors.RESET)

if len(sys.argv) != 2:
    print_colored("plugin name is missing", Colors.RED)
    sys.exit(1)

new_name = sys.argv[1]
for dir in os.listdir(pdir):
    if dir == "lua":
        os.rename(os.path.join("lua", "nvim-plugin-template"), os.path.join("lua",new_name))
        print_colored("Renamed files under lua folder successed", Colors.GREEN)
    if dir == "plugin":
        os.rename(os.path.join("plugin", "nvim-plugin-template.lua"),
                  os.path.join("plugin",new_name + ".lua"))
        print_colored("Renamed files under plugin folder successed", Colors.GREEN)
    if dir == 'doc':
        os.rename(os.path.join("doc", "nvim-plugin-template.txt"),
                  os.path.join("doc",new_name + ".txt"))
        print_colored("Renamed files under doc folder successed", Colors.GREEN)
    if dir == '.github':
        with open(os.path.join(".github","workflows","ci.yml"), 'r+') as f:
            d = f.read()
            t = d.replace('nvim-plugin-template', new_name)
            f.seek(0, 0)
            f.write(t)
        print_colored("Ci yaml has been updated", Colors.GREEN)

choice = input("Do you need plugin folder in your plugin (y|n): ")
if choice.lower() == 'n':
    os.remove(os.path.join(os.getcwd(), 'plugin'))

choice = input("Do you want also remove example code in init.lua and test (y|n): ")
if choice.lower() == 'y':
    with open(os.path.join(pdir, 'lua',new_name,'init.lua'), 'w') as f:
        f.truncate()

    with open(os.path.join(pdir, 'test','plugin_spec.lua'), 'w') as f:
        f.truncate()

os.remove(os.path.join(os.getcwd(), 'rename.py'))
print_colored("All works done enjoy", Colors.YELLOW)
