# importing date class from datetime module
from datetime import date

birth_year = input("what year were you born:")

# creating the date object of today's date
todays_date = date.today()
# fetching the current year, month and day of today
current_year = todays_date.year

age = current_year - int(birth_year)
print(f"your age is {age}")
