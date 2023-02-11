import util.files as files


def download():
    if files.has_package_json():
        files.package_json_parse()

    if not files.has_package_lock():
        package = input('Enter a package name: ')
        files.download_package(package)

    if files.has_package_lock():
        files.package_lock_parse()
