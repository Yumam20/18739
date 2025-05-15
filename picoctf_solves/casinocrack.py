
import socket
import string

from sys import argv

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('shell.hackcenter.dbrumley.com', 56477))
s = s.makefile(mode="rw")


# example read welcome
welcome1 = s.readline().strip()
welcome1 = s.readline().strip()
welcome1 = s.readline().strip()
welcome1 = s.readline().strip()
welcome1 = s.readline().strip()
welcome1 = s.readline().strip()
welcome1 = s.readline().strip()
welcome1 = s.readline().strip()
welcome1 = s.readline().strip()
checker = 1
cmd = "1"
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
  testFlagHEX = str(candidateFlagHEX + str(ord(searchspace[i])))[2:4]
  print(f"testing {candidateFlag + searchspace[i]}")
  print(testFlagHEX,file=s,flush=True)
  ct = (s.readline().strip().split(' '))
  print(f"ct={ct}")
  print(s.readline().strip())
  if all(c1 == c2 for c1, c2 in zip(ct, flag)):
   print("HIT")
   candidateFlag += searchspace[i]
   print(candidateFlag)
   if(searchspace[i] == '}'):
    meowmeow = False


# Example sending solve.
cmd = f"solve(0)"
print(cmd, file=s, flush=True)
