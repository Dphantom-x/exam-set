# Assignment 7 - Binary Trees and Binary Search Trees

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.key = val
        self.left = left
        self.right = right

Node = TreeNode


# 1. Count Leaf Nodes
def countLeaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return countLeaves(root.left) + countLeaves(root.right)

count_leaves = countLeaves


# 2. Tree Traversals
def preorder(root):
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


# 3. Kth Smallest Element in a BST
def kthSmallest(root, k):
    vals = inorder(root)
    if 1 <= k <= len(vals):
        return vals[k - 1]
    return None

kth_smallest = kthSmallest


# 4. Bonus: K Closest Values in a BST
def closestKValues(root, target, k):
    if not root or k <= 0:
        return []
    vals = inorder(root)
    vals.sort(key=lambda x: abs(x - target))
    return vals[:k]

closest_k_values = closestKValues


if __name__ == '__main__':
    # Test 1: countLeaves
    t1 = TreeNode(10)
    t1.left = TreeNode(5)
    t1.right = TreeNode(15)
    t1.left.left = TreeNode(3)
    t1.left.right = TreeNode(7)
    t1.right.right = TreeNode(20)
    print("Leaf nodes:", countLeaves(t1))

    # Test 2: traversals
    t2 = TreeNode('A')
    t2.left = TreeNode('B')
    t2.right = TreeNode('C')
    t2.left.left = TreeNode('D')
    t2.left.right = TreeNode('E')
    print("Preorder:", preorder(t2))
    print("Inorder:", inorder(t2))
    print("Postorder:", postorder(t2))

    # Test 3: kthSmallest
    t3 = TreeNode(5)
    t3.left = TreeNode(3)
    t3.right = TreeNode(7)
    t3.left.left = TreeNode(2)
    t3.left.right = TreeNode(4)
    t3.right.left = TreeNode(6)
    t3.right.right = TreeNode(8)
    print("3rd smallest:", kthSmallest(t3, 3))

    # Test 4: closestKValues (Bonus)
    t4 = TreeNode(4)
    t4.left = TreeNode(2)
    t4.right = TreeNode(5)
    t4.left.left = TreeNode(1)
    t4.left.right = TreeNode(3)
    print("Closest values:", closestKValues(t4, 3.7, 2))
