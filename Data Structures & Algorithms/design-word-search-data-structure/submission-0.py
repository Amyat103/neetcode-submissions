class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        #if letter dont exist, add and keep going else if exist make it end if end
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True

    def search(self, word: str) -> bool:
        #search using dfs func
        # 2 path, 1 for regular, 1 if there "." then well need to lok through all children and pas that stage
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                char = word[i]
                if char == ".":
                    # go through each child
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.end

        return dfs(0, self.root)