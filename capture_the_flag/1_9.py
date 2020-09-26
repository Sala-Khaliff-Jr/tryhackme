ord_data = '85 110 112 97 99 107 32 116 104 105 115 32 66 67 68'.split()

op = ""
for num in ord_data:
    op = op + chr(int(num))

print(op)