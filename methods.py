import os
import platform
import shutil


def is_file(path):
    return os.path.isfile(path)


def is_folder(path):
    return os.path.isdir(path)


def createFolder():
    name = input('Введите название папки: ')
    os.mkdir(name)


def removeFolder():
    name = input('Введите название элемента: ')
    if os.path.exists(name):
        if is_file(name):
            os.remove(name)
        if is_folder(name):
            os.rmdir(name)


def copyItem():
    old_name = input('Введите название элемента: ')
    new_name = input('Введите новое название: ')
    if os.path.exists(old_name):
        if is_file(old_name):
            shutil.copy(old_name, new_name)
        if is_folder(old_name):
            shutil.copytree(old_name, new_name)


def viewDirectory():
    print(os.listdir())


def viewFolders():
    folders = []
    for item in os.listdir():
        if (is_folder(item)):
            folders.append(item)
    print(folders)


def viewFiles():
    files = []
    for item in os.listdir():
        if (is_file(item)):
            files.append(item)
    print(files)


def viewInfoOS():
    print(platform.platform())


def getAuthor():
    print('Лавров Алексей Романович - создатель программы')


def playQuiz():
    pass


def bankBill():
    pass


def changeDirectory():
    path = os.path.join(input('Введите новую рабочую область: '))
    os.chdir(path)


def exit():
    return True
