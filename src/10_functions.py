# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


# def is_even(i):
#     if int(i) % 2 == 0:
#         return True


# Read a number from the keyboard
# num = input("Enter a number: ")
# num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
# if is_even(num) == True:
#     print("Even!")
# else:
#     print("Odd")
# YOUR CODE HERE
def is_even():
    num = input("Enter a number: ")
    num = int(num)
    if num % 2 == 0:
        print("EVEN!")
    else:
        print("ODD!")


is_even()
