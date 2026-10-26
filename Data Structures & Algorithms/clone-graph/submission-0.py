"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return

        nodes = dict()
        queue = collections.deque()

        root = Node(1)
        nodes[1] = root

        queue.append(node)

        while queue:
            node = queue.popleft()
            val = node.val

            for n in node.neighbors:

                if n.val not in nodes.keys():
                    new_node = Node(n.val)
                    nodes[n.val] = new_node
                    queue.append(n)

                nodes[val].neighbors.append(nodes[n.val])
        
        return root



                
            


        