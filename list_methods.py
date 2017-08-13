# replacing item in a list
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
zoo_animals[3] = "hippo"
print (zoo_animals)


# append method
suitcase = [] 
suitcase.append("sunglasses")
suitcase.append("shoes")
suitcase.append("shorts")
suitcase.append("bikini")

list_length = len(suitcase)

print ("There are %d items in the suitcase." % (list_length))
print (suitcase)


# slicing method
animals = "catdogfrog"
cat = animals[:3]
dog = animals[3:6]
frog = animals[6:]


#  searching for an item in a list
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")
animals.insert (duck_index, "cobra")

print (animals) 


# for loop
my_list = [1,9,3,8,5,7]

for number in my_list:
  print (2*number)
  
 
# printing in a own line 
animals = ["cat", "ant", "bat"]
animals.sort()
for animal in animals:
  print (animal)
  
  
# for loop + append + sort method
start_list = [5, 3, 1, 2, 4]
square_list = []

for i in start_list:
  square_list.append(i**2)
square_list.sort()

print (square_list)
  
