import sys
import os
import time
import socket
import zipfile
import random


# import keyboard

#
# /mnt/c/Users/iyuna/source/repos
#

# keyboard.add_hotkey('Tab', lambda: print('Hello', end=' '))


def change_dir(pre_dir, pos_dir):
    pass


# Первый иф ломается проверка zip файла время от времени
if len(sys.argv) == 2 and zipfile.is_zipfile(sys.argv[1]):
#if len(sys.argv) == 2 and ".zip" in sys.argv[1]:
    path_file_system = sys.argv[1]
else:
    # print(sys.argv)
    print("Invalid file system!")
    sys.exit(1)

system = sys.platform
start_message = "Loading...\n\nWelcome to Hometask 01\n"
pre_name = f"[yunik@{socket.gethostname()} ~]# "
commands = ["pwd", "ls", "cd", "cat", "exit", "clear", "help"]
# command = ""

print(start_message)
current_path = ['root']

file_system = zipfile.ZipFile(path_file_system, 'a')
files = file_system.namelist()  # Список всех директорий

while 123:
    command = str(input(pre_name))
    if command == "test":
        print("test started")
        print(files)
    elif command == "help":
        print(commands)
    elif command == "cls":
        if system == "win32":
            os.system('cls')
        elif system == "linux":
            os.system('clear')
    elif command == "exit":
        sys.exit(1)
    elif command == "restart":
        os.system("cls")
        os.system(rf"cd {os.getcwd()}")
        os.system(rf"py main_h1.py {path_file_system}")
        sys.exit(1)
    # Нужно будет дописать pwd
    elif command == "pwd":
        for folder in current_path: print('/' + folder, end='')
        print()
    # Создание новой папки
    elif command == "mkdir":
        pass
    elif command == "ls":
        for _dir in files:
            if _dir.count('/') == 1 or (_dir.count('/') == 2 and _dir.count('.') == 0):
                print(_dir.split('/')[1], end=' ')
        print()
    elif "cd" in command:
        command = command.split(' ')
        print(command)
        pass
    else:
        print(f"sh: {command}: command not found", command)
