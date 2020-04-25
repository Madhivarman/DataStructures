"""
Design a data structure that supports the following two operations:
"""
class TrieNode():
    def __init__(self, val):
        self.val = val
        self.isEnd = False
        self.children = {} #to append its children


class WordDictionary():

    def __init__(self):
        self.rootnode = TrieNode(None)

    def addWord(self, word):
        node = self.rootnode
        #iterate through the character
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char] #update the pointer on Tree

        node.isEnd = True
    
    def search(self, word):
        node = self.rootnode
        #iterate throug the character
        for i in range(len(word)):
            #check if i not in the children
            if word[i] not in node.children and word[i] != '.':
                return False
            elif word[i] == '.':
                for child in node.children:
                    if self.dfs(node.children[child], word[i+1:]):
                        return True
                return False
            
            #update the tree pointer
            node = node.children[word[i]]
        
        if node.isEnd:
            return True

        return False
    

    def dfs(self, root, word):
        if not word and root.isEnd:
            return True

        node =  root
        for i in range(len(word)):
            if word[i] not in node.children and word[i] != '.':
                return False
            elif word[i] == '.':
                for child in node.children:
                    if self.dfs(node.children[child], word[i+1:]):
                        return True
                return False
            
            node = node.children[word[i]]
        
        if node.isEnd:
            return True
        
        return False

words = ['bad', 'mad', 'abcd']
mainobj = WordDictionary()

for word in words:
    mainobj.addWord(word)

print(mainobj.search('b.m'))
print(mainobj.search('.ad'))
print(mainobj.search('b..'))