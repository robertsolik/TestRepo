# Test01
import datetime
from random import randint
#print("Hello World")
#list = ['hello','world','my','name','is','Robert']

# for word in list:
#     print(word.title())
# dob_input = input('Enter your date of birth (yyyy-mm-dd): ')
# year, month, day = map(int, dob_input.split('-'))
# dob = datetime.date(year, month, day)
# today = datetime.date.today()
# age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
# print(f"You are {age} years old.")
choices = ['rock','paper','scissors','quit']
abbrs = ['r','p','s','q']
p_score = 0
c_score = 0

while True:
    print(f"SCORE:  PLAYER {p_score}  COMPUTER {c_score} \n")
    print(f"{choices[0]} <{abbrs[0]}>, {choices[1]} <{abbrs[1]}>, {choices[2]} <{abbrs[2]}>, or to quit <{abbrs[3]}>")
    player = abbrs.index(input("Choose one: "))
    if player == 3:
        print("Goodbye")
        break
    # print(f"{player}")
    computer = randint(0,2)
    # print(f"{computer}")

    if (player + 1) == 3:
        check = 0
    else:
        check = player + 1

    if player == computer:
        print(f"{choices[player]} vs {choices[computer]} \n DRAW \n")
    elif choices[computer] == choices[check]:
        c_score = c_score + 1
        print(f"{choices[player]} vs {choices[computer]} \n {choices[computer].upper()} WINS \n")
    else:
        p_score = p_score + 1
        print(f"{choices[player]} vs {choices[computer]} \n {choices[player].upper()} WINS \n")
