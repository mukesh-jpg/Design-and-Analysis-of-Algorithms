# Selection Sort in Descending Order

arr = list(map(int, input("Enter elements: ").split()))
n = len(arr)

for i in range(n - 1):
    max_index = i
    for j in range(i + 1, n):
        if arr[j] > arr[max_index]:
            max_index = j

    # Swap
    arr[i], arr[max_index] = arr[max_index], arr[i]

print("Sorted Array:", *arr)
