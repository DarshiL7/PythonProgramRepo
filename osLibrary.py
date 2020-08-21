import os


def current_directory():
    cwd = os.getcwd()
    print(cwd)


def absolute_path(filename):
    file = os.path.abspath(filename)
    file1 = os.path.realpath(filename)
    file2 = os.path.relpath(filename)

    print(file)
    print(file1)
    print(file2)
