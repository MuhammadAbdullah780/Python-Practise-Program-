# a program for printing the fibonacci series till n

#taking input
n = int(input("Enter no of rows you want to print in fibonacci series: "))

#further process
first = 0
second = 1

#condition if n is less than or equals to zero
while (n < 0) and (n == 0):
    print("Error")


if n == 1:
    print(first)
elif n == 2:
     print(second)
else:
    print(first)
    print(second)
    for i in range(0,n-1):
         third = first + second
         print(third)
         first = second
         second = third
