# put your python code here

sum_total = int()
sum_squares = int()

while True:
    number = int(input())
    sum_total += number
    sum_squares += number ** 2

    if sum_total == 0:
        break

print(sum_squares)