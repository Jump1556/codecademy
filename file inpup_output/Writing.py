my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

for i in my_list:                # Iterate over my_list to get each value.
  my_file.write(str(i) + "\n")   # add a newline 
my_file.close()                  # important to close file!
