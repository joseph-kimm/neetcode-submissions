class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_rate = r

        while l <= r:
            rate = l + ((r-l) // 2)
            time = 0

            for pile in piles:
                if pile % rate == 0:
                    time += pile // rate

                else:
                    time += 1+ pile // rate

            if time <= h:
                min_rate = min(min_rate, rate)
                r = rate - 1

            else:
                l = rate + 1

        return min_rate