#a program for list sorting 

n = int(input("How many elements you want to have in the list"))
print("Enter the elements of list row wise: ")
list = []


for i in range(n):
    a = int(input())
    list.append(a)

#printing the list
print("Your list is: ")
print(list)

#for sorting the array 
print("The sorted list will be: ")
list.sort()
print(list)
