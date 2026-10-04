import heapq

h = list()

heapq.heappush(h,10)
heapq.heappush(h,43)
heapq.heappush(h,76)
heapq.heappush(h,5)

heapq.heappop(h)

print("힙 내부 상태:", h)

print("pop:", heapq.heappop(h))
print("pop:", heapq.heappop(h))

print("힙 내부 상태:", h)

nums = [5,20,25,10,15]
heapq.heapify(nums)
print("heapify 결과:",nums)
print("최소값:",nums[0])


