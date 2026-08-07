# Selection Sort to Sort Student Marks

marks = list(map(int, input("Enter student marks: ").split()))
n = len(marks)

# Selection Sort
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if marks[j] < marks[min_index]:
            min_index = j

    # Swap
    marks[i], marks[min_index] = marks[min_index], marks[i]

print("Sorted Marks:", *marks)
