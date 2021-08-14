user_name = input("Please enter user_name:")
password = input("Please enter password:")

len_of_password = len(password)

# to hide the password
hidden_password = "*" * len_of_password

print(f"Hi {user_name}, your password {hidden_password} is {len_of_password} letters long")
