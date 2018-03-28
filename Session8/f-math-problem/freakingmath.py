from random import *
from fmath import calc
def generate_quiz():
    err = choice([-1, 0, 0, 1])
    op = choice(["+", "-", "*", "+", "+", "-", "-"])
    x = randint(1, 10)
    y = randint(1, 10)
    result = calc(x, y, op) + err
    # Hint: Return [x, y, op, result]
    return x, y, op, result

def check_answer(x, y, op, result, user_choice):
    # pass
    # co the dung theo err duoc nhung de bai muon dung result nhi?
    if user_choice == True:
        if result == calc(x, y, op):
            return True
        else:
            return False
    if user_choice == False:
        if result == calc(x, y, op):
            return False
        else:
            return True
    # print(user_choice)
    # return True
