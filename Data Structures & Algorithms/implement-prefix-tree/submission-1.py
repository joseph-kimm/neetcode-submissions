class Node:
        def __init__(self):
            self.children = {}
            self.end = False

class PrefixTree:

    def __init__(self):

        self.root = Node()

    def insert(self, word: str) -> None:

        curr = self.root

        for char in word:
            if char not in curr.children.keys():
                nxt = Node()
                curr.children[char] = nxt

            curr = curr.children[char]

        curr.end = True
        return

    def search(self, word: str) -> bool:

        curr = self.root

        for char in word:

            if not char in curr.children.keys():
                return False
            
            curr = curr.children[char]

        return curr.end


    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for char in prefix:

            if not char in curr.children.keys():
                return False
            
            curr = curr.children[char]

        return True
        
        