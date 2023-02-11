import json
import os
import subprocess
from urllib.request import urlretrieve

from util.helper import clear_console

PACKAGE_LOCK_FILE: str = "package-lock.json"
PACKAGE_JSON_FILE: str = "package.json"
INPUT_FOLDER: str = "./input/"
OUTPUT_FOLDER: str = "./output/"


def make_input_output_folders() -> None:
    """
    Creates the input and output folders if they don't exist.
    :return: None
    """

    if not os.path.exists(INPUT_FOLDER):
        os.makedirs(INPUT_FOLDER)
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)


def has_file(folder: str, filename: str) -> bool:
    """
    Checks if the given file exists in the given folder.
    :param folder: The folder to check.
    :param filename: The file to check.
    :return: True if the file exists, False otherwise.
    """

    return os.path.isfile(os.path.join(folder, filename))


def has_package_lock() -> bool:
    """
    Checks if the package_lock.json file exists in the input folder.
    :return: True if the file exists, False otherwise.
    """

    return has_file(INPUT_FOLDER, PACKAGE_LOCK_FILE)


def has_package_json() -> bool:
    """
    Checks if the package.json file exists in the input folder.
    :return: True if the file exists, False otherwise.
    """

    return has_file(INPUT_FOLDER, PACKAGE_JSON_FILE)


def package_lock_parse() -> None:
    """
    Parses the package_lock.json file and downloads all the packages.
    :return: None
    """

    with open(os.path.join(INPUT_FOLDER, PACKAGE_LOCK_FILE)) as package_lock:
        package_lock_data: any = json.load(package_lock)

    dependencies: any = package_lock_data["dependencies"]

    for index, package_name in enumerate(dependencies, 1):
        clear_console()

        print(f"Files downloaded: {index}/{len(dependencies)}")

        package: any = dependencies[package_name]

        resolved: str = package["resolved"]
        file_name: str = resolved.rsplit("/", 1)[-1]

        urlretrieve(resolved, f"{OUTPUT_FOLDER}{file_name}")


def package_json_parse() -> None:
    """
    Parses the package.json file and downloads all the packages.
    :return: None
    """

    subprocess.run(["npm", "install", "--package-lock-only"], cwd=INPUT_FOLDER)


def download_package(package: str) -> None:
    """
    Downloads the given package.
    :param package: The package to download.
    :return: None
    """

    subprocess.run(["npm", "init", "-y"], cwd=INPUT_FOLDER)
    subprocess.run(["npm", "install", package, "--package-lock-only"], cwd=INPUT_FOLDER)

    if has_package_json():
        os.remove(os.path.join(INPUT_FOLDER, PACKAGE_JSON_FILE))
