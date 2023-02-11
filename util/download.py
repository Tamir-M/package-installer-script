import util.files as files
from util.helper import confirm


def download():
    if files.has_package_json():
        files.package_json_parse()

    if not files.has_package_lock():
        package = input('Enter a package name: ')
        files.download_package(package)

    if files.has_package_lock():
        files.package_lock_parse()

    if confirm('Do you wish to go to the output folder'):
        files.go_to_output()
