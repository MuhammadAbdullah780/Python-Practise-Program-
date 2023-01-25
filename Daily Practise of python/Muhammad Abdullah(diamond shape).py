n = int(input("Enter the no of rows for printing the diamond"))
for i in range(0,n):
    for s in range(0 , n-i):
        print(" ")
    for j in range(0, 2*i-1):
        print("*" , end="")