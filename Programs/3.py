# Selection Sort with Comparison and Swap Count

arr = list(map(int, input("Enter elements: ").split()))
n = len(arr)

comparisons = 0
swaps = 0

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        comparisons += 1
        if arr[j] < arr[min_index]:
            min_index = j

    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps += 1

print("Sorted Array:", *arr)
print("Comparisons:", comparisons)
print("Swaps:", swaps)
