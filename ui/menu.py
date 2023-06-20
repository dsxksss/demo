import questionary

def show_test():
    print("执行show_test")


menu_options = {
    "test1":show_test,
    "test2":show_test,
}

def show_menu():
    selected = questionary.select("请选择对应的功能",menu_options).ask()
    menu_options.get(selected)()

