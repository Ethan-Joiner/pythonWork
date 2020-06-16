"""Create three dictionaries: lloyd, alice, and tyler.
Give each dictionary the keys "name", "homework", "quizzes", and "tests".
Have the “name” key be the name of the student (that is, lloyd‘s name should be "Lloyd") and the other keys should be an empty list (We’ll fill in these lists soon!)"""

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

"""for each student in your students list, print out that student‘s data, as follows:

print the student‘s name
print the student‘s homework
print the student‘s quizzes
print the student‘s tests"""

for student in students:
  print student["name"]
  print student["homework"]
  print student["quizzes"]
  print student["tests"]

# Write a function average that takes a list of numbers and returns the average.
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)  

# Write a function called get_average that takes a student dictionary (like lloyd, alice, or tyler) as input and returns his/her weighted average.
def get_average(student):
  homework = average(student["homework"]) 
  quizzes = average(student["quizzes"]) 
  tests = average(student["tests"])   
  return homework * .1 + quizzes * .3 + tests * .6   