import util.download as download
from util.helper import menu_input


def menu():
    while True:
        user_choice = menu_input('Welcome to Package Installer',
                                 ['Download', 'Upload', 'Exit'])

        if user_choice is 'Download':
            download.download()

        if user_choice is 'Upload':
            pass

        if user_choice is 'Exit':
            exit(0)
