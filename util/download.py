import util.files as files


def download():
    if files.has_package_lock():
        files.package_lock_parse()
    else:
        print('No package.lock file')
        input('To continue press any key')
