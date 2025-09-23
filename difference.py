# maximum difference between two elements in an array
def max_difference(arr):
    if len(arr) < 2:
        return 0
    res = arr[1] - arr[0]
    min_value = arr[0]

    for i in range(1, len(arr)):
        res = max(res, arr[i] - min_value)
        min_value = min(min_value, arr[i])
    return res

print(max_difference([2]))