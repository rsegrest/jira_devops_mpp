my_string = "All work and no play makes Jack a dull boy"
print(my_string)

# Because a string is a sequence of characters (like a list or an array), you can access individual characters using an index.
print(my_string[0]) # 0 is the index of the first character -- prints "A"
print(my_string[1]) # 1 is the index of the second character -- prints "l"

print(my_string[0:3]) # prints "All"
print(my_string[4:8]) # prints "work"

print(my_string.split(" ")) # Remove the spaces and create an array from the words in the sentence

print("I can't control the volume of my voice!".upper()) # Convert to uppercase
print("PLEASE USE YOUR LIBRARY VOICE.".lower()) # Convert to lowercase

# Print the same string 100 times
for i in range(0, 100):
    print(my_string)