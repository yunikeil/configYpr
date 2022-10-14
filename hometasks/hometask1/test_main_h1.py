import os
import sys
import socket
import zipfile


# os.getlogin()
# /mnt/c/Users/iyuna/source/repos/python/yunikeil/configYPR/hometasks/hometask1
# test_main_h1.py file_system.zip


class Functional(object):
    @staticmethod
    def create_methods_list(class_name_):
        list_methods_ = []
        for attribute in dir(class_name_):
            # Получить значение атрибута
            attribute_value = getattr(class_name_, attribute)
            # Проверьте, что он доступен для вызова
            if callable(attribute_value):
                # Фильтровать все методы по (__ префиксу)
                if not attribute.startswith('__'):
                    list_methods_.append([attribute])
        for value_, string_ in enumerate(list_methods_):
            list_methods_[value_].append(getattr(class_name_, string_[0]))
        return list_methods_


class Commands(object):
    """
    self.commands = [["pwd", self.pwd], ["ls", self.ls], ["cd", self.cd], ["cat", self.cat], ["s", self.s]]
    # commands[0][1]("123")
    # Можно также списком ->
    # commands = {'pwd':pwd, 'ls':ls, 'cd':cd, 'cat':cat}
    """

    def __init__(self):
        self.commands = Functional.create_methods_list(Commands)
        print("init of Commands:\n", self.commands)
        pass

    @staticmethod
    def pwd(string, VShell_):
        print(f"pwd command: {string}")
        pass

    @staticmethod
    def ls(string, VShell_):
        print(f"ls command: {string}")
        pass

    @staticmethod
    def cd(string, VShell_):
        print(f"cd command: {string}")
        pass

    @staticmethod
    def cat(string, VShell_):
        print(f"cat command: {string}")
        pass

    @staticmethod
    def s(string, VShell_):  # вызывать отсюда специальные функции
        for SpecCommand_ in VShell_.special_commands:
            if SpecCommand_[0] in string:
                SpecCommand_[1](string, VShell_)
        pass


class SpecialCommands(object):
    """
    # __init__
    self.special_commands = [["test0", self.test0], ["test1", self.test1], ["restart", self.restart],
                             ["exit", self.exit]]
    """

    def __init__(self):
        self.special_commands = Functional.create_methods_list(SpecialCommands)
        print("init of SpecialCommands:\n", self.special_commands)

    # Функции для отладки, извне задания
    @staticmethod
    def test0(string, VShell_):
        print(f"test0\nstring: {string}\nVShell_obj: {VShell_}")

    @staticmethod
    def test1(string, VShell_):
        print(VShell_.special_commands)
        # VShell_.special_commands__[2](string, VShell_)
        # print(f"test1\nstring: {string}\nVShell_obj: {VShell_}")

    @staticmethod
    def exit(string, VShell_):
        sys.exit(1)

    @staticmethod
    def restart(string, VShell_):  # нужно получать путь из дочернего объекта, а не из основной программы
        if VShell_.system == "win32":
            i_ = str(input("Убедитесь, что запускаете через cmd, powershell не поддерживает данную команду."
                           "\nY-продолжить выполнение, n-пропустить выполнение\n> "))
            if i_ == 'Y':
                os.system("cls")
            else:
                return 0
        else:
            os.system("clear")
        os.system(rf"cd {os.getcwd()}")
        if VShell_.system == "win32":
            print(rf"python test_main_h1.py {VShell_.path_file_system}")
        else:
            os.system(rf"python3 test_main_h1.py {VShell_.path_file_system}")
        sys.exit(1)


class VShell(Commands, SpecialCommands):

    def __init__(self):
        Commands.__init__(self)
        SpecialCommands.__init__(self)
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
    if commandIN:
        i = False
        for command in shell.commands:
            if command[0] == commandIN.split(' ')[0]:
                i = True
                command[1](commandIN, shell)
        if not i: print(f"sh: {commandIN}: command not found", commandIN.split(' ')[0])
