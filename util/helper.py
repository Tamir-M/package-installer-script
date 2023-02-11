import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_input(message, options):
    first_time = True
    user_input = ''
    while not (user_input.isnumeric() and
               0 < int(user_input) < (len(options)) + 1):
        clear_console()
        if not first_time:
            print('incorrect input!')
        else:
            first_time = False

        print(message)

        [print(str(index + 1) + '. ' + option)
         for index, option in enumerate(options)]

        user_input = input("please select one of the above: ")

    clear_console()
    return options[int(user_input) - 1]


def confirm(message):
    user_input = input(message + ' (y): ').lower()
    return user_input == '' or user_input == 'y' or user_input == 'yes'
