
import socket
import string

from sys import argv

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('shell.hackcenter.dbrumley.com', 41627))
s = s.makefile(mode="rw")


# example read welcome
welcome1 = s.readline().strip()
print(welcome1)
cmd = "f"
print(cmd, file=s, flush=True)
flag = str(s.readline().strip().split(' ')[1])
print(flag)
meowmeow = True
candidateFlag  = "picoCTF{"
candidateFlagHEX = "7069636f435446"
searchspace = "}abcdefghijklmnopqrstuvwxyz1234567890_i#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f"
# Example sending encryption
while meowmeow:
 for i in range(0,len(searchspace)):
  print(s.readline().strip())
  print(f"e", file=s, flush=True)
  testFlag = candidateFlagHEX + str(hex(ord(searchspace[i])))[2:4]
  print(testFlag, file=s, flush=True)
  ct = s.readline().strip().split(' ')[5]
  print(ct)
  print(flag[0:len(ct)])
  if all(c1 == c2 for c1,c2 in zip(ct, flag[0:len(ct)])):
   print("HIT")
   candidateFlagHEX = testFlag
   candidateFlag += searchspace[i] 
   print(candidateFlag)
   if(searchspace[i] == '}'):
    meowmeow = False
