import sys
import os
import time
import zipfile
import random


def slow_lettering(string)

# import keyboard

#
#
#

# eyboard.add_hotkey('Tab', lambda: print('Hello', end=' '))

if len(sys.argv) == 2 and zipfile.is_zipfile(sys.argv[1]):
    path_file_system = sys.argv[1]
else:
    print("Invalid file system!")
    sys.exit(1)

system = sys.platform
start_message = "Loading...\n\nWelcome to Hometask 01\n"
pre_name = "[root@localhost ~]# "
commands = ["pwd", "ls", "cd", "cat", "exit", "clear", "help"]
# command = ""

print(start_message)
current_path = ['root']

file_system = zipfile.ZipFile(path_file_system, 'a')
files = file_system.namelist()  # Список всех директорий


def slow_lettering(string):
    rand = random.randint(0,50)
    for letter in string:
        print(letter)
        time.sleep(rand/100)


def change_dir(pre_dir, pos_dir):
    pass


while 123:
    command = input(pre_name)
    match command:
        case "test":
            i = str(input())
            slow_lettering(i)
        case "exit":
            sys.exit(1)
        case "cls":
            if system == "win32":
                os.system('cls')
            elif system == "linux":
                os.system('clear')
        case "help":
            print(commands)
        case "restart":
            os.system("cls")
            os.system(rf"cd {os.getcwd()}")
            os.system(rf"py main_h1.py {path_file_system}")
            sys.exit(1)
        case "pwd":
            print(current_path)
        case "ls" :
            for dir in files:
                if '.' in dir:
                    # print(files) # print(dir.rpartition('/')[len(dir.rpartition('/')) - 1])
                    dir = dir.split('/')
                    print(dir.index('file2.txt'))
                    print(dir)
        case _:
            print(f"sh: {command}: command not found", command)
