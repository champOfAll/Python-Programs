class Leaf:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

def is_mirror_iso(root):
    def is_mirror(l1, l2):
        if l1 is None and l2 is None:
            return True
        if l1 is None or l2 is None:
            return False
        return (l1.value==l2.value and is_mirror(l1.left, l2.right) and
            is_mirror(l1.right, l2.left))
    if root is None:
        return True
    return is_mirror(root.left, root.right)

def build_tree(values):
    if not values or values[0]==-999:
        return None

    root=Leaf(values[0])
    queue=[root]
    i=1
    while queue and i<len(values):
        current=queue.pop(0)
        if i<len(values):
            if values[i]!=-999:
                current.left=Leaf(values[i])
                queue.append(current.left)
            i+=1
        if i<len(values):
            if values[i]!=-999:
                current.right=Leaf(values[i])
                queue.append(current.right)
            i+=1
    return root

user_input=input("Enter tree nodes in level-order (use -999 for missing): ")
node_values=[int(val) for val in user_input.strip().split()]
tree_root=build_tree(node_values)

print("Is the tree mirror-isomorphic?", is_mirror_iso(tree_root))