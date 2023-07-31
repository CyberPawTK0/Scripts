#!/usr/bin/env python3

with open("shellcode.txt", "r") as f:
       hex_string = f.read().replace("0x","").replace("byte[] rsrc = new byte[464] {", "").replace("};","").replace(",","")
       
       hex_encode = hex_string.encode()  


print(hex_string)

print(hex_encode) 

with open("out.bin", "wb") as out:
        out.write(hex_encode)
        