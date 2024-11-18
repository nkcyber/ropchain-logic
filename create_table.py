#!/usr/bin/env python3
from pwn import *
from prettytable import PrettyTable

def get_corefile_location(executable_name: str, pid: int) -> os.PathLike[str]:
    with open("/proc/sys/kernel/core_pattern") as f:
        core_pattern = f.read()
        assert "%e" in core_pattern and "%p" in core_pattern
        return core_pattern.replace("%e", executable_name).replace("%p", str(pid)).strip()

BUFFER_SIZE = 64
# overflow the buffer
payload = cyclic(BUFFER_SIZE * 2)

# Start the vulnerable binary
with process(['./example-crash', payload]) as p:
    p.wait()  # Wait for the program to crash

# Examine the crash to find the offset
core = Coredump(get_corefile_location("example-crash", p.pid))

table = PrettyTable()
table.align = 'l' # algin left
table.field_names = ["register", "hex value", "decimal value", "cyclic_find"]

sorted_registers = dict(sorted(core.registers.items(), key=lambda item: -item[1]))
# construct table of values
for k,v in sorted_registers.items():
    table.add_row([k,hex(v), v, cyclic_find(v)])

print(table)

