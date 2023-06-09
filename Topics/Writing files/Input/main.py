# write the code here

line = input()

file = open("input.txt", "w", encoding="utf-8")
file.write(line)
file.close()
