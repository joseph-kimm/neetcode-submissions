class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [set() for _ in range(len(nums) + 1)]
        count = dict()

        for num in nums:
            if num not in count.keys():
                bucket[1].add(num)
                count[num] = 1

            else:
                bucket[count[num]].remove(num)
                count[num] += 1
                bucket[count[num]].add(num)

        res = []
        i = max(count.values())

        while len(res) < k:
            if len(bucket[i]) > 0:
                res.extend(bucket[i])

            i -= 1
        
        return res
            
                


        