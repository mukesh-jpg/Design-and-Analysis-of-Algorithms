# Find kth Smallest Element using Selection Sort

arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))

n = len(arr)

# Selection Sort (Ascending)
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(f"{k}rd Smallest Element = {arr[k-1]}")
