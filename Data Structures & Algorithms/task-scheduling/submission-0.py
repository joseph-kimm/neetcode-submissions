class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counter = dict()

        for task in tasks:

            counter[task] = counter.get(task, 0)
            counter[task] += 1

        queue = collections.deque()
        heap = []
        time = 0

        for task, count in counter.items():
            heapq.heappush(heap, (-count, task))

        while queue or heap:

            if heap: 
                count,task = heapq.heappop(heap)

                count+= 1

                if count != 0:
                    queue.append((time, (count, task)))
            
            if queue and time - queue[0][0] == n:

                heapq.heappush(heap, queue.popleft()[1])

            time+= 1

        return time
            



            


            


        