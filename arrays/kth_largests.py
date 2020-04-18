import heapq


def kth_largest(nums, k):
    return sorted(nums)[-k]


nums = [3, 2, 1, 5, 6, 4]
k = 2

print(kth_largest(nums, k))


def kth_largest_heap(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    for _ in range(len(nums)-k):
        heapq.heappop(heap)

    return heapq.heappop(heap)


print(kth_largest_heap(nums, k))
