import questionary
from ui.clear_console import clear
from service.add import add_user

menu_options = {
    "添加用户":add_user,
}

def show_menu():
    selected = questionary.select("请选择对应的功能",menu_options).ask()
    clear()
    menu_options.get(selected)()

