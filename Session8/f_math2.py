from random import randint, choice
from eval import calc
x = randint(1, 10)
y = randint(1, 10)
errors = [-1, 0, 1]
err = choice(errors)
op_list = ["+", "-", "*", "/"]
op = choice(op_list)
# if op == "+":
#     z = x + y + err
# if op == "-":
#     z = x - y + err
# if op == "*":
#     z = x * y + err
# if op == "/":
#     z = x / y + err
res = calc(x, y, op)
res += err
print("{0} {1} {2} = {3}".format(x, op, y, res))
i = input("Y/N? ").upper()
if err == 0:
    if i == "Y":
        print("Yay!!!")
    elif i == "N":
        print("You're wrong!")
if err != 0:
    if i == "Y":
        print("You're wrong!")
    elif i == "N":
        print("Yay!!!")
