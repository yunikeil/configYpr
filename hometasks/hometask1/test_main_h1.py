import os
import sys
import socket
import zipfile


class Commands(object):
    def pwd(self, string):
        pass

    def ls(self, string):
        pass

    def cd(self, string):
        pass

    def cat(self, string):
        pass
    pass


class VShell(Commands):
    @staticmethod
    def startExpectationCommand():
        cmd_input = str(input(pre_name))
        return cmd_input, len(cmd_input.split(' '))
    pass


shell = VShell()
# commands = {'pwd':pwd, 'ls':ls, 'cd':cd, 'cat':cat}
commands = [["pwd", shell.pwd], ["ls", shell.ls], ["cd", shell.cd], ["cat", shell.cat]]  # commands[0][1]("123")

if len(sys.argv) == 2 and zipfile.is_zipfile(sys.argv[1]): path_file_system = sys.argv[1]
else: print("Invalid file system!"); sys.exit(1)

system = sys.platform
start_message = "Loading...\n\nWelcome to Hometask 01\n"
pre_name = f"[yunik@{socket.gethostname()} ~]# "

print(start_message)
current_path = ['root']


while 123:
    command, command_len = shell.startExpectationCommand()
    print(f"command: {command}\ncommand len: {command_len}")







