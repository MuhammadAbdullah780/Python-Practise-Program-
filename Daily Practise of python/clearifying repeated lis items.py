n = int(input("How many numbers you want to print in repeated_list: "))


repeated_list = [int(input()) for i in range(n)]

print("The list you entered is: ", repeated_list)
un_repeated_list = []

for elements in repeated_list:
    if elements not in un_repeated_list:
        un_repeated_list.append(elements)

print("The unrepeated list is: " , un_repeated_list)