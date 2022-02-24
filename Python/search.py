import sys
from random import shuffle, randint

arr = [x for x in range(9999999)]
shuffle(arr)

if randint(0, 999999) in arr:
    print('Found')
    sys.exit(0)

print('Not found')
sys.exit(1)
