class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left: BinaryTreeNode = left
        self.right: BinaryTreeNode = right
        self.parent: BinaryTreeNode = parent

