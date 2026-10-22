# Assignment 4

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Part A

def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# 2. Recurrence: T(n) = 2T(n/2) + O(1)

# 3. Solve for height h:
# T(h) = 2T(h-1) + c = O(2^h)
# For a full tree n ~ 2^h, so O(2^h) = O(n)

# 4. Time complexity: O(n)


# Part B

def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# 2. Recurrence: T(n) = 2T(n/2) + O(1)

# 3. Time complexity: O(n)

# 4. Recursive vs BFS:
# Both are O(n) time. Recursive is shorter code with O(h) call stack, but can hit recursion limits.
# BFS uses a queue with O(w) space, avoiding stack overflow.

def max_depth_bfs(root):
    if not root:
        return 0
    q = [root]
    depth = 0
    while q:
        depth += 1
        level = []
        for node in q:
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        q = level
    return depth


# tests
if __name__ == '__main__':
    # tree 1
    t1 = Node(1)
    t1.left = Node(2, Node(4), Node(5))
    t1.right = Node(3)
    print("count:", count_nodes(t1))

    # tree 2
    t2 = Node(3)
    t2.left = Node(9)
    t2.right = Node(20, Node(15), Node(7))
    print("depth rec:", max_depth(t2))
    print("depth bfs:", max_depth_bfs(t2))
