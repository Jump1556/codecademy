class Animal(object):
  is_alive = True
  health = "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
	  print self.name
	  print self.age
hippo = Animal("Ivo",2)
sloth = Animal("Iva",3)
ocelot = Animal("Ivi",1)
hippo.description()
print (hippo.health)
print (sloth.health)
print (ocelot.health)
