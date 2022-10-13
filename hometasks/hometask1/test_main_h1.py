import os
import sys
import socket
import zipfile


# os.getlogin()
# /mnt/c/Users/iyuna/source/repos/python/yunikeil/configYPR/hometasks/hometask1
# test_main_h1.py file_system.zip


class Commands(object):
    def __init__(self):
        self.commands = [["pwd", shell.pwd], ["ls", shell.ls], ["cd", shell.cd], ["cat", shell.cat]]
        # commands[0][1]("123")
        # Можно также списком ->
        # commands = {'pwd':pwd, 'ls':ls, 'cd':cd, 'cat':cat}
        pass

    @staticmethod
    def pwd(string):
        print(f"pwd command: {string}")
        pass

    @staticmethod
    def ls(string):
        print(f"ls command: {string}")
        pass

    @staticmethod
    def cd(string):
        print(f"cd command: {string}")
        pass

    @staticmethod
    def cat(string):
        print(f"cat command: {string}")
        pass

    pass


class VShell(Commands):
    def __init__(self):
        super().__init__()
        self.system = sys.platform
        self.current_path = ['root']

    @staticmethod
    def startExpectationCommand():
        cmd_input = str(input(pre_name))
        return cmd_input, len(cmd_input.split(' '))


shell = VShell()

if len(sys.argv) == 2 and zipfile.is_zipfile(sys.argv[1]):
    path_file_system = sys.argv[1]
else:
    print("Invalid file system!"); sys.exit(1)

start_message = "Loading...\n\nWelcome to Hometask 01\n"
pre_name = f"[yunik@{socket.gethostname()} ~]# "

print(start_message)

while 123:
    commandIN, command_len = shell.startExpectationCommand()
    print(f"commandIN: {commandIN}\ncommand_len: {command_len}")
    for command in shell.commands:
        if command[0] in commandIN:
            command[1](commandIN)
