# Test01
import datetime
#print("Hello World")
#list = ['hello','world','my','name','is','Robert']

# for word in list:
#     print(word.title())
dob_input = input('Enter your date of birth (yyyy-mm-dd): ')
year, month, day = map(int, dob_input.split('-'))
dob = datetime.date(year, month, day)
today = datetime.date.today()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
print(f"You are {age} years old.")
