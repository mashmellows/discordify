import sys
from cx_Freeze import setup, Executable
import os

includes = []
include_files = [r'C:\Users\<User>\AppData\Local\Programs\Python\Python35\DLLs\tcl86t.dll',
                 r'C:\Users\<User>\AppData\Local\Programs\Python\Python35\DLLs\tk86t.dll',
                 'token.txt',
                 'icon.ico']

os.environ['TCL_LIBRARY'] = r'C:\Users\<User>\AppData\Local\Programs\Python\Python35\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\<User>\AppData\Local\Programs\Python\Python35\tcl\tk8.6'





base = "Win32GUI"

setup(  name = "Discordify",
        version = "1.0",
        description = "Discord and Spotify Integration",
        options = {"build_exe":  {'packages': ['tkinter','discord','asyncio'],"includes": includes, "include_files": include_files}},
        executables = [Executable("Discordify.py", base=base,icon='icon.ico')])
