print(2 < 3)
print(2 > 3)

small = 1
big = 100

# Is small less than big?
if small < big:
    # yes, this line will execute. "else" will be skipped.
    print ("small is less than big") 
else:
    print ("small is not less than big")

# Is small greater than big?
if small > big:
    print ("small is greater than big")
else:
    # no, this line will execute. "if" will be skipped.
    print ("small is not greater than big")
    
# "==" is the equivalency operator, and returns a boolean.
# It is common to type "=" when you mean "=="
# "=" is the assignment operator, so it will always return true.
# Sometimes the interpreter will catch this and issue a warning, but not always.

# Is small equal to big?
if small == big:
    print ("small is equal to big")
else:
    print ("small is not equal to big")
