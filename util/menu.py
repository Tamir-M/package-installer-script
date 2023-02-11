from util.download import download
from util.helper import menu_input


def menu() -> None:
    """
    Package Installer main menu.
    :return: None
    """

    open_message: str = "Welcome to Package Installer 📦."
    options: list[str] = ["Download", "Upload", "Exit"]

    while True:
        user_choice: str = menu_input(open_message, options)

        if user_choice == "Download":
            download()
        elif user_choice == "Upload":
            # TODO: Add code for uploading functionality
            pass
        elif user_choice == "Exit":
            break

    print(
        "Thank you for using Package Installer 📦.\n"
        "Check out the code repository 👉 https://github.com/Tamir-M/package-installer.\n"
        "Made by https://github.com/Tamir-M."
    )
