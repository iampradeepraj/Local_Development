# Scroll down to see the answers!
# 1 Create a user profile for your new game. \
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user_profile = {
    'age': 27,
    'user_name': "Pradeep",
    'weapon': "M416",
    'is_active': True,
    'clan': "SJ WARRIORS"
}
print(user_profile)
# 2 iterate and print all the keys in the above user.
print(user_profile.keys())
# 3 Add a new weapon to your user
user_profile.update({'weapon': "AKM"})
print(user_profile)
# 4 Add a new key to include 'is_banned'. Set it to false
user_profile.update({'is_banned': False})
print(user_profile)
# 5 Ban the user by setting the previous key to True
user_profile.update({'is_banned': True})
print(user_profile)
