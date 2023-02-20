import os


def is_windows_machine():
    return os.name == "nt"


def clear_console():
    os.system("cls" if is_windows_machine() else "clear")


def menu_input(message, options):
    first_time = True
    user_input = ""
    while not (user_input.isdigit() and
               1 <= int(user_input) <= (len(options))):
        clear_console()
        if not first_time:
            print("incorrect input!")
        else:
            first_time = False

        print(message)

        [print(f"{str(index + 1)}. {option}")
         for index, option in enumerate(options)]

        user_input = input("Please select one of the above: ")

    clear_console()
    return options[int(user_input) - 1]


def confirm(message):
    user_input = input(f"{message} (y): ").lower()
    return user_input == "" or user_input == "y" or user_input == "yes"
