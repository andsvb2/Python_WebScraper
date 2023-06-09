angle_a = int(input())
angle_b = int(input())
angle_c = int(input())

def check_triangle(a, b, c):
    if a + b + c == 180:
        print("The triangle is valid!")
    else:
        print("The triangle is not valid!")

check_triangle(angle_a, angle_b, angle_c)
