# Slice sample_list into 3 equal chunks and reverse each chunk


n = int(input("how many elements you want in a list: "))
sample_list = [int(input("Enter no of sample_list")) for i in range(n)]
chunk = len(sample_list)//3
start = 0
end = chunk


for i in range(chunk):
    index = slice(start, end)

    # getting the sample_list chunk
    list_chunk = sample_list[index]

    # printing it
    print(f"chunk {i +1} : {list_chunk}")

    # reversing it
    print(f"After reversing it: {list(reversed(list_chunk))}")

    start = end
    end += chunk