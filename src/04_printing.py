"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
percent_op = "x=%i, y=%i, z=%s" % (x, y, z)
print("%",percent_op)
# Use the 'format' string method to print the same thing
format_op = "x= {}, y= {}, z= {}" .format(x, y, z)
print("form_op",format_op)
# Finally, print the same thing using an f-string
f_string = f"x= {x}, y= {y}, z= {z}"
print("F", f_string)