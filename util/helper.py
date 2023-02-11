import os


def is_windows_machine():
    return os.name == "nt"


def clear_console() -> None:
    """
    Clears the console.
    :return: None
    """

    os.system("cls" if is_windows_machine() else "clear")


def menu_input(message, options) -> str:
    """
    Displays a menu with the given message and options.
    :param message: The message to display.
    :param options: The options to display.
    :return: The selected option.
    """

    user_input: str = ""

    while not (user_input.isdigit() and 1 <= int(user_input) <= len(options)):
        clear_console()

        print(message)

        options_text: str = "\n".join(
            [f"{index + 1}. {option}" for index, option in enumerate(options)]
        )

        user_input: str = input(f"{options_text}\n" f"Please select one of the above: ")

    return options[int(user_input) - 1]


def confirm(message):
    user_input = input(message + " (y): ").lower()
    return user_input == "" or user_input == "y" or user_input == "yes"
