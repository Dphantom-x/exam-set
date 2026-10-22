# NEW YORK CITY COLLEGE OF TECHNOLOGY (CUNY)
## Department of Computer Engineering Technology / Computer Systems
### SET 2430: Algorithmic Design and Data Structures
#### MIDTERM EXAMINATION 2 (Advanced Variant & Edge-Case Specialist)

**Instructor:** Prof. Haiying Xiao  
**Semester:** Fall 2026  
**Exam Duration:** 75 – 90 Minutes  
**Total Points:** 100 Points  
**Format:** Closed Book, Closed Notes, **Strictly Paper-Based (No IDE, No Computer, No Scratch Shell)**

---

### STUDENT IDENTIFICATION:
- **Student Full Name:** ____________________________________________________
- **CUNY EmplID (8 Digits):** ________________________
- **Date:** ________________________
- **Seat / Room #:** ________________________

---

### INSTRUCTIONS TO CANDIDATES:
1. This is an **Advanced Diagnostic Exam**. It focuses heavily on subtle edge cases, mathematical limits, pointer destruction hazards, and manual memory mutation tracking.
2. In paper examinations, **omitting an edge-case guard (such as `None` or single-element checks) is considered a critical logic failure** because a program would crash immediately on execution.
3. Write cleanly. Clearly indicate indentation using bracketed tags `[indent]` or standard four-character margins.
4. For all pointer diagrams, clearly label node contents and draw directional arrowheads.

---

### SCORE SUMMARY TABLE (OFFICIAL USE ONLY)

| Section | Topic Description | Max Points | Earned Score | Grader Initials |
| :---: | :--- | :---: | :---: | :---: |
| **A** | Deceptive Conceptual Questions & Asymptotic Rigor | 20 | | |
| **B** | Advanced Code Tracing & Two-Stack History State Engine | 20 | | |
| **C** | Advanced Recurrence Expansion Proofs ($T(n-1)+n$ & $2T(n/2)+c$) | 20 | | |
| **D** | Pointer Mutation Ordering & Memory Hazard Diagrams | 15 | | |
| **E** | Advanced Handwritten Coding (Circular Deletion & 2-Queue Stack) | 25 | | |
| **TOTAL** | **Advanced Midterm Exam 2** | **100** | | |

---
\pagebreak

## SECTION A: Deceptive Conceptual Questions & Asymptotic Rigor (20 Points)

### Question A.1: Asymptotic Fallacies & Limits (6 Points)
Analyze each mathematical assertion below. Write **TRUE** or **FALSE**, followed by a rigorous 1-sentence justification using asymptotic limit definitions ($\lim_{n \to \infty} \frac{f(n)}{g(n)}$) or counterexamples.

**(a)** Assertion: $2^{n+1} = O(2^n)$. (2 pts)  
[ _____ ] Justification: __________________________________________________________________
__________________________________________________________________________________________

**(b)** Assertion: $2^{2n} = O(2^n)$. (2 pts)  
[ _____ ] Justification: __________________________________________________________________
__________________________________________________________________________________________

**(c)** Assertion: "If an algorithm's worst-case running time is $O(n^2)$, it is mathematically impossible for that algorithm to terminate in $O(1)$ time on any specific input." (2 pts)  
[ _____ ] Justification: __________________________________________________________________
__________________________________________________________________________________________

---

### Question A.2: Dynamic Array Resizing Trap: The $+K$ Strategy (7 Points)
Suppose an engineer attempts to optimize dynamic array resizing to conserve memory: instead of **doubling** capacity ($2 \times C$), they resize by adding a fixed constant $K = 1000$ slots whenever the array fills up.

**(a)** If we insert $N$ items into an initially empty array using this fixed increment strategy (where $N = m \cdot K$), how many total resizing/copy operations will be performed across all expansions? Express the total work as a summation. (3 pts)

```
SUMMATION DERIVATION:
Total Copies = K + 2K + 3K + ... + mK = 
```

**(b)** Evaluate the summation in closed form and state the resulting **amortized cost per append**. (2 pts)  
Closed-form sum = _________________________________  
Amortized cost per append = $\Theta($ ___________ $)$

**(c)** Hardware Realities: Why is geometric doubling ($2 \times C$) strictly superior to linear expansion ($+K$) for dynamic arrays? (2 pts)
```
ANSWER: __________________________________________________________________________________
__________________________________________________________________________________________
```

---

### Question A.3: Nested Loop Asymptotic Analysis (7 Points)
Determine the exact number of times the `print()` statement is executed, and derive the tight Big-$\Theta$ time complexity for the following code snippet:

```python
def tricky_loop(n):
    count = 0
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            print(i, j)
            count += 1
            j *= 2
        i += 1
    return count
```

**(a)** For a fixed value of the outer variable `i`, how many times does the inner `while j <= n:` loop execute? (2 pts)  
Inner loop executions per outer step = _________________________________

**(b)** What is the total number of print executions in terms of $n$? (2 pts)  
Total operations = _________________________________

**(c)** What is the tight asymptotic time complexity of `tricky_loop(n)`? (3 pts)  
Time Complexity = $\Theta($ _________________________________ $)$

---
\pagebreak

## SECTION B: Advanced Code Tracing & Memory Mutation Tracing (20 Points)

### Question B.1: Object Mutation, Scope & Variable Arguments Trace (10 Points)
Carefully trace the following Python program. Note how Python handles mutable object attributes versus local variable reassignments inside functions with `*args` and `**kwargs`.

```python
class NodeRef:
    def __init__(self, tag, val):
        self.tag = tag
        self.val = val

def mutate_network(lead, *nodes, **adjustments):
    lead.val += 10
    lead = NodeRef("LEAD_REBOUND", 999)  # Local re-binding
    
    for i, node in enumerate(nodes):
        node.val += adjustments.get(node.tag, 0)
        if node.val > 50:
            node.tag = node.tag + "_MAX"
            
    print(f"Inside lead.tag: {lead.tag}, lead.val: {lead.val}")

# Main execution:
n0 = NodeRef("ALPHA", 40)
n1 = NodeRef("BETA", 25)
n2 = NodeRef("GAMMA", 45)

adjust = {"BETA": 15, "GAMMA": 10, "ALPHA": 5}

mutate_network(n0, n1, n2, **adjust)

print(f"Outside n0: {n0.tag} = {n0.val}")
print(f"Outside n1: {n1.tag} = {n1.val}")
print(f"Outside n2: {n2.tag} = {n2.val}")
```

**(a) State Table of Objects (4 Points):**  
Fill in the exact final attribute values of `n0`, `n1`, and `n2` after the entire script completes:
- `n0.tag` = _____________________, `n0.val` = _________
- `n1.tag` = _____________________, `n1.val` = _________
- `n2.tag` = _____________________, `n2.val` = _________

**(b) Exact Console Printout (6 Points):**  
Write the four lines printed to the console in order:
```
Line 1: __________________________________________________________________________________
Line 2: __________________________________________________________________________________
Line 3: __________________________________________________________________________________
Line 4: __________________________________________________________________________________
```

---

### Question B.2: Two-Stack Browser History Engine Trace (10 Points)
In Assignment 5 Part A, you implemented `BrowserHistory(homepage)` using two stacks: `back_stack` and `fwd_stack`. Recall the exact logic:
- `visit(url)`: Push `curr` onto `back_stack`; update `curr = url`; **clear `fwd_stack` completely**.
- `back(steps)`: Move at most `steps` from `back_stack` to `fwd_stack`, setting `curr = back_stack.pop()`. Cannot go back past the earliest page.
- `forward(steps)`: Move at most `steps` from `fwd_stack` to `back_stack`, setting `curr = fwd_stack.pop()`. Cannot go forward past newest available forward page.

Trace the internal state of `curr`, `back_stack`, and `fwd_stack` through the following sequence. Represent stacks with the top of the stack on the right: `[bottom, ..., top]`.

| Step # | Method Call | `curr` URL | `back_stack` (Bottom to Top) | `fwd_stack` (Bottom to Top) | Method Return Value |
| :---: | :--- | :--- | :--- | :--- | :---: |
| 0 | `BrowserHistory("home.com")` | `"home.com"` | `[]` | `[]` | — |
| 1 | `visit("news.com")` | | | | — |
| 2 | `visit("sports.com")` | | | | — |
| 3 | `visit("tech.com")` | | | | — |
| 4 | `back(2)` | | | | |
| 5 | `visit("weather.com")` | | | | — |
| 6 | `forward(1)` | | | | |
| 7 | `back(5)` | | | | |

---
\pagebreak

## SECTION C: Advanced Recurrence Relations Expansion Proofs (20 Points)

### Question C.1: Linear Decrement Recurrence Proof (10 Points)
Consider the linear decrement recurrence relation:
$$T(n) = T(n-1) + n, \quad \text{for } n > 1, \quad \text{with base case } T(1) = 1$$
*(This recurrence arises in algorithms such as Recursive Selection Sort and QuickSort worst-case).*

Show the **complete, step-by-step algebraic expansion** to prove that $T(n) = \Theta(n^2)$.

**Step 1: Write the initial recurrence:**  
$$T(n) = T(n-1) + n$$

**Step 2: First substitution (substitute $T(n-1)$ into the equation):** (2 pts)
```
T(n) = [                                        ] + n
     = 
```

**Step 3: Second substitution (substitute $T(n-2)$ into the equation):** (2 pts)
```
T(n) = 
     = 
```

**Step 4: Express the general summation pattern after $k$ expansions:** (2 pts)
```
T(n) = T(n - k) + ________________________________________________________________________
```

**Step 5: Solve for the base case termination step $k$:** (2 pts)
```
We reach T(1) when n - k = 1  ===>  k = _______________
```

**Step 6: Substitute $k$ and apply Gauss's summation formula to find the tight bound:** (2 pts)
```
T(n) = 
     = 
Conclusion: T(n) = \Theta(                    )
```

---

### Question C.2: Binary Tree Traversal Recurrence with Constant Work (10 Points)
In Assignment 4 Part A, you analyzed counting nodes in a binary tree:
$$T(n) = 2T\left(\frac{n}{2}\right) + c, \quad \text{for } n > 1, \quad \text{with base case } T(1) = c$$
where $c$ is a positive constant representing $O(1)$ pointer comparison and addition work at each node. (Assume $n$ is a power of 2, $n = 2^m$).

**(a) Step-by-Step Expansion (6 Points):**
1. Initial: $T(n) = 2T(n/2) + c$
2. Substitute $T(n/2)$:
   $$T(n) = 2[2T(n/4) + c] + c = 4T(n/4) + 2c + c = 4T(n/4) + 3c$$
3. Substitute $T(n/4)$:
   $$T(n) = 4[2T(n/8) + c] + 3c = 8T(n/8) + 4c + 3c = 8T(n/8) + 7c$$
4. General pattern after $k$ expansions:
   $$T(n) = 2^k T(n/2^k) + c \cdot (2^k - 1)$$
5. Terminate at base case ($2^k = n \implies k = \log_2 n$):
   $$T(n) = n \cdot T(1) + c(n - 1)$$
   Substitute $T(1) = c$:
   $$T(n) = n(c) + cn - c = \mathbf{2cn - c}$$

**(b) The Critical Contrast (4 Points):**  
Why does the recurrence $T(n) = 2T(n/2) + c$ solve to **$\Theta(n)$**, whereas $T(n) = 2T(n/2) + n$ solves to **$\Theta(n \log_2 n)$**? Explain by analyzing where the bulk of the work is performed across the levels of the recursion tree.

```
ANSWER WORKSPACE:
__________________________________________________________________________________________
__________________________________________________________________________________________
__________________________________________________________________________________________
__________________________________________________________________________________________
```

---
\pagebreak

## SECTION D: Pointer Mutation Ordering & Memory Hazard Diagrams (15 Points)

### Question D.1: The Premature Head Reassignment Catastrophe (7 Points)
A student is writing the `addAtHead(val)` method for a **Circular Linked List** using Prof. Xiao's node convention (`self.value`, `self.right`):

```python
# Student's buggy attempt:
def addAtHead(self, val):
    new_node = Node(val)
    if not self.head:
        self.head = new_node
        new_node.right = new_node
        return
        
    self.head = new_node          # <-- LINE X (PREMATURE REASSIGNMENT!)
    
    curr = self.head
    while curr.right != self.head:
        curr = curr.right
        
    new_node.right = self.head
    curr.right = new_node
```

Suppose the list initially contains two nodes: `[10 | right] ──> [20 | right] ──> (back to 10)`.  
The student calls `addAtHead(5)`.

**(a) Memory Hazard Analysis (4 pts):**  
Trace what happens when the student's code executes starting at `LINE X`. Why does the `while curr.right != self.head:` loop immediately result in either a catastrophic infinite loop or a corrupt single-node cycle? Draw the memory diagram.

```
MEMORY HAZARD DIAGRAM:
```

**(b) Correct Pointer Sequence (3 pts):**  
Write down the exact 3-line pointer reassignment sequence that MUST be executed to insert `new_node` at the head of a circular list without breaking the ring:
```python
# Line 1: ________________________________________________________________________________
# Line 2: ________________________________________________________________________________
# Line 3: ________________________________________________________________________________
```

---

### Question D.2: In-Place Singly Linked List Reversal Diagram (8 Points)
Given the singly linked list:
$$\text{head} \longrightarrow [\,1\,|\,\bullet\,] \longrightarrow [\,2\,|\,\bullet\,] \longrightarrow [\,3\,|\,\text{None}\,]$$

We wish to reverse the list in-place using three pointers: `prev = None`, `curr = head`, and `next_node = None`.  
The core loop body is:
```python
next_node = curr.next    # Step 1
curr.next = prev         # Step 2
prev = curr              # Step 3
curr = next_node         # Step 4
```

**(a) Step-by-Step Diagram (6 pts):**  
Draw the memory state (showing all 3 nodes, their `next` pointers, and where `prev`, `curr`, and `next_node` point) **immediately after the first full iteration** (i.e. after processing node 1).

```
DIAGRAM SPACE AFTER ITERATION 1:
```

**(b) Hazard Explanation (2 pts):**  
Why is Step 1 (`next_node = curr.next`) strictly mandatory before Step 2 (`curr.next = prev`)? What specific memory consequence occurs if Step 2 is executed first?
```
ANSWER: __________________________________________________________________________________
__________________________________________________________________________________________
```

---
\pagebreak

## SECTION E: Advanced Handwritten Python Coding on Paper (25 Points)

> **STRICT PAPER CODING RULES:**
> - No IDE, no auto-complete, no syntax coloring.
> - Hand-indent clearly.
> - Full credit requires guarding against `None` references and handling single-node list transitions.

---

### Question E.1: Circular Linked List: `delete_node(self, target_val)` (12 Points)

Given Prof. Xiao's `CircularLinkedList` and `Node` classes:
```python
class Node:
    def __init__(self, val):
        self.value = val
        self.right = None  # Pointer to next node

class CircularLinkedList:
    def __init__(self):
        self.head = None
```

Write the method `delete_node(self, target_val)` on paper.  
**Requirements:**
1. Searches the circular list for the first node where `node.value == target_val`.
2. If found, unlinks the node, preserves the circular ring invariant, and returns `True`.
3. If not found or if the list is empty, returns `False` without entering an infinite loop!
4. **Must gracefully handle all edge cases:**
   - Empty list (`self.head is None`).
   - Single-node list whose value equals `target_val` (must set `self.head = None`).
   - Deleting the `head` node in a multi-node circular list (requires finding the tail node to update its `right` pointer to the new head!).
   - Deleting a middle or tail node.

```python
    def delete_node(self, target_val):
        # WRITE YOUR CODE CAREFULLY BELOW THIS LINE WITH ACCURATE INDENTATION:
```
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\

---
\pagebreak

### Question E.2: LIFO Stack Implemented with Two FIFO Queues (13 Points)

In Assignment 5 Part B, you implemented a LIFO Stack using two Queues. Assume a fully working `Queue` ADT is available with the following exact methods:
- `q.enqueue(val)`: Adds `val` to the rear of the queue.
- `q.dequeue()`: Removes and returns the front item. Returns `None` if queue is empty.
- `q.peek()`: Returns front item without removing. Returns `None` if queue is empty.
- `q.empty()`: Returns `True` if queue contains 0 items, `False` otherwise.

Implement the `MyStack` class below on paper such that:
- `push(self, x)` runs in **$O(n)$ time by shifting elements between `q1` and `q2`**, ensuring that `self.q1`'s front item is ALWAYS the most recently pushed item.
- `pop(self)` runs in **$O(1)$ time** and returns the top element (or `None` if stack is empty).
- `top(self)` runs in **$O(1)$ time** and returns the top element without removing (or `None` if empty).
- `is_empty(self)` returns `True` if empty, `False` otherwise.

```python
class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        # WRITE CODE FOR push(x):
```
\
\
\
\
\
\
\
\
\
```python
    def pop(self):
        # WRITE CODE FOR pop():
```
\
\
\
\
\
\
```python
    def top(self):
        # WRITE CODE FOR top():
```
\
\
\
\
\
\
```python
    def is_empty(self):
        # WRITE CODE FOR is_empty():
```
\
\

---
\pagebreak

## MASTER SOLUTIONS & GRADING RUBRICS (EXAM 2)

### Section A Solutions & Rubric (20 Points Total)

#### A.1 Solution: (6 Points, 2 pts each)
**(a) TRUE.**  
$2^{n+1} = 2^1 \cdot 2^n = 2 \cdot 2^n$. By definition of Big-O, choose $c = 2$ and $n_0 = 1$; then $2^{n+1} \le c \cdot 2^n$ holds for all $n \ge n_0$. (Or $\lim_{n \to \infty} \frac{2^{n+1}}{2^n} = 2 < \infty$).

**(b) FALSE.**  
$2^{2n} = (2^2)^n = 4^n$. Taking the limit: $\lim_{n \to \infty} \frac{2^{2n}}{2^n} = \lim_{n \to \infty} \frac{4^n}{2^n} = \lim_{n \to \infty} 2^n = \infty$. No constant $c$ can bound $4^n \le c \cdot 2^n$ as $n \to \infty$.

**(c) FALSE.**  
Big-O is an upper bound on the worst-case scenario. An algorithm with worst-case $O(n^2)$ (such as Insertion Sort or Linear Search) can terminate in $O(1)$ constant time on favorable best-case inputs (e.g. array is already sorted or target is at index 0).

#### A.2 Solution: (7 Points)
**(a)** (3 pts)  
Expansions occur after every $K$ items. At the $j$-th resize ($j = 1, 2, \dots, m$), there are $j \cdot K$ items in the array that must be copied:
$$\text{Total Copies} = K + 2K + 3K + \dots + mK = K \sum_{j=1}^m j$$

**(b)** (2 pts)  
Using Gauss's summation $\sum_{j=1}^m j = \frac{m(m+1)}{2}$:
$$\text{Total Copies} = K \cdot \frac{m(m+1)}{2} = \frac{K \cdot m^2 + K \cdot m}{2}$$
Since total elements $N = m \cdot K \implies m = N/K$:
$$\text{Total Copies} = K \cdot \frac{(N/K)^2}{2} = \frac{N^2}{2K} = \Theta(N^2)$$
Amortized cost per append = $\frac{\Theta(N^2)}{N} = \mathbf{\Theta(N)}$ (Linear amortized time!).

**(c)** (2 pts)  
Linear $+K$ expansion causes the total copying overhead to scale quadratically ($\Theta(N^2)$), degrading append to $O(N)$ amortized. Geometric doubling spreads resizing out exponentially, keeping total copy overhead bounded by $< 2N$, which guarantees **$O(1)$ amortized** performance.

#### A.3 Solution: (7 Points)
**(a)** (2 pts)  
The inner loop variable $j$ starts at 1 and doubles ($j = 1, 2, 4, 8, \dots$) until $j > n$.  
The number of iterations is $\lfloor \log_2 n \rfloor + 1$.

**(b)** (2 pts)  
The outer loop runs $n$ times ($i = 1, 2, \dots, n$).  
Total operations = $n \times (\lfloor \log_2 n \rfloor + 1) \approx \mathbf{n \log_2 n + n}$.

**(c)** (3 pts)  
$$\mathbf{\Theta(n \log_2 n)}$$

---

### Section B Solutions & Rubric (20 Points Total)

#### B.1 Solution: (10 Points)
**(a) Object Attribute State (4 pts):**
- `n0.tag` = **'ALPHA'**, `n0.val` = **50** (Passed as `lead`. `lead.val += 10` modified `n0.val` from 40 to 50. Reassigning `lead = NodeRef(...)` only changed the local variable, leaving `n0` unchanged in caller scope!).
- `n1.tag` = **'BETA'**, `n1.val` = **40** (`adjustments['BETA'] = 15`. `25 + 15 = 40`. Does not exceed 50, so tag is not updated).
- `n2.tag` = **'GAMMA_MAX'**, `n2.val` = **55** (`adjustments['GAMMA'] = 10`. `45 + 10 = 55`. Exceeds 50, so tag becomes `'GAMMA_MAX'`).

**(b) Console Output (6 pts):**
```
Inside lead.tag: LEAD_REBOUND, lead.val: 999
Outside n0: ALPHA = 50
Outside n1: BETA = 40
Outside n2: GAMMA_MAX = 55
```

#### B.2 Solution: (10 Points)
Trace Table:

| Step # | Method Call | `curr` URL | `back_stack` | `fwd_stack` | Return |
| :---: | :--- | :--- | :--- | :--- | :---: |
| 0 | `init("home.com")` | `"home.com"` | `[]` | `[]` | — |
| 1 | `visit("news.com")` | `"news.com"` | `["home.com"]` | `[]` | — |
| 2 | `visit("sports.com")` | `"sports.com"` | `["home.com", "news.com"]` | `[]` | — |
| 3 | `visit("tech.com")` | `"tech.com"` | `["home.com", "news.com", "sports.com"]` | `[]` | — |
| 4 | `back(2)` | `"news.com"` | `["home.com"]` | `["tech.com", "sports.com"]` | **"news.com"** |
| 5 | `visit("weather.com")` | `"weather.com"` | `["home.com", "news.com"]` | `[]` *(Cleared!)* | — |
| 6 | `forward(1)` | `"weather.com"` | `["home.com", "news.com"]` | `[]` *(Cannot move forward)* | **"weather.com"** |
| 7 | `back(5)` | `"home.com"` | `[]` *(Hits bottom)* | `["weather.com", "news.com"]` | **"home.com"** |

*Rubric:* 1 pt per correct row. 2 pts for correctly clearing `fwd_stack` on Step 5. 1 pt for clamping `back(5)` at the root `"home.com"`.

---

### Section C Solutions & Rubric (20 Points Total)

#### C.1 Solution: (10 Points)
- **Step 1:** $T(n) = T(n-1) + n$
- **Step 2 (2 pts):**
  $$T(n) = [T(n-2) + (n-1)] + n = T(n-2) + (n-1) + n$$
- **Step 3 (2 pts):**
  $$T(n) = [T(n-3) + (n-2)] + (n-1) + n = T(n-3) + (n-2) + (n-1) + n$$
- **Step 4 (2 pts):** General pattern after $k$ expansions:
  $$T(n) = T(n-k) + \sum_{j=0}^{k-1} (n - j)$$
- **Step 5 (2 pts):** Base case reached when $n - k = 1 \implies k = n - 1$.
- **Step 6 (2 pts):**
  $$T(n) = T(1) + \sum_{j=0}^{n-2} (n - j) = 1 + [2 + 3 + 4 + \dots + n] = \sum_{i=1}^n i$$
  Applying Gauss's formula:
  $$T(n) = \frac{n(n+1)}{2} = \frac{n^2 + n}{2} \implies \mathbf{\Theta(n^2)}$$

#### C.2 Solution: (10 Points)
**(a)** (6 pts): Algebraic expansion as detailed in question:
- Reaches $T(n) = 2cn - c$ at base case $k = \log_2 n$.
- Yields $\mathbf{\Theta(n)}$.

**(b)** (4 pts):
- In $T(n) = 2T(n/2) + c$, the non-recursive work per node is constant ($c$).
  - Level 0 has 1 node $\to c$ work.
  - Level 1 has 2 nodes $\to 2c$ work.
  - Level $k$ has $2^k$ nodes $\to 2^k c$ work.
  - This is a geometric series dominated entirely by the **leaves** at the bottom level ($2^{\log_2 n} = n$ leaves $\times c = O(n)$ total work).
- In $T(n) = 2T(n/2) + n$, the work per level is **equal at every level** ($2^k \times \frac{n}{2^k} = n$).
  - Since there are $\log_2 n$ levels and each level does $n$ work, total work is $n \times \log_2 n = \mathbf{\Theta(n \log_2 n)}$.

---

### Section D Solutions & Rubric (15 Points Total)

#### D.1 Solution: (7 Points)
**(a) Hazard Diagram (4 pts):**
```
Initial:  [ 10 | • ] ──> [ 20 | • ] ──> (back to 10)
LINE X executes: self.head = new_node (node 5)

Now self.head points to node 5!
Then: curr = self.head  ===> curr points to node 5!
Then: while curr.right != self.head:
```
Because `new_node.right` was initialized to `None`, evaluating `curr.right != self.head` compares `None != Node(5)` (True), and `curr = curr.right` sets `curr = None`.  
On the very next iteration, `curr.right` attempts `None.right`, causing an immediate **`AttributeError: 'NoneType' object has no attribute 'right'`** crash!  
Furthermore, all references to the original list `[10 -> 20]` were lost when `self.head` was overwritten!

**(b) Correct Sequence (3 pts):**
```python
# Assuming curr was navigated to the tail node (where curr.right == self.head):
new_node.right = self.head   # Line 1: Wire new_node to current head
curr.right = new_node        # Line 2: Wire tail to new_node
self.head = new_node         # Line 3: Finally update head
```

#### D.2 Solution: (8 Points)
**(a) Memory State after Iteration 1 (6 pts):**
```
prev                 curr / next_node
  ↓                         ↓
[ 1 | None ]           [ 2 | • ] ──> [ 3 | None ]
```
- Node 1's `next` pointer has been rewired backwards to `prev` (`None`).
- `prev` now points to Node 1.
- `curr` and `next_node` both point to Node 2.

**(b) Hazard Explanation (2 pts):**
If Step 2 (`curr.next = prev`) is executed before saving `curr.next`, the only pointer reference to Node 2 is destroyed. Once Node 1 points to `prev`, the remaining list `[2 -> 3]` is permanently **orphaned in memory**, making it impossible to advance `curr` to the next node!

---

### Section E Solutions & Rubric (25 Points Total)

#### E.1 Master Code Solution: `delete_node(self, target_val)` (12 Points)

```python
    def delete_node(self, target_val):
        # 1. Edge Case: Empty list
        if not self.head:
            return False

        # 2. Edge Case: Single-node list
        if self.head.right == self.head:
            if self.head.value == target_val:
                self.head = None
                return True
            return False

        # 3. Case: Deleting the head node in multi-node list
        if self.head.value == target_val:
            # Find the tail node (whose right pointer points to head)
            tail = self.head
            while tail.right != self.head:
                tail = tail.right
            # Bypass old head
            tail.right = self.head.right
            self.head = self.head.right
            return True

        # 4. Case: Deleting middle or tail node
        curr = self.head
        while curr.right != self.head:
            if curr.right.value == target_val:
                curr.right = curr.right.right
                return True
            curr = curr.right

        # 5. Target not found after complete cycle
        return False
```

**Grading Rubric for E.1:**
- **[+2 pts] Empty List Check:** Checks `if not self.head:` and returns `False`.
- **[+3 pts] Single-Node List:** Checks `self.head.right == self.head`, deletes sole node if matching, sets `self.head = None`, returns `True`.
- **[+4 pts] Multi-Node Head Deletion:** Traverses to find `tail`, updates `tail.right = self.head.right`, updates `self.head = self.head.right`.
- **[+2 pts] Middle/Tail Deletion:** Traverses with predecessor reference (`curr.right.value == target_val`) and unlinks node cleanly.
- **[+1 pt] Loop Termination:** Terminates loop cleanly when `curr.right == self.head` without looping indefinitely.

---

#### E.2 Master Code Solution: `MyStack` (Assignment 5 Part B) (13 Points)

```python
class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        # Enqueue new element into q2
        self.q2.enqueue(x)
        # Transfer all elements from q1 to q2 behind x
        while not self.q1.empty():
            self.q2.enqueue(self.q1.dequeue())
        # Swap q1 and q2 so q1 holds all elements in LIFO order
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.is_empty():
            return None
        return self.q1.dequeue()

    def top(self):
        if self.is_empty():
            return None
        return self.q1.peek()

    def is_empty(self):
        return self.q1.empty()
```

**Grading Rubric for E.2:**
- **[+5 pts] `push(x)` Implementation:**
  - Enqueues `x` into helper `q2` (+1 pt)
  - Transfers all items from `q1` to `q2` in loop (+2 pts)
  - Swaps `q1` and `q2` references (+2 pts)
- **[+3 pts] `pop()` Implementation:**
  - Checks if stack is empty; returns `None` (+1 pt)
  - Returns `self.q1.dequeue()` in $O(1)$ time (+2 pts)
- **[+3 pts] `top()` Implementation:**
  - Checks empty check (+1 pt)
  - Returns `self.q1.peek()` in $O(1)$ time (+2 pts)
- **[+2 pts] `is_empty()` Implementation:**
  - Returns `self.q1.empty()`.

---
\pagebreak

## "RED PEN ALERTS" & COMMON PAPER-EXAM BLUNDERS (EXAM 2)

1. **The Circular List Tail Bypass Blunder:**
   - When deleting the `head` in a circular linked list, simply doing `self.head = self.head.right` DOES NOT WORK. The `tail.right` pointer is still pointing to the OLD head! You MUST traverse to `tail` and update `tail.right = self.head.right`.
2. **Infinite Loops on Circular List Searches:**
   - In circular lists, writing `while curr is not None:` runs forever because `curr` will cycle endlessly. You MUST check `while curr.right != self.head:`.
3. **The `q1, q2 = q2, q1` Swap Omission:**
   - In the 2-queue stack, students often transfer items into `q2` but forget to swap references at the end of `push()`. On the next push, `q1` is empty and items get trapped in `q2`.
4. **Re-binding vs Mutating in Python Functions:**
   - Writing `lead = NodeRef(...)` inside a function ONLY overwrites the local pointer variable `lead`. It has ZERO effect on `n0` in the calling scope! Only attribute mutations (`lead.val = 50`) persist.
5. **Linear Array $+K$ Resizing Complexity:**
   - Never say "adding $K$ slots takes $O(1)$ amortized". Expanding by a constant increment means the sum of copies is $K \sum j = \Theta(N^2)$, yielding an disastrous $\Theta(N)$ amortized cost per append.
