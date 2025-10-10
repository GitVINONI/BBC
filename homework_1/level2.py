a, znak, b = map(str, input().split())

a = int(a)
b = int(b)

def plus(a : int, b : int) -> int:
    print(f"{a} + {b} = {int(a + b)}")
    return 0

def minus(a : int, b : int) -> int:
    print(f"{a} - {b} = {int(a - b)}")
    return 0

def multiplication(a : int, b : int) -> int:
    print(f"{a} * {b} = {int(a * b)}")
    return 0

def division(a : int, b : int) -> int:
    print(f"{a} / {b} = {float(a / b)}")
    return 0

if znak == "+":
    plus(a, b)
elif znak == "-":
    minus(a, b)
elif znak == "*":
    multiplication(a, b)
else:
    division(a, b)