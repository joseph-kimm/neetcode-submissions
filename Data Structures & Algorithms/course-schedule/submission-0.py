class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        c_graph = {i:[] for i in range(numCourses)}

        for a,b in prerequisites:
            c_graph[a].append(b)

        visit = set()

        def dfs(course):

            if course in visit:
                return False

            if len(c_graph[course]) == 0:
                return True

            visit.add(course)

            for pre in c_graph[course]:

                if not dfs(pre): 
                    return False

            visit.remove(course)
            c_graph[course] = []

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

