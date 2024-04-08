class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def find_max(root):
    if root is None:
        return float('-inf')

    res = root.val
    lres = find_max(root.left)
    rres = find_max(root.right)

    if lres > res:
        res = lres
    if rres > res:
        res = rres
    return res

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(7)
    root.right = TreeNode(5)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(11)
    root.right.right = TreeNode(9)
    root.right.right.left = TreeNode(4)

    print(f"Maximum element is {find_max(root)}")