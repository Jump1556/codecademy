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
  
  
# line 29 print items such a tuples
# line 30 print keys
# line 31 print values
# line 34 print keys and values each in a line
my_dict = {
  'Mom' : 64,
  'papa' : 113,
  'weight' : True
}
print (my_dict.items())
print (my_dict.keys())
print (my_dict.values())

for key in my_dict:
  print (key, my_dict[key])
  
  
#  total value of inventory
total = 0
for key in prices:
  i = prices[key]*stock[key]
  total += i
  print (i)
print (total)

