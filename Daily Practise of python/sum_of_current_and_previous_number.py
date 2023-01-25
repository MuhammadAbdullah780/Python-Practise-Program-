# Print the sum of the current number and the previous number

n = int(input("Enter a number: "))

for i in range(n):
    print(
        f"current number {i}, previous number is {i-1} and their sum is: {i +(i-1)}")
