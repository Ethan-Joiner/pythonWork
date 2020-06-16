# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

"""Delete the 'Sloth' and 'Bengal Tiger' items from zoo_animals using del.

Set the value associated with 'Rockhopper Penguin' to anything other than 'Arctic Exhibit'."""
del zoo_animals["Sloth"]
del zoo_animals["Bengal Tiger"]
zoo_animals["Rockhopper Penguin"] = "Anything other than 'Arctic Exhibit'"

# Remove 'dagger' from the list of items stored in the backpack variable.
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove("dagger")


"""Add a key to inventory called 'pocket'

Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'

.sort() the items in the list stored under the 'backpack' key

Then .remove('dagger') from the list of items stored under the 'backpack' key

Add 50 to the number stored under the 'gold' key"""

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory["pocket"] = ["seashell", "strange berry", "lint"]
inventory["backpack"].sort()
inventory["backpack"].remove("dagger")
inventory["gold"] += 50