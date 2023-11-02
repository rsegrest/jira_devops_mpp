from _03_hellomodule import say_hello, say_hello_to, say_hello_to_you

# The following only runs if the file is run directly,
# If it is imported as a module, it will be ignored.
if __name__ == "__main__":
    say_hello()
    say_hello_to("Batman")
    say_hello_to_you() # uses default values
    say_hello_to_you("Bruce", "Wayne")