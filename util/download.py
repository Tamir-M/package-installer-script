from util.files import (
    download_package,
    go_to_output,
    has_package_json,
    has_package_lock,
    make_input_output_folders,
    package_json_parse,
    package_lock_parse,
)
from util.helper import confirm


def download():
    make_input_output_folders()

    if has_package_json():
        package_json_parse()

    if not has_package_lock():
        download_package(input("Enter a package name: "))

    if has_package_lock():
        package_lock_parse()

    if confirm("Do you wish to go to the output folder"):
        go_to_output()

    if confirm("Do you wish to go to the output folder"):
        go_to_output()
