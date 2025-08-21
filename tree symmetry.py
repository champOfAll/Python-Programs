class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Solution:
    def isSymmetric(self, root):
        def mirror(a, b):
            return not a and not b or a and b and mirror(a.left, b.right) and mirror(a.right, b.left)
        return not root or mirror(root.left, root.right)

def build_tree(vals):
    from collections import deque
    nodes = [None if v == "None" else Node(int(v)) for v in vals]
    q = deque([nodes[0]])
    i = 1
    while q and i < len(nodes):
        curr = q.popleft()
        if i < len(nodes): curr.left = nodes[i]; q.append(nodes[i]); i += 1
        if i < len(nodes): curr.right = nodes[i]; q.append(nodes[i]); i += 1
    return nodes[0]

raw = input("Enter tree nodes (level-order, 'None' for missing):\n> ").strip()
if raw.startswith("[") and raw.endswith("]"):
    raw = raw[1:-1].replace(",", " ")
vals = raw.split()

root = build_tree(vals)
print(Solution().isSymmetric(root)) 