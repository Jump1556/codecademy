#list comprehension syntax
# range atantion!

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

even_squares = [x*x for x in range (1, 11) if x%2 == 0]
print (even_squares)

cubes_by_four = [c**3 for c in range (1, 11) if c**3%4 == 0]
print (cubes_by_four)


# slicing list list[start:end:stride]
l = [i ** 2 for i in range(1, 11)]
print (l[2:9:2])

to_21 = range(1, 22)
odds = to_21[::2]
middle_third = to_21[7:14]


# reversing a list
my_list = range(1, 11)
backwards = my_list[::-1]


# anonymous function, lambda syntax
my_list = range(16)
print (filter(lambda x: x % 3 == 0, my_list))

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print (filter(lambda x: x=="Python", languages))
