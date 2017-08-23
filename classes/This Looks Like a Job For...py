class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Create a new class
class PartTimeEmployee(Employee):
# Create calculate_wage method
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12

  # Add a new method full_time_wage
  def full_time_wage(self, hours):
    return super(PartTimeEmployee,self).calculate_wage(hours)
  
# Create an instance of the PartTimeEmployee class called milton
milton = PartTimeEmployee("Alex")
print (milton.full_time_wage(10))   # print out the result of full_time_wage method
