# SET 2430 — Week 9: Trees, Binary Search Trees, and Heaps

**Prof. Haiying Xiao** · Fall 2026

---

## 1. Tree Anatomy & Terminology

A **Tree** is a hierarchical, non-linear data structure consisting of nodes connected by directed edges.
* **Invariant:** Exactly one path exists between any two nodes. No cycles permitted.
* **Root:** The topmost node with no parent.
* **Node:** Contains data/value and references/pointers to child nodes.
* **Parent:** A node that has branches extending downward to child nodes.
* **Child:** A node directly below and linked to a parent node.
* **Leaf (External Node):** A node that has no children (degree 0).
* **Edge:** A directed link connecting a parent to a child.
* **Path:** A sequence of consecutive nodes and edges.
* **Subtree:** A tree consisting of a node and all of its descendants.
* **Depth:** The number of edges on the path from the root down to the node (Root depth = 0).
* **Height:** The longest path (number of edges) from the node down to a leaf.
* **Siblings:** Nodes that share the exact same parent node.

```
       A (Root)
      / \
     B   C
    /
   D (Leaf)
```
* **Root:** A
* **Parents:** A, B
* **Children:** B, C (children of A); D (child of B)
* **Leaves:** C, D

---

## 2. Why Use Trees?

1. **Hierarchical Data Representation:** Natural model for organizational charts, file system directories, and the HTML Document Object Model (DOM).
2. **Fast Search, Insertion, and Deletion:** Binary Search Trees allow dynamic collections to achieve average $O(\log n)$ time, outperforming contiguous arrays ($O(n)$ insertion/deletion) and linear linked lists ($O(n)$ search).
3. **Efficient Priority Management:** Heaps allow immediate $O(1)$ lookup of extreme values (min or max) and $O(\log n)$ extraction.
4. **Routing & Text Processing:** Tries (prefix trees) power dictionary lookups, spell checkers, and search-engine autocomplete.

---

## 3. The Family of Trees: Comprehensive Summary Table

| Tree Type | Child Limit | Ordering Rule | Best Use Case | Intuitive Analogy |
| :--- | :---: | :--- | :--- | :--- |
| **Binary Tree** | Max 2 | None | Foundation for specialized trees | Family tree with a 2-child policy |
| **Binary Search Tree (BST)** | Max 2 | $\text{Left} < \text{Parent} < \text{Right}$ | Fast dynamic search, insert, and delete | Phone book organized alphabetically |
| **Heap (Binary Heap)** | Max 2 | $\text{Parent} \ge \text{Children}$ (Max-Heap)<br>$\text{Parent} \le \text{Children}$ (Min-Heap) | Priority queues, scheduling, top-K selection | To-do list sorted by urgency |
| **Balanced BST (AVL / Red-Black)** | Max 2 | $\text{Left} < \text{Parent} < \text{Right}$ (Auto-balancing) | Guaranteed worst-case $O(\log n)$ operations | Self-organizing bookshelf |
| **B-Tree** | Many | Keys inside nodes are sorted | Database storage engines, file systems | Library card catalog system |
| **Trie (Prefix Tree)** | Many (e.g. 26) | Edge path from root spells the key | Autocomplete, spell check, IP routing | Dictionary flipped letter-by-letter |

---

## 4. Binary Search Trees (BST)

### The BST Invariant
For every node $X$ in the tree:
* All values in the left subtree of $X$ must be **strictly less than** $X$.
* All values in the right subtree of $X$ must be **strictly greater than** $X$.

```
         8
       /   \
      3     10
     / \      \
    1   6      14
       / \    /
      4   7  13
```

### Time Complexity of BST Operations

| Operation | Average Case | Worst Case (Degenerate / Skewed) | Balanced BST (AVL/Red-Black) |
| :--- | :---: | :---: | :---: |
| **Search** | $O(\log n)$ | $O(n)$ | $\Theta(\log n)$ |
| **Insert** | $O(\log n)$ | $O(n)$ | $\Theta(\log n)$ |
| **Delete** | $O(\log n)$ | $O(n)$ | $\Theta(\log n)$ |

---

## 5. In-Class Practice: Recursive `count_nodes`

```python
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def count_nodes(root):
    # Base Case: empty tree has 0 nodes
    if root is None:
        return 0
    # Recursive Case: 1 (current node) + left subtree + right subtree
    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

---

## 6. Heaps & Priority Queues

A **Heap** is a complete binary tree (all levels fully packed except possibly the bottom level, which is filled from left to right) that satisfies the **Heap Order Property**:
* **Min-Heap:** $\text{Parent} \le \text{Children}$ (Root is always the minimum value).
* **Max-Heap:** $\text{Parent} \ge \text{Children}$ (Root is always the maximum value).

### Practical Applications of Heaps:
1. **Priority Queues:** OS job schedulers and network packet routers.
2. **Merge $K$ Sorted Lists:** Efficient multi-way merging.
3. **Find $K$-th Largest / Smallest Element:** Maintain a heap of size $k$ in $O(n \log k)$ time.
4. **Dijkstra’s Algorithm:** Extracting the nearest vertex in $O((V + E) \log V)$ time.
5. **Continuous Median Maintenance:** Using a Max-Heap for lower half + Min-Heap for upper half.

### Heap vs. Balanced BST Comparison Table

| Operation | Binary Heap | Balanced BST | Explanation |
| :--- | :---: | :---: | :--- |
| **Find Min / Max** | $\mathbf{O(1)}$ | $O(\log n)$ | Heap root directly stores the extremum. |
| **Insert** | $O(\log n)$ | $O(\log n)$ | Both bubble/rebalance up the tree. |
| **Delete Min / Max** | $O(\log n)$ | $O(\log n)$ | Heap sifts down; BST re-links successor. |
| **Search Arbitrary** | $O(n)$ | $\mathbf{O(\log n)}$ | Heaps lack left-vs-right ordering. |
| **Delete Arbitrary** | $O(n)$ | $\mathbf{O(\log n)}$ | Finding the target node in a heap takes linear time. |

> **Advanced Note:** If an arbitrary node's index is tracked using a hash map, heap deletion can be optimized to $O(\log n)$.
