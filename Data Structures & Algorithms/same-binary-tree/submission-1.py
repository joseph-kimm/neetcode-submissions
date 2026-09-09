# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queue_p = collections.deque()
        queue_q = collections.deque()

        if not p and not q:
            return True

        if not p or not q:
            return False

        queue_p.append((p,'r',0))
        queue_q.append((q,'r',0))

        while queue_p and queue_q:

            p_node,p_pos,p_height = queue_p.popleft()
            q_node,q_pos,q_height = queue_q.popleft()

            if p_node.val != q_node.val or p_pos != q_pos or p_height != q_height:

                return False

            if p_node.left:
                queue_p.append((p_node.left, 'l', p_height+1))

            if p_node.right:
                queue_p.append((p_node.right, 'r', p_height+1))

            if q_node.left:
                queue_q.append((q_node.left, 'l', q_height+1))

            if q_node.right:
                queue_q.append((q_node.right, 'r', q_height+1))


        if queue_q or queue_p:
            return False
            
        return True

        