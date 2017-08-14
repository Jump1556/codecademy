# print key and value of dictionary 
prices = { 
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}
stock = {
  "banana": 6,
   "apple": 0,
  "orange": 32,
  "pear": 15
}
for key in prices:
    print (key)
    print ("Prices: %s" % prices[key])
    print ("Stock: %s" % stock[key])
  
#  total value of inventory
total = 0
for key in prices:
  i = prices[key]*stock[key]
  total += i
  print (i)
print (total)

