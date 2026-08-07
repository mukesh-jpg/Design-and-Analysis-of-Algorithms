# Basic Bubble Sort

arr = list(map(int, input("Enter elements: ").split()))
n = len(arr)

# Bubble Sort
for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted Array:", *arr)
