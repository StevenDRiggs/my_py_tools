from sys import argv

message = argv[1]

if len(argv) == 3:
    count = int(argv[2])
else:
    count = 1

bin_l = []
message_l = list(message)

for char in message_l:
    bin_l.append('{:08b}'.format(ord(char)))

print(''.join(bin_l) * count)
quit()
