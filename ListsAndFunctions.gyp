n = [1, 3, 5]

# On line 3, multiply the second element of the n list by 5
# Overwrite the second element with that result. Append 4. Remove first item
n[1] *= 5
n.append(4)
n.pop(0)

print n

number = 5

# Change the function so the given argument is multiplied by 3 and returned.
def my_function(x):
  return x * 3

# Define a function called add_function that has 2 parameters x and y and adds them together.
print my_function(number)
m = 5
n = 13
def add_function(x,y):
  return x + y

print add_function(m, n)