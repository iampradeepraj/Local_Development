a = [1, 2, 3, 4, 5]
print(a.append(6))
# op of this is null

b = [11, 12, 13, 14, 15]
b.append(16)
print(b)

basket = [1, 2, 3, 4, 5]
new_basket = basket.append(6)
print(new_basket)  # none op

basket_new = [21, 22, 23, 24, 25]
basket_new.append(26)
new_basket_proper = basket_new
print(new_basket_proper)

basket_new = [31, 32, 33, 34, 35]
basket_new.insert(4, 36)
new_basket_proper = basket_new
print(new_basket_proper)

basket_new = [41, 42, 43, 44, 45]
basket_new.extend([100, 101, 102])
new_basket_proper = basket_new
print(new_basket_proper)

new_basket_proper.pop()  # last number is popped
print(new_basket_proper)

new_basket_proper.pop(0)  # first number is popped
print(new_basket_proper)

new_basket_proper.remove(44)
print(new_basket_proper)

# using this list,
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
# 1. Remove the Banana from the list
basket.remove("Banana")
print(basket)
# 2. Remove "Blueberries" from the list.
basket.remove("Blueberries")
print(basket)
# 3. Put "Kiwi" at the end of the list.
basket.append("Kiwi")
print(basket)
# 4. Add "Apples" at the beginning of the list
basket.insert(0, "Apples")
print(basket)
# 5. Count how many apples in the basket
print(basket.count("Apples"))

# using this list,
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)

# sort alphabetically
basket.sort()
print(basket)

# reverse of a list
basket.reverse()
print(basket)

# 6. empty the basket
basket.clear()
print(basket)

# fix this code so that it prints a sorted list of all of our friends (alphabetical)
# friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

# new_friend = ['Stanley']

# print(friends.sort() + new_friend)

friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
friends.sort()
print(friends)
new_friend = ['Stanley']
print(friends + new_friend)
