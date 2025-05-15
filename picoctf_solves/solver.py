import socket
import string
from sys import argv
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('shell.hackcenter.dbrumley.com',56473))
s = s.makefile(mode="rw")
welcome1 = s.readline()
print(welcome1)
print(s.readline())
for k in range(0, 0xff):
    i = (k<<8) | 0x5e
    cmd = "1"
    print(cmd, file=s, flush=True)
    s.readline()
    print(f"{i:024x}",file=s, flush=True)
    print(f"{i:024x}")
    s.readline()
    print("2", file=s, flush=True)
    s.readline()
    print("Come on man.", file=s, flush=True)
    ct = s.readline().strip().split('Output: ')[1] 
    print(ct)
    if(ct == '"DONALD TRUMP"'):
         print("HIT")
