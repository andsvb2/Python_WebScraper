first_number = int(input())
second_number = int(input())

def number_sort(f_number, s_number):
    if f_number >= s_number:
        print(f_number, s_number, sep='\n')
    else:
        print(s_number, f_number, sep='\n')

number_sort(first_number, second_number)
