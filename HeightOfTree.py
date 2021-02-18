"""
Write a Program to Find the Maximum Depth or Height of a Tree
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def height(root):
    if root is None:
        return -1
    
    ldepth = height(root.left)
    rdepth = height(root.right)

    if(ldepth > rdepth):
        return ldepth + 1
    else:
        return rdepth + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)

if __name__ == "__main__":
    print(height(root))