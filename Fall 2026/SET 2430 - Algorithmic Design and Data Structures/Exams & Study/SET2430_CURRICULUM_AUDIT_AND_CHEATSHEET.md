# SET 2430: Master Curriculum Audit & Midterm Formula Cheat Sheet
**Course:** SET 2430 — Algorithmic Design and Data Structures  
**Institution:** New York City College of Technology (City Tech - CUNY)  
**Instructor:** Prof. Haiying Xiao | Fall 2026  
**Exam Target:** Midterm Exam (Weeks 1 to 7)  

---

## 1. Master Topic Matrix (Weeks 1 to 7)

| Week | Core Module | Specific Theoretical & Mathematical Concepts | Specific Implementations / Code Audited |
| :---: | :--- | :--- | :--- |
| **W1** | **Python Basics & ADTs** | ADT (Interface/What) vs. Data Structure (How). Type systems, variables, string formatting (`%`, `.format()`, f-strings), slices, loops. | Slide scripts, VS Code IDLE execution, input handling. |
| **W2** | **Python OOP & Collections** | Classes, `__init__`, instance vs class variables, `@property` getters/setters, `*args` tuple packing, `**kwargs` dict packing, file I/O context managers (`with open`). Java vs Python comparisons. | `Staff` class, `is_prime(n)` validation, `remove_adjacent_duplicates`, `disStuInfo` (Assignment 2). |
| **W3** | **Math Foundations & Summations** | Mathematical tools: sets, logarithms, arithmetic series (Gauss), sum of squares, geometric series, harmonic series. | `sum_loop(n)` ($O(n)$) vs `sum_formula(n)` ($O(1)$), `mystery(n)` loop counting (Assignment 3). |
| **W4** | **Algorithm Analysis (Part 1)** | Best, worst, average cases; Big-O ($O$), Big-Omega ($\Omega$), Big-Theta ($\Theta$). Growth hierarchy: $O(1) < \log n < n < n \log n < n^2 < 2^n < n!$. | Linear search comparison, count occurrences (linear $O(n)$ vs bisect $O(\log n)$), print pairs recursion. |
| **W5** | **Algorithm Analysis (Part 2) & Recurrence Relations** | Recurrence relations: Linear ($O(n)$), Divide & Conquer ($O(n \log n)$), Branching ($O(2^n)$). Step-by-step expansion method. Space complexity (Input vs Auxiliary vs Call Stack). | Solving $T(n) = 2T(n/2) + n \implies O(n \log n)$, `runningSum(nums)` space analysis, binary tree recursion intro (Assignment 4). |
| **W6** | **Linear Structures: Dynamic Arrays & Linked Lists** | Dynamic array resizing doubling strategy, amortized analysis $O(1)$ proof table, RAM contiguous locality vs heap pointer chasing. Singly Linked List operations. | List append timing benchmark, `SinglyLinkedList` (`addAtHead`, `append`, `deleteAtIndex`, `get`, `display`). |
| **W7** | **Circular/Doubly Lists, Stacks & Queues** | Circular Linked Lists (ring traversal), Doubly Linked Lists (`left` and `right` pointers), LIFO Stacks, FIFO Queues, ADT contracts. | `CircularLinkedList` (`addAtHead`, `print_list`), `DoublyLinkedList` (`append`, `addAtHead`, `get`, `print_forward`), `BrowserHistory` (2 stacks), `MyStack` (2 queues). |

---

## 2. Prof. Xiao's In-Class Conventions & Quirks

1. **Pointer Attribute Names in Class:**
   - Prof. Xiao uses **`right`** for the forward/next pointer in Circular Linked Lists and Doubly Linked Lists.
   - Prof. Xiao uses **`left`** for the backward/prev pointer in Doubly Linked Lists.
   - `self.value` or `self.val` is used for node payload.
   ```python
   # Xiao DoublyNode Convention:
   class DoublyNode:
       def __init__(self, val):
           self.value = val
           self.left = None   # prev
           self.right = None  # next
   ```
2. **Binary Tree Node Default Parameters:**
   - In Assignment 4, tree nodes are defined with defaults:
   ```python
   class Node:
       def __init__(self, val=0, left=None, right=None):
           self.val = val
           self.left = left
           self.right = right
   ```
3. **Structured 6-Step Recurrence Expansion:**
   - Prof. Xiao insists on explicit substitution steps (Step 1 equation $\to$ Step 2 substitute once $\to$ Step 3 substitute twice $\to$ Step 4 pattern at step $k$ $\to$ Step 5 base condition $k = \log_2 n$ $\to$ Step 6 Big-O evaluation).
4. **Amortized Doubling Accounting Table:**
   - Column layout: `| Operation | Action | Capacity | Elements in Array | Cost |`

---

## 3. Mathematical Formulas to Memorize Verbatim

### A. Summation Identities
1. **Gauss Arithmetic Summation:**
   $$\sum_{i=1}^n i = 1 + 2 + \dots + n = \frac{n(n + 1)}{2} = \frac{n^2 + n}{2} = \mathbf{\Theta(n^2)}$$
2. **Sum of Squares:**
   $$\sum_{i=1}^n i^2 = \frac{n(n + 1)(2n + 1)}{6} = \frac{2n^3 + 3n^2 + n}{6} = \mathbf{\Theta(n^3)}$$
3. **Geometric Series:**
   $$\sum_{j=0}^k 2^j = 2^{k+1} - 1 < 2 \cdot 2^k$$
   *(Used in proving that dynamic array doubling copy cost is $< 2N$, yielding amortized $O(1)$).*
4. **Harmonic Series:**
   $$\sum_{i=1}^n \frac{1}{i} \approx \ln n + 0.5772 \dots = \mathbf{\Theta(\log n)}$$

---

### B. Recurrence Expansion Derivations

#### 1. Divide-and-Conquer Recurrence: $T(n) = 2T(n/2) + n$, $T(1) = 1$
* **Step 1:** $T(n) = 2T(n/2) + n$
* **Step 2:** $T(n) = 2[2T(n/4) + n/2] + n = 4T(n/4) + 2n$
* **Step 3:** $T(n) = 4[2T(n/8) + n/4] + 2n = 8T(n/8) + 3n$
* **Step 4 (General $k$):** $T(n) = 2^k T(n/2^k) + k \cdot n$
* **Step 5 (Base case):** $n/2^k = 1 \implies 2^k = n \implies k = \log_2 n$
* **Step 6 (Closed form):** $T(n) = n \cdot T(1) + (\log_2 n) \cdot n = n + n \log_2 n = \mathbf{\Theta(n \log n)}$

#### 2. Tree Traversal Recurrence: $T(n) = 2T(n/2) + c$, $T(1) = c$
* **Step 1:** $T(n) = 2T(n/2) + c$
* **Step 2:** $T(n) = 2[2T(n/4) + c] + c = 4T(n/4) + 2c + c = 4T(n/4) + 3c$
* **Step 3:** $T(n) = 8T(n/8) + 7c$
* **Step 4 (General $k$):** $T(n) = 2^k T(n/2^k) + (2^k - 1)c$
* **Step 5 (Base case):** $2^k = n \implies k = \log_2 n$
* **Step 6 (Closed form):** $T(n) = n \cdot c + (n - 1)c = 2cn - c = \mathbf{\Theta(n)}$

#### 3. Linear Decrement Recurrence: $T(n) = T(n-1) + n$, $T(1) = 1$
* **Step 1:** $T(n) = T(n-1) + n$
* **Step 2:** $T(n) = [T(n-2) + (n-1)] + n = T(n-2) + (n-1) + n$
* **Step 3:** $T(n) = T(n-3) + (n-2) + (n-1) + n$
* **Step 4 (General $k$):** $T(n) = T(n-k) + \sum_{j=0}^{k-1} (n - j)$
* **Step 5 (Base case):** $n - k = 1 \implies k = n - 1$
* **Step 6 (Closed form):** $T(n) = T(1) + 2 + 3 + \dots + n = \sum_{i=1}^n i = \frac{n(n+1)}{2} = \mathbf{\Theta(n^2)}$

---

### C. Formal Asymptotic Limit Rules
* **$f(n) = O(g(n))$:** $\lim_{n \to \infty} \frac{f(n)}{g(n)} < \infty$ (finite non-negative constant or $0$).
* **$f(n) = \Omega(g(n))$:** $\lim_{n \to \infty} \frac{f(n)}{g(n)} > 0$ (positive constant or $\infty$).
* **$f(n) = \Theta(g(n))$:** $\lim_{n \to \infty} \frac{f(n)}{g(n)} = C$ where $0 < C < \infty$.
* **$f(n) = o(g(n))$:** $\lim_{n \to \infty} \frac{f(n)}{g(n)} = 0$ (strictly slower).
* **$f(n) = \omega(g(n))$:** $\lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty$ (strictly faster).

---

## 4. Master Data Structure Trade-Off Table

| Data Structure | Access by Index | Search by Value | Insert at Head | Insert at Tail | Delete Head | Delete Tail / Index | Space Overhead |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Python List (Dynamic Array)** | $\Theta(1)$ | $O(n)$ | $O(n)$ | $O(1)$ amortized | $O(n)$ | $O(1)$ (tail) / $O(n)$ (index) | Contiguous buffer with $2\times$ over-allocation |
| **Singly Linked List** | $O(n)$ | $O(n)$ | $\Theta(1)$ | $\Theta(1)$ with tail / $O(n)$ | $\Theta(1)$ | $O(n)$ (requires predecessor) | 1 pointer (`next`) per node |
| **Doubly Linked List** | $O(n)$ ($n/2$ split) | $O(n)$ | $\Theta(1)$ | $\Theta(1)$ | $\Theta(1)$ | $\Theta(1)$ if node reference given | 2 pointers (`left`, `right`) per node |
| **Circular Linked List** | $O(n)$ | $O(n)$ | $\Theta(1)$ with tail ref / $O(n)$ without | $\Theta(1)$ with tail ref / $O(n)$ | $\Theta(1)$ with tail ref / $O(n)$ | $O(n)$ | 1 pointer (`right` $\to$ `head`) |
| **Stack (LIFO)** | $\text{N/A}$ | $O(n)$ | $\Theta(1)$ `push` | $\text{N/A}$ | $\Theta(1)$ `pop` | $\text{N/A}$ | Array or single linked chain |
| **Queue (FIFO)** | $\text{N/A}$ | $O(n)$ | $\Theta(1)$ `enqueue` | $\text{N/A}$ | $\Theta(1)$ `dequeue` | $\text{N/A}$ | Linked list or circular array buffer |
