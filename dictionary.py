#dictionaries are mutable

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
menu['Pasta basilika'] = 11.50
menu['Salad Frue'] = 10.00
menu['Beef Alfredo'] = 15.50 

print ("There are " + str(len(menu)) + " items on the menu.")
print (menu)


# adding and delating items from a dictinary
zoo_animals = {
  'Sloth' : 'Rainforest Exhibit',
  'Bengal Tiger' : 'Jungle House',
  'Atlantic Puffin' : 'Arctic Exhibit',
  'Rockhopper Penguin' : 'Arctic Exhibit'
}
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Exhibit'
print (zoo_animals)


inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'],
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
# Adding a key 'pocket'
inventory ['pocket'] = ['seashell', 'strange berry', 'lint']
#sorting a key 'backpack
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory ['gold'] = 550
print (inventory)


#for loop
d = {"foo" : "bar"}
for key in d: 
  print (key, d[key]) 
