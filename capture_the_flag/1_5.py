hex_data = '68 65 78 61 64 65 63 69 6d 61 6c 20 6f 72 20 62 61 73 65 31 36 3f'.split(' ')

op = ""
for hex in hex_data:
    op = op + chr(int(hex,16))

print(op)