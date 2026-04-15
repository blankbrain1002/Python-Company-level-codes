def two_sum(arr, target):
    num_map = {}  

    for i in range(len(arr)):
        needed = target - arr[i]

        if needed in num_map:
            return [num_map[needed], i]

        num_map[arr[i]] = i

    return []

arr = [2, 7, 11, 15]
target = 26

print(two_sum(arr, target))  