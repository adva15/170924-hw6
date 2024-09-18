import random

asterisk = int(input('enter number asterisk:'))

#asterisk= asterisk * 2 -1
for i in range(asterisk+1):
    print('  ' * ( asterisk - i), end='')
    print(' * ' * ( i * 2 - 1))

