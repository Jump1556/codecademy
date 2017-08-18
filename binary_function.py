# function to check if the fourth bit from the right is on.      
def check_bit4(input):
  check = input & 0b1000
  if check > 0:
    return "on"
  else:
    return "off"
    

# turn on the third bit from the right
a = 0b10111011
mask = 0b100
print (bin(a | mask))
      
      
# use a bitmask and the value a in order to achieve all of the bits in a are flipped
a = 0b11101110
mask = 0b11111111
print (bin(a^mask))
      

# in function flip the nth bit with the ones bit being the first bit, store it in result
def flip_bit (number, n):
  mask = 0b1 << n -1 
  result = number ^ mask
  return bin(result)
