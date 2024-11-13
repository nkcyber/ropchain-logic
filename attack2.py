from pwn import *


# ./example "$(python3 -c "print('A' * 77)")" 
# -> segfault at 0 ip 0000000000000000 
# ./example "$(python3 -c "print('A' * 78)")" 
# -> segfault at ff00413d ip 0000000056556243
# ./example "$(python3 -c "print('A' * 78)")" 
# -> segfault at 41413d

