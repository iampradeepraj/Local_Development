print("Hi Pradeep")

# Type conversion
print(type(str(100)))

# Escape Sequence
weather = "it\'s \"kinda\" sunny"

print(weather)

weather = "\t it\'s \"kinda\" sunny. \n Lets go tomorrow"

print(weather)

name = input("Please provide name: ")

age = input("Please provide age: ")

print("Hi " + name + " your age is " + age)

print("Hi {}. your {} years old".format("tyson", 7))

print("Hi {0}. your {1} years old".format("vijaya", 45))

print("Hi {name}. your {age} years old".format(name="tyson", age=7))

print("Hi {0}. your {age} years old".format("Ramesh", age=56))

print(f"Hi {name}. your {age} years old")

# Guess the output of each print statement before you click RUN!
python = 'I am PYTHON'

print(python[1:4])
print(python[1:])
print(python[:])
print(python[1:100])
print(python[-1])
print(python[-4])
print(python[:-3])
print(python[-3:])
print(python[::-1])
