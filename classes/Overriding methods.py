# Define a new class named "Car"
class Car (object):
   condition = "new"     # member variables
   def __init__(self, model, color, mpg):
    # in order to assign a member variable,use dot notation self.new_variable=new_variable
    self.model = model
    self.color = color
    self.mpg = mpg
   # add a method named display_car 
   def display_car(self):
    return "This is a " + self.color + " " + self.model + " " + "with " + str(self.mpg) + " " + "MPG" + "."
   # # add a method named drive_car
   def drive_car(self):
    self.condition = "used"

my_car = Car("DeLorean", "silver", 88)
#an object(instance of class)
model = "DeLorean"
color = "silver"
mpg = 88
print (my_car.display_car())

# Create a class ElectricCar that inherits from Car
class ElectricCar (Car):
  def __init__ (self, model, color, mpg, battery_type):     # __init__() method
    super(ElectricCar, self).__init__(model, color, mpg)
    self.battery_type = battery_type
    
  def drive_car(self):
    self.condition = "like new"
      
my_car = ElectricCar("Volvo", "red", 25,"molten salt")

print (my_car.condition)
my_car.drive_car()
print (my_car.condition)
print (my_car.display_car())

