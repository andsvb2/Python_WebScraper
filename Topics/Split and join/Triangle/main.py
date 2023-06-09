triangle_size = int(input())

count = 1
base_triangle = (triangle_size * 2) - 1

for _ in range(triangle_size):
    text = "#" * count
    print(text.center(base_triangle))
    count += 2
