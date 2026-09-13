# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        if not root:
            return res

        queue = collections.deque()
        queue.append((root,0))

        level = 0

        while queue:

            while len(queue) > 0 and queue[0][1] == level:
                node, i = queue.popleft()

                if node.left:
                    queue.append((node.left, level+1))

                if node.right:
                    queue.append((node.right, level+1))

            res.append(node.val)
            level += 1

        return res

            


        