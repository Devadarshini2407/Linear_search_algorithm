# Linear Search

n = int(input("Enter the number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

target = int(input("Enter the element to search: "))

for i in range(n):
    if arr[i] == target:
        print("Element found at index", i)
        break
else:
    print("Element not found")
