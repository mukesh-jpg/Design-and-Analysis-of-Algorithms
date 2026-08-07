# Optimized Bubble Sort

arr = list(map(int, input("Enter elements: ").split()))
n = len(arr)

passes = 0

for i in range(n - 1):
    swapped = False
    passes += 1

    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    if not swapped:
        print("Array is already sorted")
        break

print("Passes required:", passes)
print("Sorted Array:", *arr)
