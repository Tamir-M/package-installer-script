from util.helper import confirm
from util.files import (
    has_package_lock,
    has_package_json,
    package_json_parse,
    download_package,
    package_lock_parse,
    go_to_output
)


def download():
    if has_package_json():
        package_json_parse()

    if not has_package_lock():
        package = input('Enter a package name: ')
        download_package(package)

    if has_package_lock():
        package_lock_parse()

    if confirm('Do you wish to go to the output folder'):
        go_to_output()
