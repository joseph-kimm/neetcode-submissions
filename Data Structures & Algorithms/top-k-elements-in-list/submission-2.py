class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = dict()

        for num in nums:
            if num not in count.keys():
                count[num] = 0

            count[num] += 1

        heap = []

        for key, value in count.items():
            heap.append((value,key))

        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)

        res = []
        for v,k in heap:
            res.append(k)

        return res