# ropchain-lab

A lab to explain ropchain exploits

This is part of [CyberSword](https://github.com/nkcyber/cybersword).

This is a docker container that instructs students to overwrite `$eip` with a buffer overflow to perform a ropchain attack.

## Necessary Host System Configuration

The host system will need to be configured to store host files and to disable ASLR
- <https://ddanilov.me/how-to-configure-core-dump-in-docker-container>

```bash
# Disable ASLR
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
# Store core files in /tmp
echo '/tmp/core.%e.%p' | sudo tee /proc/sys/kernel/core_pattern
```

## Docker Context

This lab expects to be in a [`docker-compose.yml` like this](https://github.com/nkcyber/cybersword/blob/7d2498a0dd37627cdfbdad73d0c299dbbd791fdc/docker-compose.yml#L54-L62), from CyberSword.

If you don't want to use that, delete the [lines that expect the setup scripts](https://github.com/nkcyber/ropchain-lab/blob/ffa4ce3d86c7820ec633f06b1a52ab6291fd9d6a/Dockerfile#L32-L38).

## Resources I used

- <https://textbook.cs161.org/memory-safety/x86.html#:~:text=eip%20is%20the%20instruction%20pointer,of%20the%20current%20stack%20frame.>
- <https://stackoverflow.com/questions/69559640/how-can-i-get-a-corefile-for-a-pe-in-python-like-i-can-with-pwntools-for-an-elf>
- <https://tc.gts3.org/cs6265/tut/tut06-01-rop.html>
- <https://github.com/Gallopsled/pwntools-tutorial/blob/master/rop.md>
- <https://docs.pwntools.com/en/stable/rop/rop.html>
- <https://ocw.cs.pub.ro/courses/cns/labs/lab-08>
- <https://ir0nstone.gitbook.io/notes/binexp/stack/pie/pie-bypass>
- <https://docs.pwntools.com/en/stable/elf/corefile.html>

However, I don't beleive I've copied anything directly.

