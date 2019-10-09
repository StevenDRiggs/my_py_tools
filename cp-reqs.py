import os

from sys import argv

path = argv[1]
print('path:', path)

try:
    with open(os.path.join(path, 'home-requirements.txt')) as f:
        home = f.read()
    with open(os.path.join(path, 'wk-requirements.txt')) as g:
        work = g.read()

    if home == work:
        print('The files match.')
    else:
        print('The files do not match.')
        
        home_list = home.split(sep='\n')
        work_list = work.split(sep='\n')

        if len(home_list) > len(work_list):
            filename = 'wk-requirements.txt'
        else:
            filename = 'home-requirements.txt'

        non_union = (set(home_list) | set(work_list)) - (set(home_list) & set(work_list))
        non_union_printout = '\n'.join(non_union)

        print(f'{filename} is missing:\n{non_union_printout}')

except FileNotFoundError as e:
    print('This folder is missing one or more of the following:\nhome-requirements.txt\nwk-requirements.txt')
