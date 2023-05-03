# Variable anme assignment
# variable_name = value or expression

# = is used as assignment
# == Equality operator or congruency

# song = 2 + 1
# song = 3.0
song = "Geese"
print(song)
"""
print()
type()
abs()
"""

mystery_value = type ("Hello World")
print(mystery_value)
print(mystery_value)

x = input("What is your name? ")
y = input("What is your age? ")

print("Hello " + x)
print("You are", y, "years old")

first_age = input("What is the age of person 1? ")
second_age = input("What is the age of person 2? ")

difference = int(first_age) - int(second_age)

print("Person 1 is", difference ,  "years older than person 2")

"""
int()
str()
bool()
float()
"""

student_count = str("8675307")
print(student_count)

# Step 13
introduction_question = input("What is your name?")
print(introduction_question)
pi = int(3.14159)
print(pi)
print(bool(0 == 4-3))
print(bool(3/3 == 1))
print(float(10))

# Step 18
studs_in_class1 = 27
studs_in_class2 = 31
studs_in_class3 = 13
sum_of_students = studs_in_class1 + studs_in_class2 + studs_in_class3

average_student_count = int(sum_of_students / 3)
print(average_student_count)

# Step 19
print(type(input("type in a name: ")))
print(type(input("type in a number: ")))
print(type(input("Enter anything: ")))

#Conditionals example
x = int(input("pick a number:"))
if (x < 10):
  print("too low")
else:
  print("too high")

# Step 21
guess = input("Pick a number: ")

if (guess < 10):
  print("too low")
elif (guess == 10):
  print("Exactly 10!")
else:
  print("too high")

