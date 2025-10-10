a, znak, b = map(str, input().split())

a = int(a)
b = int(b)

def plus(a, b):
    print(f"{a} + {b} = {a + b}")
    return 0

def minus(a, b):
    print(f"{a} - {b} = {a - b}")
    return 0

def multiplication(a, b):
    print(f"{a} * {b} = {a * b}")
    return 0

def division(a, b):
    print(f"{a} / {b} = {a / b}")
    return 0

if znak == "+":
    plus(a, b)
elif znak == "-":
    minus(a, b)
elif znak == "*":
    multiplication(a, b)
else:
    division(a, b)