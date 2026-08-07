# Bubble Sort - Count Number of Passes

arr = list(map(int, input("Enter elements: ").split()))
n = len(arr)

passes = 0

for i in range(n - 1):
    passes += 1
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted Array:")
print(*arr)
print("Number of Passes:", passes)
