#06-Aug-2021
# <variable name> = <value>
a = 10
b = 10
c = a + b
print(c)

a = b = c = d = e = 20

print(e)

f, h, k = 10, 20, 40

print(f)
print(h)
print(k)

this_is_my_first_course = 20
print(this_is_my_first_course)

CONSTANT = 40
print(CONSTANT)

c_123 = 10

test = 20
TEST = 30

print(test)
print(TEST)

a = 10
print(type(a))
a = 10.5
print(type(a))
a_s = "10"
print(type(a_s))
a_ss = '10'
print(type(a_ss))
a_l = [10]
print(type(a_l))

# Arithmetic operators
a = 10  # int
b = 20
c = 10.5  # float
x = a + c
print(type(x))
print(type(a + b))

print(a + b)
print(a - b)
print(a * b)
print(a * c)
print(a / b)
print(a / c)

value = (((12 * 2) + 1) * 3) + 25
print(value)

x = 5
y = 2

z = x ** y
print(z)

aString = 'Prudhvi Akella  what ever it is'
abString = "Prudhvi Akella  what ever it is"

print(aString)

# astring[lowerboundary:upperbounder]
'''
    lowerboundary
    upperboundary
    astring[:10] -> upto 10th index(10th index is excluded)
        lowerboundary = 0
        upperboundary = 10
    astring[4:] 
        lowerboundary = 4
        upperboundary = len(astring)-1 or nth index
    aString[4:11]
        lowerboundary = 4
        upperboundary = 11 -> upto 11th index
    aString[-5:-1] -> 
        lowerboundary = -5
        upperboundary = -1 upto or exclude -1th location
    aString[-5:] -> Last 5 characters as a string              
'''
print(aString[4:10]+aString[15:20]) #string concatination
print(abString[-5:-1]) #from -5th index to until last character
print(abString[-5:]) #from -5th index to last character
print(abString[0:10:2])
print(abString[0:10:3])

"""
aString[lowerboundary:upperboundary:step]
abString[0:11:2]
0 -> P
0 + 2 = 2 -> u
2 + 2 = 4 -> h
4 + 2 = 6 -> i
6 + 2 = 8 -> A
8 + 2 = 10 -> e
abString[0:10:3]
0->P
0+3 = 3 ->d
3+3 = 6 ->i
6+3 = 9 ->k
"""

# Reverse a string
# Prudhvi = input string
# 0123456 = index
# len(Prudhvi) = 7
# 7 - 1 = 6 = i
# 6 - 1 = 5 = v
# 5 - 1 = 4 = h
# 4 - 1 = 3 = d
#...
# 1 - 1 = 0 = p

abString = "Prudhvi Akella  what ever it is"
print(abString[20:0:-1])

aString1 = 'Prudhvi'
aString2 = ' Akella'
aString3 = aString1 + aString2
print(aString3)

# str is a built in function which converts an object of any type to string in below case we are converting int to string
print("Prudhvi" + str(1))
print("Prudhvi" + str(1.5))

print(" prudhvi " * 5)

# Membership operator(in)
aString1 = 'Prudhvi Akella'
aString2 = "Prudhvi"
a_string_in = aString2 in aString1
print(a_string_in)
print(type(a_string_in))
# in operator will always do exact match
print(aString1 in aString2)
# "not in" negate of "in" output
print(aString1 not in aString2)