class Node:

    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):

        self.root = Node()

    def addWord(self, word: str) -> None:

        curr = self.root
        
        for char in word:

            if char not in curr.children.keys():
                curr.children[char] = Node()
                
            curr = curr.children[char]

        curr.end = True

        return
        

    def search(self, word: str) -> bool:

        candidates = [self.root]

        for char in word:

            new = []
            for node in candidates:

                if char == '.':

                    for child in node.children.keys():
                        new.append(node.children[child])
                    
                else:

                    if char in node.children.keys():
                        new.append(node.children[char])
                
            if len(new) == 0:
                return False

            candidates = new

        for node in candidates:
            
            if node.end:
                return True

        return False





        
        
