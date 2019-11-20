import sys

program = open(sys.argv[1], 'rb').read()
out = open(sys.argv[2], 'wb')

for char in program:
    char = int(char)
    for _ in range(8):
        if char % 2 == 0:
            write = b' '
            print(' ', end='')
        else:
            write = b'\n'
            print('\\n', end='')
        out.write(write)
        char //= 2

out.close()
print()