# Bubble Sort to Sort Names Alphabetically

n = int(input("Enter number of names: "))
names = []

print("Enter names:")
for i in range(n):
    names.append(input())

# Bubble Sort
for i in range(n - 1):
    for j in range(n - 1 - i):
        if names[j] > names[j + 1]:
            names[j], names[j + 1] = names[j + 1], names[j]

print("Sorted Names:")
for name in names:
    print(name)
