class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = dict()

        for num in nums:
            if num not in count.keys():
                count[num] = 0

            count[num] += 1

        heap = []

        for key,val in count.items():
            heapq.heappush(heap, (val,key))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for val,key in heap:
            res.append(key)

        return res