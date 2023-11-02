
# Add two numbers
print(1+1)

# These are strings, not numbers
print('1'+'1') # This will print 11, because the "+" operator concatenates strings (instead of adding them)

# Convert the strings back to numbers to add them
print(int('1') + int('1'))

not_a_number = "ABC"

# Uncomment the next two lines to see what happens when you try cast a non-integer string to an integer
# print('Trying to cast "ABC" to an integer...')
# print(int(not_a_number)) # Can't cast letters (or symbols) to numbers, so this throws an error

print('Trying again to cast "ABC" to an integer with a try/except block...')
my_number = None # None is a special keyword in Python that means "no value, yet", like "null" in other languages
try:
    my_number = int(not_a_number)
except ValueError:
    my_number = 0 # If the conversion fails, set the value to 0

print(my_number)

# The modulo operator (%) returns the remainder of a division operation
def is_this_number_even(a_number):
    if a_number % 2 == 0:
        return True
    else:
        return False

print('Is 1 even?')
print(is_this_number_even(1))
print() # Print a blank line
print('Is 2 even?')
print(is_this_number_even(2))
print()
print("Test your own number-- type an integer and press ENTER:")
my_even_test = is_this_number_even(int(input()))

if my_even_test == True:
    print("Your number is even!")
else: # (my_even_test is False)
    print("Your number is odd!")
    
# To improve the function, you can test whether the string was converted to an integer successfully
#   using a try/except block, like we did above.
    