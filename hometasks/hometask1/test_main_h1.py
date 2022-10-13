import os
import sys
import socket
import zipfile


# os.getlogin()
# /mnt/c/Users/iyuna/source/repos/python/yunikeil/configYPR/hometasks/hometask1
# test_main_h1.py file_system.zip


class Commands(object):
    def __init__(self):
        self.commands = [["pwd", self.pwd], ["ls", self.ls], ["cd", self.cd], ["cat", self.cat], ["s", self.s]]
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

    @staticmethod
    def s(): # вызывать отсюда специальные функции, с утра мб передумаю но вообще возможно можно так
        print()
        pass


class SpecialCommands(object):
    def __init__(self):
        self.special_commands = [["test", self.test], ["test1", self.test1]]

    # Функции для отладки, извне задания
    @staticmethod
    def test(string):
        sys.exit(1)

    @staticmethod
    def test1(string, path_file_system): # нужно получать путь из дочернего объекта, а не из основной программы
        os.system(rf"cd {os.getcwd()}")
        os.system(rf"python3 test_main_h1.py {path_file_system}")


class VShell(Commands, SpecialCommands):

    def __init__(self):
        super().__init__()
        self.system = sys.platform
        self.path_file_system = None
        self.current_path = ['root']

    def start(self):
        if len(sys.argv) == 2 and zipfile.is_zipfile(sys.argv[1]):
            self.path_file_system = sys.argv[1]
        else:
            print("Invalid file system!")
            sys.exit(1)

    @staticmethod
    def startExpectationCommand():
        cmd_input = str(input(pre_name))
        return cmd_input, len(cmd_input.split(' '))


shell = VShell()
shell.start()

start_message = "Loading...\n\nWelcome to Hometask 01\n"
pre_name = f"[yunik@{socket.gethostname()} ~]# "

print(start_message)

while 123:
    commandIN, command_len = shell.startExpectationCommand()
    print(f"commandIN: {commandIN}\ncommand_len: {command_len}")
    i = False
    for command in shell.commands:
        if command[0] in commandIN:
            i = True
            command[1](commandIN)

