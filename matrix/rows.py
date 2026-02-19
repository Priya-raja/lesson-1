

arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

for row in arr:
    for x in row:
        print(x, end=" ")
    print()
  
def search_in_matrix(arr,target):
    row,cols = len(arr),len(arr[0])

    for i in range(row):
        for j in range(cols):
            if arr[i][j] == target:
                return True
    return False

print(search_in_matrix(arr, 10))

if search_in_matrix(arr, 10):
    print("found")
else:    print("not found")