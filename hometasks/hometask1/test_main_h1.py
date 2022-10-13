import os
import sys
import socket
import zipfile


def pwd(command):
    pass


def ls(command):
    pass


def cd(command):
    pass


def cat(command):
    pass


#commands = ["pwd", "ls", "cd", "cat", "exit", "clear", "help"]
#commands = {'pwd':pwd, 'ls':ls, 'cd':cd, 'cat':cat}
commands = [["pwd", pwd], ["ls", ls], ["cd", cd], ["cat", cat]]  # commands[0][1]("123")


if len(sys.argv) == 2 and zipfile.is_zipfile(sys.argv[1]):
    path_file_system = sys.argv[1]
else:
    print("Invalid file system!")
    sys.exit(1)

system = sys.platform
start_message = "Loading...\n\nWelcome to Hometask 01\n"
pre_name = f"[yunik@{socket.gethostname()} ~]# "

print(start_message)
current_path = ['root']


