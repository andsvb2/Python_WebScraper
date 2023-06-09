a: int = int(input())
b: int = int(input())


try:
    print(a / b)
except ZeroDivisionError:
    print("The Error!")
