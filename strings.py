'''
Created by Samuel Mondier
2/25/18

Just a simple script to make a bunch of quoted strings
for stress testing my heapsort program
'''
import sys
import string
import random

if __name__ == '__main__':
    fp = open(sys.argv[1], 'w+')

    if len(sys.argv) > 2:
        try:
            strNum = int(sys.argv[2])
        except ValueError:
            print('Invalid number: {}'.format(sys.argv[2]))
    else:
        strNum = 1000000

    for _ in range(strNum):
        fp.write('"')
        fp.write(
            ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1, 10)))
        )
        fp.write('"')
        fp.write("\n")
