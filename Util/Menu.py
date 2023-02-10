def correct_input(message, options):
    first_time = True
    user_input = ''
    while not (user_input.isnumeric() and
               0 < int(user_input) < (len(options)) + 1):

        if not first_time:
            print('incorrect input!')
        else:
            first_time = False

        print(message)

        [print(str(index + 1) + '. ' + option)
         for index, option in enumerate(options)]

        user_input = input("please select one of the above:")

    return options[int(user_input) - 1]


def menu():
    while True:
        result = correct_input('Welcome to Package Installer',
                               ['Download', 'Upload', 'Exit'])
        print(result)
