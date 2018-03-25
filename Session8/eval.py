from random import choice
# x = 3
# op = choice(["+", "-", "*", "/"])
# y = 7
# result = -9999
# def cong():
#     result = x + y
#     print(result)
# def tru():
#     result = x - y
#     print(result)
# def nhan():
#     result = x * y
#     print(result)
# def chia():
#     result = x / y
#     print(result)
# if op == "+":
#     cong()
# elif op == "-":
#     tru()
# elif op == "*":
#     nhan()
# elif op == "/":
#     chia()
op = choice(["+", "-", "*", "/"])
def calc(x , y, op):
    # x = 3
    # op = choice(["+", "-", "*", "/"])
    # y = 7
    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        result = x / y

    return result
# res = calc(3, 7, "+")
# print(res)
# r = calc(1, 2, "-")
# print(r)
# argument, parameter
# calc(4, 8, op)
