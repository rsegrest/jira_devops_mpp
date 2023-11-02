my_list_of_numbers = [1, 2, 3, 4, 5]
print(my_list_of_numbers)

my_menu = ["Pizza", "Burrito", "Sushi"]
print(my_menu)

my_menu.append("Steamed Hams")
print(my_menu)

seasonal_menu = ["Candy Canes", "Eggnog", "Soylent Green"]

# Add the seasonal menu to the regular menu
my_menu.extend(seasonal_menu)
print(my_menu)
print()
print("The length of my menu is now:")
print(len(my_menu))

# Remove Soylent Green, because it's people!
my_menu.remove("Soylent Green")
print(my_menu)

# We lost our liquor license, so we can't serve eggnog anymore
my_menu.pop() # "pop()" removes the last item
print(my_menu)

# Wilford Brimley is a regular customer, and he has diabeetus.
#   We have to remove the Candy Canes from the menu so he won't be tempted to eat them.
del my_menu[-1] # del deletes an item. "-1" references the last item in the list
print(my_menu)

# The FDA said we could serve liquor, candy, and people--
#   as long as we alphabetize the menu.
# Re-add the seasonal menu, and sort the list alphabetically 
fda_approved_menu = my_menu + seasonal_menu
fda_approved_menu.sort()
print(fda_approved_menu)