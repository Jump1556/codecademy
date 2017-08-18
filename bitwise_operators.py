#shift operations
shift_right = 0b1100
shift_left = 0b1

shift_right = shift_right >> 2 
shift_left = shift_left << 2

print (bin(shift_right))
print (bin(shift_left))


# AND (&) operator
# AND compares two numbers on a bit level and returns multiplication of them
print (bin(0b1110 & 0b101))


# OR (|) operator
# OR compares two numbers and returns the corresponding bits of either number are 1
a = 0b1110
b = 0b101 
print (bin (0b1110 | 0b101 ))


# XOR (^) or exclusive or operator 
result = 0b1011
print (bin(0b1110 ^ 0b101))


# NOT (~) operator
print (~3)  # -4
print (~42) # -43
