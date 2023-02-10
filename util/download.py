import util.files as files


def download():
    files.make_input_output_folders()

    if files.has_package_json():
        files.package_json_parse()

    if files.has_package_lock():
        files.package_lock_parse()
