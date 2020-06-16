# Use a for loop to print out all of the elements in the list names.
names = ["Adam","Alex","Mariah","Martine","Columbus"]

for name in names:
  print name

# Use a for loop to go through the webster dictionary and print out all of the definitions.
  webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

for key in webster:
  print webster[key]

"""Like step 2 above, loop through each item in the list called a.

Like step 3 above, if the number is even, print it out. You can test if the item % 2 == 0 to help you out."""
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for number in a:
  if number % 2 == 0:
    print number