# Bubble Sort in Descending Order

arr = list(map(int, input("Enter elements: ").split()))
n = len(arr)

# Bubble Sort (Descending)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted Array:", *arr)
