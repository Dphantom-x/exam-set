# CUNY Data Structures Authentic Past Exam Question Bank
**Target Course:** SET 2430 — Algorithmic Design and Data Structures  
**Institution:** New York City College of Technology (City Tech - CUNY), Computer Engineering Technology / Software Engineering Department  
**Instructor:** Professor Haiying Xiao (Office: Voorhees V-631)  
**Midterm Target Window:** Fall 2026 (Week 8, Mid-October)  
**Exam Format:** In-Person, Closed-Book, Handwritten Paper-Based (No IDE / Compiler)  

---

## 1. Executive Intelligence & Professor Profile: Prof. Haiying Xiao

### 1.1 Academic Background & Teaching Style
* **Affiliations:** Previously faculty in Technology and Computing at Queensborough Community College (QCC - CUNY); currently teaching in City Tech's Computer Engineering Technology / Software Engineering Technology (CET/SET) program. Co-author of Open Educational Resources (OER) on CUNY Academic Works (e.g., *Software Engineering: AI-Enhanced Full Stack Development*).
* **Pedagogical Approach:**
  * Highly structured weekly slide decks supplemented by live coding in VS Code during lectures and weekly lab assignments (10 assignments total, accounting for **40% of the course grade**).
  * Strong emphasis on bridging mathematical formalism (summations, limits, recurrence relations, expansion trees) with clean Python object-oriented implementation.
  * **Strict Departmental Attendance & Policy Enforcement:** 1–19 min late = 1 Late; 3 Lates = 1 Absence; >20 min late = Absence. **3 absences = automatic "WF" or "F" grade.** Absolutely zero credit for late assignments.
* **Core Textbooks & References:**
  1. *Data Structures & Algorithms in Python* by John Canning, Alan Broder, Robert Lafore (Recommended textbook).
  2. *Introduction to Python Programming and Data Structures*, 3e by Y. Daniel Liang (Reference).
  3. *Cracking the Coding Interview*, 6e by Gayle Laakmann McDowell (Reference).

### 1.2 Prof. Xiao’s Specific Coding & Naming Conventions
Exam graders look for patterns aligned with the instructor's classroom demonstrations:
* **Node Pointer Nomenclature:**
  * For Singly & Circular Linked Lists: Prof. Xiao frequently uses `node.right` (or `node.next`) to represent forward link references.
  * For Doubly Linked Lists: Uses `node.left` (predecessor/prev) and `node.right` (successor/next).
* **Recursive & Tree Structure:** Binary trees use `node.left`, `node.right`, and `node.val` / `node.value`.
* **Dynamic Array Focus:** Resizing mechanics (doubling capacity from 2 to 4 to 8), copying overhead, memory locality (contiguous RAM blocks vs. heap node pointers), and amortized $O(1)$ analysis.
* **Midterm Scope (Weeks 1–7):**
  1. Python OOP fundamentals (`class`, `__init__`, encapsulation, inheritance, `*args`, `**kwargs`).
  2. Algorithm analysis: Best, worst, average cases; $O, \Omega, \Theta, o, \omega$ formal definitions and limits; multi-parameter complexity ($O(N \cdot M)$).
  3. Space complexity: Input space vs. Auxiliary space vs. Call Stack space.
  4. Mathematical foundations: Summations ($\sum i, \sum i^2$), geometric series, logarithms, Gauss's closed form.
  5. Recurrence relations solved via repeated substitution (iterative expansion) and recursion trees ($T(n) = 2T(n/2) + n$, $T(n) = T(n-1) + c$, $T(n) = 2T(n/2) + O(1)$).
  6. Dynamic arrays & Amortized analysis (Python list mechanics, table doubling cost).
  7. Linked Lists: Singly, Doubly, and Circular Linked Lists (insertions, deletions, edge cases, traversals).
  8. Stacks (LIFO) & Queues (FIFO): ADT interfaces, circular arrays, 2-stack browser history navigation, LIFO stack using two FIFO queues, postfix arithmetic expression evaluation.

---

## 2. CUNY Data Structures Exam Formats & Typical Points Distribution

Across CUNY computer science departments (City Tech SET 2430 / CST 3650, Brooklyn College CISC 3130, Hunter College CSCI 235/335, CCNY CSC 22000, Queens College CSCI 313), midterm examinations are strictly paper-based and closed-book.

### Standard 100-Point Handwritten Midterm Blueprint:

| Section | Topic Archetype | Typical Point Range | Cognitive Skill Tested |
| :--- | :--- | :---: | :--- |
| **Part I** | **Asymptotic Analysis & Big-O Classification** | 15–20 pts | Formal definitions ($O, \Omega, \Theta$), ranking growth rates, analyzing code loop fragments. |
| **Part II** | **Recurrence Relations by Repeated Substitution** | 15–20 pts | Step-by-step algebraic expansion, pattern spotting at step $k$, base case substitution, closed-form summation. |
| **Part III** | **Code Tracing & Variable State Table** | 15–20 pts | Tracing loop/recursion execution line-by-line, filling trace table columns, predicting exact STDOUT output. |
| **Part IV** | **Box-and-Pointer Memory Diagrams** | 15–20 pts | Drawing heap memory nodes, pointer arrows, before-and-after states for node insertion/deletion, highlighting lost-pointer traps. |
| **Part V** | **Stack & Queue Simulations** | 15 pts | Tracing LIFO/FIFO states, postfix expression evaluation table, 2-stack browser history, 2-queue stack emulation. |
| **Part VI** | **Handwritten Python Implementation (Edge Cases)** | 15–20 pts | Writing clean, syntax-valid Python methods without an IDE, handling empty list (`head is None`), 1-node lists, head removal, index boundaries. |

---

## 3. The 12 Authentic CUNY Data Structures Exam Questions

---

### Question 1: Asymptotic Loop Analysis & Summations (10 Points)
**Exam Source Style:** City Tech SET 2430 / CST 3650 / Brooklyn College CISC 3130  
**Prompt:**  
Consider the following Python function:
```python
def algorithm_alpha(n):
    total = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            total += 1
    return total
```
1. Write the mathematical summation representing the total number of times `total += 1` executes.
2. Find the closed-form algebraic formula for this summation.
3. State the tight asymptotic time complexity ($\Theta$) and space complexity.

**Official Solution & Rubric:**
1. **Summation Expression (3 pts):**
   $$\sum_{i=1}^n \sum_{j=1}^i 1 = \sum_{i=1}^n i = 1 + 2 + 3 + \dots + n$$
2. **Closed-Form Formula (4 pts):**
   $$\text{Total operations} = \frac{n(n + 1)}{2} = \frac{n^2 + n}{2}$$
3. **Complexity Classification (3 pts):**
   * **Time Complexity:** $\mathbf{\Theta(n^2)}$ (Quadratic time, tight bound).
   * **Auxiliary Space Complexity:** $\mathbf{O(1)}$ (Only uses scalar variables `total`, `i`, `j`).

---

### Question 2: Multi-Parameter Complexity Analysis (8 Points)
**Exam Source Style:** Prof. Xiao SET 2430 Lecture Week 4/5 Exam Pattern  
**Prompt:**  
Analyze the time complexity of the following code fragment:
```python
def process_matrix(grid):
    n = len(grid)
    m = len(grid[0])
    count = 0
    for i in range(n):
        for j in range(m):
            count += grid[i][j]
    return count
```
Is the time complexity $O(n^2)$? Justify your answer thoroughly.

**Official Solution & Rubric:**
* **Answer (3 pts):** No, the time complexity is **not** $O(n^2)$ in the general case; it is $\mathbf{O(n \cdot m)}$ (or $\mathbf{\Theta(n \cdot m)}$).
* **Justification (5 pts):** The algorithm takes two independent input dimensions: $n$ (number of rows) and $m$ (number of columns). The outer loop runs $n$ times, and for each outer iteration, the inner loop runs $m$ times. Total operations equal $c \cdot n \cdot m$. The complexity can only be expressed as $O(n^2)$ if it is explicitly given that $n = m$ (a square matrix). In arbitrary rectangular matrices where $m \gg n$ or $n \gg m$, simplifying to $O(n^2)$ is mathematically incorrect.

---

### Question 3: Recurrence Relation by Repeated Substitution — Divide-and-Conquer (15 Points)
**Exam Source Style:** City Tech SET 2430 Week 4/5 / CCNY CSC 22000  
**Prompt:**  
Given the recurrence relation describing MergeSort / recursive array splitting:
$$T(n) = 2T(n/2) + n \quad \text{for } n > 1, \quad \text{with base case } T(1) = 1$$
Solve for the closed-form Big-O running time using the **repeated substitution (expansion) method**. You must show at least three substitution steps, establish the generalized formula for step $k$, determine the stopping condition, and show the final algebraic derivation.

**Official Solution & Rubric:**
* **Step 1: Initial Equation (1 pt):**
  $$T(n) = 2T(n/2) + n$$
* **Step 2: First Substitution (Substitute $T(n/2) = 2T(n/4) + n/2$) (3 pts):**
  $$T(n) = 2\left[2T(n/4) + \frac{n}{2}\right] + n = 4T(n/4) + n + n = 4T(n/4) + 2n$$
* **Step 3: Second Substitution (Substitute $T(n/4) = 2T(n/8) + n/4$) (3 pts):**
  $$T(n) = 4\left[2T(n/8) + \frac{n}{4}\right] + 2n = 8T(n/8) + n + 2n = 8T(n/8) + 3n$$
* **Step 4: Generalize Pattern for Step $k$ (3 pts):**
  $$T(n) = 2^k T\left(\frac{n}{2^k}\right) + k \cdot n$$
* **Step 5: Base Case Termination (3 pts):**
  Set the subproblem size to the base case:
  $$\frac{n}{2^k} = 1 \implies 2^k = n \implies k = \log_2 n$$
* **Step 6: Substitute $k$ and $2^k$ back into the expression (2 pts):**
  $$T(n) = n \cdot T(1) + (\log_2 n) \cdot n = n(1) + n \log_2 n$$
  $$\mathbf{T(n) = n + n \log_2 n \implies O(n \log n)}$$

---

### Question 4: Recurrence Relation for Binary Tree Node Count (10 Points)
**Exam Source Style:** Prof. Xiao SET 2430 Assignment 4 & Oct 7 In-Class Practice  
**Prompt:**  
Consider the following recursive algorithm that counts nodes in a full, balanced binary tree:
```python
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
```
1. Write the recurrence relation $T(n)$ in terms of problem size $n$ (number of nodes).
2. Express the recurrence in terms of tree height $h$.
3. State the time complexity and auxiliary space complexity (call stack).

**Official Solution & Rubric:**
1. **Recurrence in terms of $n$ (3 pts):**
   $$T(n) = 2T(n/2) + O(1), \quad T(0) = O(1)$$
2. **Recurrence in terms of tree height $h$ (3 pts):**
   At height $h$, each node branches into two subtrees of height $h-1$:
   $$T(h) = 2T(h-1) + c \implies T(h) = O(2^h)$$
   Since for a full binary tree $n \approx 2^h - 1$, substituting $2^h \approx n$ yields $O(n)$.
3. **Complexities (4 pts):**
   * **Time Complexity:** $\mathbf{O(n)}$ (Every node in the tree is visited exactly once).
   * **Space Complexity (Auxiliary Call Stack):** $\mathbf{O(h)}$ where $h = \log_2 n$ for a balanced tree, degrading to $\mathbf{O(n)}$ for a skewed tree.

---

### Question 5: Code Tracing with Variable State Table (12 Points)
**Exam Source Style:** Hunter CSCI 235 / City Tech Midterm Standard  
**Prompt:**  
Trace the execution of `mystery_filter([4, 7, 2, 9, 6])`. Complete the variable state table for each iteration of the while loop and state the return value.
```python
def mystery_filter(arr):
    out = []
    i = 0
    acc = 0
    while i < len(arr):
        if arr[i] % 2 == 0:
            acc += arr[i]
            out.append(acc)
        else:
            acc -= 1
        i += 1
    return out
```

**Official Solution & Rubric:**
**Variable State Table (10 pts):**

| Step / Iteration | `i` | `arr[i]` | Condition (`arr[i] % 2 == 0`) | `acc` | `out` (List Contents) |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **Start** | 0 | — | — | 0 | `[]` |
| **Iter 1** | 0 | 4 | True | 4 | `[4]` |
| **Iter 2** | 1 | 7 | False | 3 | `[4]` |
| **Iter 3** | 2 | 2 | True | 5 | `[4, 5]` |
| **Iter 4** | 3 | 9 | False | 4 | `[4, 5]` |
| **Iter 5** | 4 | 6 | True | 10 | `[4, 5, 10]` |
| **Exit** | 5 | — | False (`5 < 5`) | 10 | Loop terminates |

* **Final Return Value (2 pts):** `[4, 5, 10]`

---

### Question 6: Box-and-Pointer Diagram — Singly Linked List Insertion (12 Points)
**Exam Source Style:** City Tech SET 2430 / QCC / Brooklyn College CISC 3130  
**Prompt:**  
You are given a singly linked list with reference `head` pointing to the first node:
```
head ──> [ 10 | • ] ──> [ 30 | • ] ──> [ 40 | None ]
```
You want to insert a new node `newNode = Node(20)` between node `10` and node `30`.  
A pointer `curr` currently references node `10`.
1. Write the exact two lines of Python code required to perform this insertion safely without losing any list nodes.
2. Draw the resulting box-and-pointer diagram showing the new node linked in.
3. Explain what disastrous error occurs if the two lines of code are executed in reverse order.

**Official Solution & Rubric:**
1. **Safe Pointer Rewiring Code (4 pts):**
   ```python
   newNode.next = curr.next  # Step 1: Link new node forward to node 30
   curr.next = newNode       # Step 2: Redirect node 10's pointer to newNode
   ```
2. **Box-and-Pointer Diagram (4 pts):**
   ```
   head
    ↓
   [ 10 | • ] ───┐
                 ↓
               [ 20 | • ] ──> [ 30 | • ] ──> [ 40 | None ]
   ```
   *(Graders require `head` pointing to `10`, `10.next` pointing to `20`, `20.next` pointing to `30`, and `40.next` terminated with `None`).*
3. **Reverse Order Bug / Lost Pointer Trap (4 pts):**
   If executed in reverse:
   ```python
   curr.next = newNode      # Node 10 points to Node 20
   newNode.next = curr.next # Node 20 points to itself! (curr.next is now newNode)
   ```
   *Consequence:* The reference to node `30` and all subsequent nodes (`40`, etc.) is permanently severed and lost in memory (an orphan sublist / memory leak). Furthermore, `newNode` points to itself in an infinite circular loop.

---

### Question 7: Box-and-Pointer Diagram — Doubly Linked List Node Deletion (12 Points)
**Exam Source Style:** Prof. Xiao SET 2430 Week 6/7 (DoublyNode with `left` and `right`)  
**Prompt:**  
A Doubly Linked List uses nodes with three attributes: `left` (prev), `value`, and `right` (next).  
Given three consecutive nodes:
```
... <══> [ left | 100 | right ] <══> [ left | 200 | right ] <══> [ left | 300 | right ] <══> ...
```
Let `target` reference node `200`. Write the pointer rewiring statements to delete `target` from the list, and draw the resulting box-and-pointer diagram showing how the pointers bypass `target`.

**Official Solution & Rubric:**
1. **Rewiring Code (4 pts):**
   ```python
   target.left.right = target.right  # Node 100's right points to Node 300
   target.right.left = target.left  # Node 300's left points to Node 100
   target.left = None               # Optional clean-up
   target.right = None
   ```
2. **Resulting Memory Diagram (5 pts):**
   ```
          ┌──────────────────────────────────────────────┐
          │                                              ↓
   ... [ left | 100 | right ]                  [ left | 300 | right ] ...
          ↑                                              │
          └──────────────────────────────────────────────┘

                   [ None | 200 | None ] (Unlinked / Garbage Collected)
   ```
3. **Time Complexity (3 pts):**
   * Time complexity is $\mathbf{O(1)}$ because a direct pointer to `target` is already provided (no search traversal required). In a singly linked list, deletion requires $O(n)$ traversal to locate the predecessor node.

---

### Question 8: Circular Linked List Traversal & Modification (10 Points)
**Exam Source Style:** Prof. Xiao Week 7 Class Implementation (`CircularLinkedList`)  
**Prompt:**  
In Prof. Xiao's circular singly linked list implementation, the last node's `right` pointer loops back to `self.head`.
```python
class Node:
    def __init__(self, val):
        self.value = val
        self.right = None
```
Write the complete method `addAtHead(self, val)` for `CircularLinkedList`. Ensure your method correctly handles both:
* Case 1: The list is currently empty (`self.head is None`).
* Case 2: The list has one or more existing nodes.

**Official Solution & Rubric:**
```python
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def addAtHead(self, val):
        new_node = Node(val)
        
        # Case 1: Empty list (4 pts)
        if not self.head:
            self.head = new_node
            new_node.right = new_node  # Points to itself in a 1-node circle
            return

        # Case 2: Non-empty list (6 pts)
        # Traverse to find the tail node (the node whose right pointer points to head)
        curr = self.head
        while curr.right != self.head:
            curr = curr.right

        # Rewire pointers
        new_node.right = self.head  # Step A: New head points to old head
        curr.right = new_node       # Step B: Tail points to new head
        self.head = new_node        # Step C: Update list head reference
```

---

### Question 9: Postfix Arithmetic Expression Evaluation with Stack Trace (12 Points)
**Exam Source Style:** CUNY Standard (Hunter CSCI 235 / City Tech CST 3650 / SET 2430)  
**Prompt:**  
Evaluate the following postfix expression using a stack:  
`8  4  2  /  +  5  *  3  -`  
Construct an explicit step-by-step trace table showing each token processed, the action taken, and the complete contents of the stack (bottom to top).

**Official Solution & Rubric:**
**Trace Table (10 pts):**

| Token Scanned | Token Type | Action Performed | Stack Contents (Bottom $\to$ Top) |
| :---: | :---: | :--- | :--- |
| **`8`** | Operand | Push `8` | `[8]` |
| **`4`** | Operand | Push `4` | `[8, 4]` |
| **`2`** | Operand | Push `2` | `[8, 4, 2]` |
| **`/`** | Operator | Pop `op2 = 2`, Pop `op1 = 4`. Compute $4 / 2 = 2$. Push `2`. | `[8, 2]` |
| **`+`** | Operator | Pop `op2 = 2`, Pop `op1 = 8`. Compute $8 + 2 = 10$. Push `10`. | `[10]` |
| **`5`** | Operand | Push `5` | `[10, 5]` |
| **`*`** | Operator | Pop `op2 = 5`, Pop `op1 = 10`. Compute $10 \times 5 = 50$. Push `50`. | `[50]` |
| **`3`** | Operand | Push `3` | `[50, 3]` |
| **`-`** | Operator | Pop `op2 = 3`, Pop `op1 = 50`. Compute $50 - 3 = 47$. Push `47`. | `[47]` |

* **Final Result (2 pts):** Pop the final remaining value: $\mathbf{47}$.  
*(Note on Subtraction Trap: $op1 - op2 = 50 - 3 = 47$. If calculated backwards as $3 - 50 = -47$, 4 points are deducted).*

---

### Question 10: Two-Stack Browser History Simulation (12 Points)
**Exam Source Style:** Prof. Xiao SET 2430 Assignment 5 Part A  
**Prompt:**  
A browser history navigation system is implemented using a current URL variable and two stacks: `back_stack` and `forward_stack`.
Trace the state of `self.curr`, `back_stack`, and `forward_stack` after each of the following sequential operations:
1. `browser = BrowserHistory("google.com")`
2. `browser.visit("youtube.com")`
3. `browser.visit("github.com")`
4. `browser.back(1)`
5. `browser.visit("reddit.com")`
6. `browser.forward(1)`

**Official Solution & Rubric:**
**State Trace Table (10 pts):**

| Step | Operation Executed | `self.curr` | `back_stack` (Bottom $\to$ Top) | `forward_stack` (Bottom $\to$ Top) | Return Value |
| :---: | :--- | :--- | :--- | :--- | :---: |
| 1 | `init("google.com")` | `"google.com"` | `[]` | `[]` | — |
| 2 | `visit("youtube.com")` | `"youtube.com"` | `["google.com"]` | `[]` | — |
| 3 | `visit("github.com")` | `"github.com"` | `["google.com", "youtube.com"]` | `[]` | — |
| 4 | `back(1)` | `"youtube.com"` | `["google.com"]` | `["github.com"]` | `"youtube.com"` |
| 5 | `visit("reddit.com")` | `"reddit.com"` | `["google.com", "youtube.com"]` | `[]` *(Cleared!)* | — |
| 6 | `forward(1)` | `"reddit.com"` | `["google.com", "youtube.com"]` | `[]` | `"reddit.com"` |

* **Key Concept Tested (2 pts):** In Step 5, calling `visit()` must **clear** `forward_stack`. Therefore, in Step 6, `forward(1)` has no forward history available and remains on `"reddit.com"`.

---

### Question 11: LIFO Stack Implemented Using Two Queues (12 Points)
**Exam Source Style:** Prof. Xiao SET 2430 Assignment 5 Part B / LeetCode 225  
**Prompt:**  
Explain the algorithmic strategy for implementing a LIFO Stack (`MyStack`) using only two FIFO Queues (`q1` and `q2`).
1. Write the code for `push(self, x)`.
2. Trace the contents of `q1` and `q2` during:
   * `push(10)`
   * `push(20)`
   * `pop()`

**Official Solution & Rubric:**
1. **Push Algorithm Code (6 pts):**
   ```python
   def push(self, x):
       # Step 1: Enqueue the new item into the empty auxiliary queue q2
       self.q2.enqueue(x)
       # Step 2: Transfer all existing items from q1 to q2 (behind x)
       while not self.q1.empty():
           self.q2.enqueue(self.q1.dequeue())
       # Step 3: Swap q1 and q2 so q1 always holds elements in LIFO order
       self.q1, self.q2 = self.q2, self.q1
   ```
2. **Trace of Queue States (6 pts):**
   * **`push(10)`:**
     * `q2.enqueue(10)` $\to q2 = [10]$.
     * `q1` is empty $\to$ nothing transferred.
     * Swap: `q1 = [10]`, `q2 = []`.
   * **`push(20)`:**
     * `q2.enqueue(20)` $\to q2 = [20]$.
     * Dequeue `10` from `q1` and enqueue to `q2` $\to q2 = [20, 10]$ *(20 is now at front!)*.
     * Swap: `q1 = [20, 10]`, `q2 = []`.
   * **`pop()`:**
     * Direct dequeue from `q1` $\to$ returns $\mathbf{20}$.
     * Remaining state: `q1 = [10]`. *(Correct LIFO behavior: 20 was pushed last and popped first!)*.

---

### Question 12: Handwritten Python Method with Complete Edge-Case Handling (15 Points)
**Exam Source Style:** CUNY Common Core Exam Question (All Campuses)  
**Prompt:**  
Given the following `SinglyLinkedList` definition:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
```
Write the complete method `delete_by_value(self, target)` that deletes the **first occurrence** of `target` from the linked list and decrements `self.size`. If `target` is not present, the method should return `False`; if successfully removed, return `True`.  
**Your code must explicitly handle:**
1. The list is empty.
2. The target is located at the `head` node.
3. The target is located in the middle or at the tail.
4. The target does not exist in the list.

**Official Solution & Rubric:**
```python
def delete_by_value(self, target):
    # Edge Case 1: Empty list (2 pts)
    if self.head is None:
        return False

    # Edge Case 2: Target is located at the head node (4 pts)
    if self.head.data == target:
        self.head = self.head.next
        self.size -= 1
        return True

    # Edge Case 3: Target in middle or tail (Requires predecessor tracking) (6 pts)
    prev = self.head
    curr = self.head.next

    while curr is not None:
        if curr.data == target:
            prev.next = curr.next  # Bypass curr
            self.size -= 1
            return True
        prev = curr
        curr = curr.next

    # Edge Case 4: Target not found after complete traversal (3 pts)
    return False
```
