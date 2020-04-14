import os

import re

from sys import argv


def mass_rename(path, find_pattern, repl_pattern):

    with os.scandir(path) as entries:
        for entry in entries:
            if not entry.is_dir():
                os.rename(entry.path, re.sub(find_pattern, repl_pattern, entry.path))
            else:
                mass_rename(entry.path, find_pattern, repl_pattern)


if __name__ == '__main__':
    try:
        mass_rename(argv[1], argv[2], argv[3])
        print('Mass rename complete.')
    except IndexError:
        print(f'{argv=}')
        print("Please use the syntax 'py mass_rename.py <path> <find pattern> <replacement pattern>'")
        quit()
