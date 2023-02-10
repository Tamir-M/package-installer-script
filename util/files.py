import os
import json
from urllib.request import urlretrieve
import os

PACKAGE_LOCK_FILE = 'package-lock.json'
INPUT_FOLDER = './input/'
OUTPUT_FOLDER = './output/'


def make_input_output_folders():
    if not os.path.exists(INPUT_FOLDER):
        os.makedirs(INPUT_FOLDER)
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)


def has_package_lock():
    return os.path.isfile(INPUT_FOLDER + PACKAGE_LOCK_FILE)


def package_lock_parse():
    # open the package_lock.json.
    package_lock = open(INPUT_FOLDER + PACKAGE_LOCK_FILE)
    # parse the json.
    package_lock_data = json.loads(package_lock.read())
    # get the dependencies from the package_lock.
    dependencies = package_lock_data['dependencies']
    # loop through each dependency.
    for package_name in dependencies:
        # get the package.
        package = dependencies[package_name]
        # get the resolved (url) and filename.
        resolved = package['resolved']
        file_name = resolved.split('/')[-1]
        # download the file.
        urlretrieve(resolved, OUTPUT_FOLDER + file_name)
