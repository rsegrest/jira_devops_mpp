# If you run this file, nothing will happen,
#   because the functions are never called.
# Run "main.py", which calls the functions in this file.

# A function
def say_hello():
    print("Hello World!")
    return

# A function with positional parameters
def say_hello_to(name):
    print("Hello " + name + "!")
    return

def say_hello_to_you(first_name="Rick", last_name="Segrest"):
    # Set a variable that holds your name
    print("Hello " + first_name + " " + last_name + "!")
    return
