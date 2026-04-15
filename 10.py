def min_platforms(arr, dep):
    arr.sort()
    dep.sort()

    i = j = 0
    platforms = 0
    max_platforms = 0
    n = len(arr)

    while i < n and j < n:
        if arr[i] <= dep[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1

    return max_platforms

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

print(min_platforms(arr, dep)) 