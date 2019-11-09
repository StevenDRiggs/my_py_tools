from random import randint
from sys import argv
from time import sleep

scream = 'AAAAA!!!!!'
count = randint(0, 50) if len(argv) < 2 else int(argv[1])

for _ in range(count):
    front = randint(0, 60)
    back = 70 - front - 10

    print(' ' * front + scream + ' ' * back)

    sleep(0.03)
