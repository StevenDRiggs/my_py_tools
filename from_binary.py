from sys import argv

message = ''.join(argv[1:])

answer = []

while len(message) >= 8:
    answer.append(chr(int(message[:8], 2)))
    message = message[8:]
if message:
    answer.append(chr(int(message, 2)))

print(''.join(answer))
quit()
