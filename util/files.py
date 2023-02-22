import json
import os
import re
import subprocess
from urllib.request import urlretrieve

from util.helper import clear_console, is_windows_machine, http_request

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

        retrieve_to_output(resolved, file_name)


def package_json_parse():
    subprocess.run(["npm", "i", "--package-lock-only"], cwd=INPUT_FOLDER, shell=True)


def download_npm_package(package):
    subprocess.run(["npm", "init", "-y"], cwd=INPUT_FOLDER, shell=True)
    subprocess.run(["npm", "i", package, "--package-lock-only"], cwd=INPUT_FOLDER, shell=True)
    if has_package_json():
        os.remove(os.path.join(INPUT_FOLDER, PACKAGE_JSON_FILE))


def go_to_output():
    if is_windows_machine():
        subprocess.run(["Explorer", "."], cwd=OUTPUT_FOLDER, shell=True)
    else:
        subprocess.run(["xdg-open", OUTPUT_FOLDER], shell=True)


def retrieve_to_output(url, filename):
    urlretrieve(url, os.path.join(OUTPUT_FOLDER, filename))


def latest_stable_release(releases_list):
    latest = releases_list[0]
    for version in releases_list:
        if not re.search('[a-zA-Z]', version):
            latest = version
            break
    return latest


def download_pip_package(package):
    url = f"https://pypi.org/pypi/{package}/json"

    response_body = http_request(url)
    if not response_body:
        return

    releases = list(reversed(list(response_body["releases"])))

    version = latest_stable_release(releases)

    version_info = response_body["releases"][version][0]
    download_link = version_info["url"]
    download_name = version_info["filename"]

    retrieve_to_output(download_link, download_name)
    print("Download successful!")
