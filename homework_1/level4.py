import math

class Calculator:

    def __init__(self, a, znak, b):
        self.a = a
        self.b = b
        self.znak = znak
    
    def arifm(self):
        if self.znak == "+":
            self.answer = a + b
            print(f"{self.a} + {self.b} = {self.answer}")
        elif self.znak == "-":
            self.answer = a - b
            print(f"{self.a} - {self.b} = {self.answer}")
        elif self.znak == "*":
            self.answer = a * b
            print(f"{self.a} * {self.b} = {self.answer}")
        else:
            self.answer = a / b
            print(f"{self.a} / {self.b} = {self.answer}")
    
    def triganometry(self):
        if self.znak == "sin":
            self.answer = math.sin(self.a)
            print(f"sin({self.a}) = {self.answer}")
        elif self.znak == "cos":
            self.answer = math.cos(self.a)
            print(f"cos({self.a}) = {self.answer}")
        else:
            self.answer = math.tan(self.a)
            print(f"tg({self.a}) = {self.answer}")
        
first = str(input("Что вы хотите? Тригонометрия(trg) или базовые арифм(arifm) операции: "))

if first == "trg":
    znak, a = map(str, input().split())
    a = int(a)
    calk = Calculator(a, znak, 0)
    calk.triganometry()
else:
    a, znak, b = map(str, input().split())
    a = int(a)
    b = int(b)
    calk = Calculator(a, znak, b)
    calk.arifm()

