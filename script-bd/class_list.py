import re
from sys import argv


if len(argv) == 1:
    raise SyntaxError("Must list one or more files as arguments.")

for file_str in argv[1:]:
    with open(file_str, 'r') as f:
        script = f.read()

    found = re.findall(r'^\s*class (.+)\((.*)\):$', script, flags=re.MULTILINE)

    mro = []

    with open(file_str + '.txt', 'w') as target:
        for cls in found:
            if cls[1] in mro:
                index = mro.index(cls[1])
                mro = mro[:index+1]
            else:
                mro.append(cls[1])
            target.write('\t'*(len(mro)-1) + cls[0] + '\n')
