import os
import platform
import shutil
import quiz
import bank_bill


def __is_file(path):
    return os.path.isfile(path)


def __is_folder(path):
    return os.path.isdir(path)


def create_folder():
    name = input('Введите название папки: ')
    os.mkdir(name)


def remove_folder():
    name = input('Введите название элемента: ')
    if os.path.exists(name):
        os.remove(name) if __is_file(name) else os.rmdir(name)


def copy_item():
    old_name = input('Введите название элемента: ')
    new_name = input('Введите новое название: ')
    if os.path.exists(old_name):
        shutil.copy(old_name, new_name) if __is_file(old_name) else shutil.copytree(old_name, new_name)


def view_directory():
    print(os.listdir())


def view_folders():
    folders = [item for item in os.listdir() if __is_folder(item)]
    print(folders)


def view_files():
    files = [item for item in os.listdir() if __is_file(item)]
    print(files)


def view_info_OS():
    print(platform.platform())


def get_author():
    print('Лавров Алексей Романович - создатель программы')


def play_quiz():
    quiz.start()


def play_bank_bill():
    bank_bill.start()


def change_directory():
    path = os.path.join(input('Введите новую рабочую область: '))
    os.chdir(path)


def exit():
    return True
