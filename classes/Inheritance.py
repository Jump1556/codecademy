#Create a class, Triangle
class Triangle(object):
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
 
# Create method with if, else statement 
  number_of_sides = 3
  def check_angles(self):
    if (self.angle1+self.angle2+self.angle3) == 180:
      return True
    else:
      return False

# Create variable my_triangle and set it to a instance of your Triangle clas.
my_triangle = Triangle(90,30,60)
print (my_triangle.number_of_sides)
print (my_triangle.check_angles())
    
# Create a class named Equilateral that inherits from Triangle    
class Equilateral(Triangle):
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle
    
  
