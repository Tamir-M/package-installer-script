from util.download import download
from util.files import make_input_output_folders
from util.helper import menu_input


def menu():
    make_input_output_folders()
    while True:
        user_choice = menu_input("Welcome to Package Installer",
                                 ["Download", "Upload", "Exit"])

        if user_choice == "Download":
            download()
        elif user_choice == "Upload":
            pass
        elif user_choice == "Exit":
            break

    print(
        "Thank you for using Package Installer.\n"
        "Check out the code repository: https://github.com/Tamir-M/package-installer.\n"
        "Made by: https://github.com/Tamir-M."
    )
