# Binary Search with Automatic Sorting

n = int(input("Enter the number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Sort the array
arr.sort()

print("Sorted array:", arr)

target = int(input("Enter the element to search: "))

low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Element found at position", mid + 1)
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")