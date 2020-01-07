from random import randint
from sys import argv
from time import sleep

arg1, arg2 = None, None
scream = 'AAAAA!!!!!'

try:
    arg1 = argv[1]
    arg2 = argv[2]
except IndexError:
    pass

if arg1 and arg1.isdigit():
    count = int(arg1)
    if arg2:
        scream = arg2
elif arg2 and arg2.isdigit():
    count = int(arg2)
    scream = arg1
else:
    count = randint(0, 50)
    if arg1:
        scream = arg1

for _ in range(count):
    front = randint(0, 70 - len(scream))
    back = 70 - front - len(scream)
    if front < 0:
        front = 0
    if back < 0:
        back = 0

    print(' ' * front + scream + ' ' * back)

    sleep(0.03)
