class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        # make empty
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
        root.end = True #mark end of word

    def search(self, word: str) -> bool:
        # find child, keep going down, return self.end
        root = self.root
        for char in word:
            if char not in root.children:
                return False
            root = root.children[char]
        return root.end

    def startsWith(self, prefix: str) -> bool:
        #same as above but return true insread of end
        root = self.root
        for char in prefix:
            if char not in root.children:
                return False
            root = root.children[char]
        return True
        