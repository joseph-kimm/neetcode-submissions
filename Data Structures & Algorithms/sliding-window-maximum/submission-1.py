class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        res = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        num, i = heap[0]
        res.append(-num)

        for r in range(k, len(nums)):
            heapq.heappush(heap, (-nums[r], r))

            while heap[0][1] <= r - k:
                heapq.heappop(heap)

            res.append(-heap[0][0])

        return res

