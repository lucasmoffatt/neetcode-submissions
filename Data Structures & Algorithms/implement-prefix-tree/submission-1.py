class PrefixTree:

    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

    def insert(self, word: str) -> None:
        curr = self
        
        for c in word:
            i = ord(c) - ord('a')

            if curr.children[i] is None:
                curr.children[i] = PrefixTree()
            
            curr = curr.children[i]
        
        curr.isWord = True
            
            


    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            i = ord(c) - ord('a')
            
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        
        return curr.isWord

        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            i = ord(c) - ord('a')
            
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        
        return True
        
        