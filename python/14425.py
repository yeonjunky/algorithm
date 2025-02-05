class Trie:
    def __init__(self):
        self.root = Node(None)
    
    def insert(self, string):
        curr_node = self.root
        str_len = len(string)

        for i, c in enumerate(string):
            if c not in curr_node.children:
                curr_node.children[c] = Node(i == (str_len - 1))
            curr_node = curr_node.children[c]
        
        curr_node.is_end = True
    
    def search(self, string):
        curr_node = self.root

        for c in string:
            if c in curr_node.children:
                curr_node = curr_node.children[c]
            else:
                return False
        
        if curr_node.is_end:
            return True
        return False

class Node:
    def __init__(self, is_end):
        self.children = {}
        self.is_end = is_end

import sys

n, m = map(int, sys.stdin.readline().split())
t = Trie()
cnt = 0

for _ in range(n):
    t.insert(sys.stdin.readline().rstrip())

for _ in range(m):
    if t.search(sys.stdin.readline().rstrip()):
        cnt += 1

print(cnt)
