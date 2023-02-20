import json
import os
import subprocess
from urllib.request import urlretrieve

from util.helper import clear_console, is_windows_machine

PACKAGE_LOCK_FILE = "package-lock.json"
PACKAGE_JSON_FILE = "package.json"
INPUT_FOLDER = "./input/"
OUTPUT_FOLDER = "./output/"


def make_input_output_folders():
    if not os.path.exists(INPUT_FOLDER):
        os.makedirs(INPUT_FOLDER)
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)


def has_file(folder, filename):
    return os.path.isfile(os.path.join(folder, filename))


def has_package_lock():
    return has_file(INPUT_FOLDER, PACKAGE_LOCK_FILE)


def has_package_json():
    return has_file(INPUT_FOLDER, PACKAGE_JSON_FILE)


def package_lock_parse():
    # open the package_lock.json.
    with open(os.path.join(INPUT_FOLDER, PACKAGE_LOCK_FILE)) as package_lock:
        package_lock_data = json.load(package_lock)

    if is_windows_machine():
        dependencies = package_lock_data["dependencies"]
    else:
        dependencies = package_lock_data["packages"]

    for index, package_name in enumerate(dependencies):
        if package_name == "":
            continue

        clear_console()

        print(f"Files downloaded: {str(index)}/{str(len(dependencies))}")

        package = dependencies[package_name]

        resolved = package["resolved"]
        file_name = resolved.split("/")[-1]

        urlretrieve(resolved, os.path.join(OUTPUT_FOLDER, file_name))


def package_json_parse():
    subprocess.run(["npm", "i", "--package-lock-only"], cwd=INPUT_FOLDER, shell=True)


def download_package(package):
    subprocess.run(["npm", "init", "-y"], cwd=INPUT_FOLDER, shell=True)
    subprocess.run(["npm", "i", package, "--package-lock-only"], cwd=INPUT_FOLDER, shell=True)
    if has_package_json():
        os.remove(os.path.join(INPUT_FOLDER, PACKAGE_JSON_FILE))


def go_to_output():
    if is_windows_machine():
        subprocess.run(["Explorer", "."], cwd=OUTPUT_FOLDER, shell=True)
    else:
        subprocess.run(["xdg-open", OUTPUT_FOLDER], shell=True)
