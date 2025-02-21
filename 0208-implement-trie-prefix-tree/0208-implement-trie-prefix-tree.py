# Neetcode approach
# Time Complexity: O(N), O(N), O(N) N = number of chars in a word
# Space Complexity: O(K*N) for K strings of N chars each
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            # If char is not in the current children, insert it
            if char not in curr.children:
                curr.children[char] = TrieNode()
            # Now that we have the char, move next
            curr = curr.children[char]
        # Mark the end of string after for loop
        curr.is_end = True


    def search(self, word: str) -> bool:
        # Traverse the Trie
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            # Move to next node
            curr = curr.children[char]
        
        # Return true only if this is the end of str
        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        # Traverse the Trie
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            # Move to next
            curr = curr.children[char]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)