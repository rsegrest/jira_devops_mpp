websters = {
    "Aardvark" : "(n): A weird animal with a giant tongue that licks up ants",
    "Apple" : "(n): (1) A fruit; (2) A company that manufactures highly addictive devices",
}
print("Print the entire dictionary:")
print(websters)

print()
print("Print the definition of Apple:")
print(websters["Apple"])

print()
print("Adding a new entry to the dictionary...")
websters["Blackberry"] = "(n): (1) A sub-par fruit; (2) An extinct phone"

print("Print the keys in the dictionary:")
print(websters.keys())
print()
print("How many entries are there in the dictionary?:")
print(len(websters))