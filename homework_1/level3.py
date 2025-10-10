a, znak, b = map(str, input().split())

a = int(a)
b = int(b)

def arifm(a : int, b : int, znak : str) -> int:
    if znak == "+" :
        print(f"{a} + {b} = {int(a + b)}")
    elif znak == "-":
        print(f"{a} - {b} = {int(a - b)}")
    elif znak == "*":
        print(f"{a} * {b} = {int(a * b)}")
    else:
        print(f"{a} / {b} = {float(a / b)}")
    return 0

arifm(a, b, znak)