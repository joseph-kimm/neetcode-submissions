class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i, stone in enumerate(stones):
            stones[i] = -stone

        heapq.heapify(stones)

        while len(stones) > 1:

            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            new_stone = -abs(stone1 - stone2)

            if new_stone != 0:
                heapq.heappush(stones, new_stone)

        if not stones:
            return 0

        else:
            return -stones[0]


        