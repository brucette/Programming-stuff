#!/usr/bin/env python
 
from time import sleep
import platform
import subprocess
 
 
command = "cls" if platform.system().lower() == "windows" else "clear"
 
 
def spinner():
    spin = ["\\", "|", "/", "-", "\\", "|", "/", "-"]
    for sp in spin:
        print("Computer is thinking: ", sp)
        sleep(1)
        subprocess.call(command)
 
 
spinner()