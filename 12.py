import heapq
from collections import Counter

def top_k_frequent(nums, k):
    freq = Counter(nums)
    min_heap = []

    for num, count in freq.items():
        heapq.heappush(min_heap, (count, num))
        
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for count, num in min_heap]

print(top_k_frequent([1,1,1,2,2,3], 2))  