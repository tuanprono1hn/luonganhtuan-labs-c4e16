from random import randint, choice
x = randint(0, 20)
y = randint(0, 20)
errors = [-1, 0, 1]
err = choice(errors)
# print(err)
z = x + y + err
print("{0} + {1} = {2}".format(x,y,z))
i = input("Y/N? ").upper()
if err == 0:
    if i == "Y":
        print("Yay!!!")
    elif i == "N":
        print("You Noob!")
if err != 0:
    if i == "Y":
        print("You Noob!")
    elif i == "N":
        print("Yay!!!")
