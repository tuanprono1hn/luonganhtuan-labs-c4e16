x = int(input("x = "))
op = input("operation (+, -, *, /): ")
y = int(input("y = "))
def cong():
    result = x + y
    print(result)
def tru():
    result = x - y
    print(result)
def nhan():
    result = x * y
    print(result)
def chia():
    result = x / y
    print(result)
if op == "+":
    cong()
elif op == "-":
    tru()
elif op == "*":
    nhan()
elif op == "/":
    chia()
