from menu import menu
from methods import *


def init():
    menu_switch()


def menu_switch():
    while True:
        for menu_item in menu.values():
            print(f"{menu_item['id']}. {menu_item['title']}")
        choose = int(input('Выберите пункт меню: '))
        if choose in menu:
            is_exit = eval(menu[choose]['method'])()
            if is_exit:
                break


if __name__ == '__main__':
    init()
