a, znak, b = map(str, input().split())

a = int(a)
b = int(b)

if znak == "+" :
    print(f"{a} + {b} = {a + b}")
elif znak == "-":
    print(f"{a} - {b} = {a - b}")
elif znak == "*":
    print(f"{a} * {b} = {a * b}")
else:
    print(f"{a} / {b} = {a / b}")