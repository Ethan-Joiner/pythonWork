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

"""Write a function that counts how many times the string "fizz" appears in a list.

Write a function called fizz_count that takes a list x as input.
Create a variable count to hold the ongoing count. Initialize it to zero.
for each item in x:, if that item is equal to the string "fizz" then increment the count variable.
After the loop, please return the count variable."""

def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count += 1

  return count   

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

"""Loop through each key in prices.
For each key, print out the key along with its price and stock information."""

for key in prices:
  print key
  print "price: %s" % prices[key]
  print "stock: %s" % stock[key]

"""Let’s determine how much money you would make if you sold all of your food.

Create a variable called total and set it to zero.
Loop through the prices dictionary.
For each key in prices, multiply the number in prices by the number in stock. Print that value into the console and then add it to total.
Finally, outside your loop, print total."""
total = 0
for key in prices:
  total += prices[key] * stock[key]
print total

# First, make a list called groceries with the values "banana","orange", and "apple".
groceries = ["banana", "orange", "apple"]