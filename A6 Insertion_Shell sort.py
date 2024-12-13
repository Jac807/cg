def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Taking input for percentages dynamically
n = int(input("Enter the number of students: "))
percentages = []
for i in range(n):
    score = float(input(f"Enter percentage for student {i + 1}: "))
    percentages.append(score)

# Using Insertion Sort
insertion_sort(percentages)
print("Top 5 scores using Insertion Sort:", percentages[-5:])

# Using Shell Sort
percentages = percentages[:]  # Copy the sorted list
shell_sort(percentages)
print("Top 5 scores using Shell Sort:", percentages[-5:])
