import zipfile
import os
import sys


# Основной класс эмулятора командной строки
class Vshell():
    # Конструктор
    def __init__(self, file_system_image):
        self.current_folder = "/"
        self.file_system_image = file_system_image

    # Вывод сведений о рабочей директории
    def pwd(self):
        if "/" == self.current_folder:
            print("/")
        else:
            print(self.current_folder[:-1])

    # Чтение файла и  вывод его содержимого на экран
    def cat(self, file_to_open):
        for file in file_system_image.infolist():
            if self.current_folder[1:] + file_to_open in file.filename or file_to_open[0] == "/" and file_to_open[
                                                                                                     1:] in file.filename or self.current_folder == "/" and file_to_open == file.filename:
                byte_text = file_system_image.read(file)
                print(byte_text.decode('utf-8'))
                break
        else:
            print("can't open " + file_to_open + ": No such file or directory")

    # Вывод содержимого директории
    def ls(self):
        if self.current_folder == "/":
            for name in file_system_image.namelist():
                if "/" not in name:
                    print(name)
                elif "." not in name and "/" not in name[:-1]:
                    print(name[:-1])
        else:
            for name in file_system_image.namelist():
                if self.current_folder[1:] in name and self.current_folder[1:] != name:
                    if "/" not in name[len(self.current_folder) - 1:]:
                        print(name[len(self.current_folder) - 1:])
                    elif "." not in name[len(self.current_folder) - 1:] and "/" not in name[
                                                                                       len(self.current_folder) - 1:-1]:
                        print(name[len(self.current_folder) - 1:-1])

    # Изменение рабочей директории
    def cd(self, folder):
        # Если выбрана корневая папка
        if "/" == folder[0] and len(folder) == 1 or folder == "~":
            self.current_folder = "/"
        # Если нужно вернуться на одну директорию назад
        elif folder[0] == "-" and len(folder) == 1 or folder[0] == "." and folder[1] == "." and len(folder) == 2:
            if self.current_folder == "/":
                if folder[0] == "-":
                    self.pwd()
            else:
                i = len(self.current_folder) - 1
                while (self.current_folder[i - 1] != "/"):
                    i -= 1
                self.current_folder = self.current_folder[:i]
                if folder[0] == "-":
                    self.pwd()
        # Если путь абсолютный
        elif "/" == folder[0]:
            for name in file_system_image.namelist():
                if folder[1:] in name:
                    self.current_folder = folder + "/"
                    break
            else:
                print("can't cd to " + folder + ": No such file or directory")
        # Если путь относительный
        else:
            for name in file_system_image.namelist():
                if (self.current_folder + folder)[1:] == name[:-1]:
                    self.current_folder = self.current_folder + folder + "/"
                    break
            else:
                print("can't cd to " + folder + ": No such file or directory")

    # Основной цикл
    def mainLoop(self):
        while True:
            if self.current_folder == "/":
                print(os.getlogin() + ":~" + "$", end=" ")
            else:
                print(os.getlogin() + ":~" + self.current_folder[:-1] + "$", end=" ")
            command = input()

            # Если помимо команды есть ещё и путь
            if " " in command:
                command, folder = command.split(" ", 1)

            if command == "ls":
                self.ls()
            elif command == "pwd":
                self.pwd()
            elif command == "cat":
                self.cat(folder)
            elif command == "cd":
                self.cd(folder)
            else:
                print(command + ": not found")


# Основной код программы

path = sys.argv[1]

file_system_image = zipfile.ZipFile(path, 'r')
vshell = Vshell(file_system_image)
vshell.mainLoop()