class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numbers = set(nums)
        start = set()

        for num in numbers:
            if num-1 not in numbers:
                start.add(num)

        longest = 0
        
        for n in start:
            seq = 0
            while n in numbers:
                seq += 1
                n += 1
            
            longest = max(seq, longest)
        
        return longest
        