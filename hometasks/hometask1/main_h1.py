import os
import sys
import socket
import zipfile

# /mnt/c/Users/iyuna/source/repos/python/yunikeil/configYPR/hometasks/hometask1
# test_main_h1.py file_system.zip


login = "yunik"  # os.getlogin()
hostname = socket.gethostname
start_message = "Loading...\n\nWelcome to Hometask 01\n"


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
    def __init__(self):
        self.commands = Functional.create_methods_list(Commands)

    @staticmethod
    def pwd(string, VShell_):
        if len(string.split(' ')) == 1: print('/' + '/'.join(VShell_.current_path))

    @staticmethod
    def ls(string, VShell_):
        if len(string.split(' ')) == 1:
            z_ = False
            passed = []
            current_folder_ = VShell_.current_path[len(VShell_.current_path) - 1]
            for file_ in VShell_.files:
                directory_ = file_.split('/')
                for value_, folder_ in enumerate(directory_):
                    if folder_ == current_folder_ and directory_[value_ + 1] not in passed:
                        if directory_[value_ + 1]: z_ = True
                        if z_:
                            passed.append(directory_[value_ + 1])
                            print(directory_[value_ + 1], end=' ')
            if z_: print()

    @staticmethod
    def cd(string, VShell_):
        # отдаляемся на шаг назад
        if len(string.split(' ')) == 1 and len(VShell_.current_path) != 1:
            VShell_.current_path.pop(len(VShell_.current_path) - 1)
        # идём на указанную директорию
        elif len(string.split(' ')) == 2:
            if string.split(' ')[1].split('/')[0] == "root" and string.split(' ')[1].split('/')[1] == '':
                VShell_.current_path = ['root']
            elif string.split(' ')[1].split('/')[0] == "root":
                for directories_ in VShell_.files:
                    if directories_[len(directories_) - 1] == '/': directories_ = directories_[:-1]
                    if str(string.split(' ')[1]) == str(directories_):
                        VShell_.current_path = directories_.split('/')
                        return 0
                print("can't cd to " + string.split(' ')[1] + ": No such file or directory")
            else:
                for directories_ in VShell_.files:
                    if directories_[len(directories_) - 1] == '/': directories_ = directories_[:-1]
                    if str('/'.join(VShell_.current_path) + '/' + string.split(' ')[1]) == str(directories_):
                        VShell_.current_path = directories_.split('/')
                        return 0
                print("can't cd to " + str('/' + '/'.join(VShell_.current_path) + '/' + string.split(' ')[1]) +
                      ": No such file or directory")

    # Изменить условие кета, в тестовой версии поменял.
    @staticmethod
    def cat(string, VShell_):
        if len(string.split(' ')) == 2:
            current_path_str_without_first_slash = '/'.join(VShell_.current_path)
            name_file = string.split(' ')[1]
            files_obj = VShell_.file_system.infolist()
            files_list = VShell_.file_system.namelist()
            for file_ in files_list:
                if current_path_str_without_first_slash + '/' + name_file == str(file_):
                    print('> ', end='')
                    for symbol_ in VShell_.file_system.read(file_).decode('utf-8'):
                        if symbol_ != '\n':
                            print(symbol_, end='')
                        else:
                            print('\n> ', end='')
                    print()
                    return 0
            print("can't open " + name_file + ": No such file or directory")

    @staticmethod
    def s(string, VShell_):  # вызывать отсюда специальные функции
        for SpecCommand_ in VShell_.special_commands:
            if SpecCommand_[0] in string:
                SpecCommand_[1](string, VShell_)


class SpecialCommands(object):
    def __init__(self):
        self.special_commands = Functional.create_methods_list(SpecialCommands)
        # print("init of SpecialCommands:\n", self.special_commands)

    # Функции для отладки, извне задания
    @staticmethod
    def test0(string, VShell_):
        print(VShell_.files)

    @staticmethod
    def test1(string, VShell_):
        print(f"test1\nstring: {string}\nVShell_obj: {VShell_}")

    @staticmethod
    def exit(string, VShell_):
        sys.exit(1)

    @staticmethod
    def restart(string, VShell_):  # нужно получать путь из дочернего объекта, а не из основной программы
        if VShell_.system == "win32":
            i_ = str(input("Убедитесь, что запускаете через cmd, "
                           "powershell не поддерживает данную команду.\n\033[33mY\033[0m-продолжить "
                           "выполнение\n\033[33mn\033[0m-пропустить выполнение\n> "))
            if i_ == 'Y':
                os.system("cls")
            else:
                return 0
        else:
            os.system("clear")
        os.system(rf"cd {os.getcwd()}")
        if VShell_.system == "win32":
            os.system(rf"py test_main_h1.py {VShell_.path_file_system}")
        else:
            os.system(rf"python3 test_main_h1.py {VShell_.path_file_system}")
        sys.exit(1)


class VShell(Commands, SpecialCommands):

    def __init__(self):
        Commands.__init__(self)
        SpecialCommands.__init__(self)
        self.other_pre_name = None
        self.pre_name_root = None
        self.system = sys.platform
        self.path_file_system = None
        self.file_system = None
        self.files = None
        self.current_path = ['root']

    def start(self):
        if len(sys.argv) == 2 and zipfile.is_zipfile(sys.argv[1]):
            self.path_file_system = sys.argv[1]
            self.file_system = zipfile.ZipFile(self.path_file_system, 'a')
            self.files = self.file_system.namelist()
            print(start_message)
        else:
            print("Invalid file system!")
            sys.exit(1)

    def startExpectationCommand(self):
        self.pre_name_root = str("\033[32m{}\033[0m{}\033[34m{}\033[0m{}"
                                 .format(f"{login}@{hostname()}", ':', '~', '$ '))
        self.other_pre_name = str("\033[32m{}\033[0m{}\033[34m{}\033[0m{}"
                                  .format(f"{login}@{hostname()}", ':', f"/{'/'.join(self.current_path)}", '$ '))
        if len(self.current_path) == 1:
            cmd_input = str(input(self.pre_name_root))
        else:
            cmd_input = str(input(self.other_pre_name))
        return cmd_input, len(cmd_input.split(' '))


shell = VShell()
shell.start()

while 123:
    commandIN, command_len = shell.startExpectationCommand()
    if commandIN:
        i = False
        for command in shell.commands:
            if command[0] == commandIN.split(' ')[0]:
                i = True
                command[1](commandIN, shell)
        if not i: print(f"sh: {commandIN}: command not found", commandIN.split(' ')[0])
