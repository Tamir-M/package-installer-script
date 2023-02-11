import os
import json
from urllib.request import urlretrieve
import os
from util.helper import clear_console, is_windows_machine

PACKAGE_LOCK_FILE = 'package-lock.json'
PACKAGE_JSON_FILE = 'package.json'
INPUT_FOLDER = './input/'
OUTPUT_FOLDER = './output/'


def make_input_output_folders():
    if not os.path.exists(INPUT_FOLDER):
        os.makedirs(INPUT_FOLDER)
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)


def has_package_lock():
    return os.path.isfile(INPUT_FOLDER + PACKAGE_LOCK_FILE)


def has_package_json():
    return os.path.isfile(INPUT_FOLDER + PACKAGE_JSON_FILE)


def package_lock_parse():
    # open the package_lock.json.
    package_lock = open(INPUT_FOLDER + PACKAGE_LOCK_FILE)
    # parse the json.
    package_lock_data = json.loads(package_lock.read())
    # get the dependencies from the package_lock.
    if is_windows_machine():
        dependencies = package_lock_data['dependencies']
    else:
        dependencies = package_lock_data['packages']
    # loop through each dependency.
    for index, package_name in enumerate(dependencies):
        clear_console()
        print('Files downloaded: ' + str(index) + '/' + str(len(dependencies)))
        # get the package.
        package = dependencies[package_name]
        # get the resolved (url) and filename.
        resolved = package['resolved']
        file_name = resolved.split('/')[-1]
        # download the file.
        urlretrieve(resolved, OUTPUT_FOLDER + file_name)


def package_json_parse():
    os.system('cd ' + INPUT_FOLDER + ' && npm i --package-lock-only')


def download_package(package):
    os.system('cd ' + INPUT_FOLDER + ' && npm init -y && npm i ' + package + ' --package-lock-only')
    if has_package_json():
        os.remove(INPUT_FOLDER + PACKAGE_JSON_FILE)


def go_to_output():
    os.system('cd ' + OUTPUT_FOLDER + ' && ' + 'Explorer .' if is_windows_machine() else 'xdg-open .')
