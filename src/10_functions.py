# Write a function is_even that will return true if the passed-in number is even.

# Read a number from the keyboard
num = input("Enter a number: ")

# YOUR CODE HERE
def is_even(num):
    # cast to int
    num = int(num)
    # Print out "Even!" if the number is even. Otherwise print "Odd"
    if num % 2 == 0:
        return("Even!")
    else:
        return("Odd")


