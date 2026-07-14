class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):

            cars.append((position[i], speed[i]))

        cars.sort(reverse=True)
        times = []

        for i in range(len(cars)):
            times.append((target - cars[i][0]) / cars[i][1])

        stack = []

        for time in times:
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)

        