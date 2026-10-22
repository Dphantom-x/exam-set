# SET 2430 — Week 6: Linear Structures (Arrays, Amortized Analysis, Linked Lists)

Prof. Haiying Xiao · Fall 2026

---

## 1. Asymptotic Notation Review & Extensions

### Standard Bounds
* **$O(g(n))$ — Upper Bound**: $f(n)$ grows *at most as fast as* $g(n)$ (can grow slower or same rate, but **NOT** faster).
  * Example: $3n + 5 = O(n)$ (linear growth dominates).
* **$\Omega(g(n))$ — Lower Bound**: $f(n)$ grows *at least as fast as* $g(n)$ (can grow same rate or faster, but **NOT** slower).
  * Example: $3n + 5 = \Omega(n)$.
* **$\Theta(g(n))$ — Tight Bound**: True when **BOTH** $f(n) = O(g(n))$ and $f(n) = \Omega(g(n))$ hold.
  * Example: $3n + 5 = \Theta(n)$ (exact same order of growth).

### Strict Growth Notations (Optional / Advanced)
* **Little-o ($o(g(n))$) — Strictly Smaller Growth**:
  * $f(n)$ grows strictly slower than $g(n)$.
  * Mathematical definition:
    $$\lim_{n \to \infty} \frac{f(n)}{g(n)} = 0$$
  * As $n$ becomes arbitrarily large, $f(n)$ is negligible compared to $g(n)$.
* **Little-$\omega$ ($\omega(g(n))$) — Strictly Faster Growth**:
  * $f(n)$ grows strictly faster than $g(n)$ ($\lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty$).

---

## 2. Growth Rate Hierarchy (Fastest to Slowest Efficiency)

Always rank algorithms using this reference hierarchy before selecting data structures:

| Notation | Name | Practical Efficiency |
| :--- | :--- | :--- |
| **$O(1)$** | Constant | Instant / Best possible |
| **$O(\log n)$** | Logarithmic | Extremely fast (e.g., Binary Search) |
| **$O(n)$** | Linear | Proportional to input size |
| **$O(n \log n)$** | Linearithmic | Standard optimal sorting (MergeSort, HeapSort) |
| **$O(n^2)$** | Quadratic | Slow on large $n$ (Nested loops, BubbleSort) |
| **$O(2^n)$** | Exponential | Impractical for medium/large $n$ (Recursive Fibonacci) |
| **$O(n!)$** | Factorial | Combinatorial explosion (Traveling Salesperson brute force) |

---

## 3. Amortized Analysis & Dynamic Arrays

### What is Amortized Analysis?
* **Definition**: Amortized analysis calculates the **average cost per operation over a worst-case sequence of operations**, rather than assessing an isolated single operation in isolation.
* **Why it matters**: Some operations are cheap almost all the time ($O(1)$) but occasionally require an expensive reorganization ($O(n)$). Worst-case analysis alone is misleadingly pessimistic.
* **Analogy**: Buying a car — monthly maintenance/gas is cheap ($O(1)$), but every few years you pay for a major transmission repair ($O(n)$). The **amortized cost** averaged across the entire vehicle life is small and constant.

### Python List Dynamic Resizing
In Python, lists are implemented as dynamically resizing array buffers (arrays of pointers):
1. Normal `append(x)` inserts at the next available allocated slot $\to \mathbf{O(1)}$.
2. When the allocated buffer is full:
   * A new, larger array buffer is allocated (typically doubling in size: $2n$).
   * All $n$ existing elements are copied to the new buffer $\to \mathbf{O(n)}$.
   * The internal pointer reference is updated to point to the new memory block.
   * The old buffer is reclaimed.

#### Operations and Costs Table (Doubling Strategy starting at capacity 2):
| Operation | Action | Capacity | Elements in Array | Cost |
| :--- | :--- | :--- | :--- | :--- |
| `append 1` | Insert into empty slot | 2 | 1 | 1 |
| `append 2` | Insert into empty slot | 2 | 2 (Full) | 1 |
| `append 3` | **Resize to 4**, copy 2 + insert 1 | 4 | 3 | $2 + 1 = 3$ |
| `append 4` | Insert into empty slot | 4 | 4 (Full) | 1 |
| `append 5` | **Resize to 8**, copy 4 + insert 1 | 8 | 5 | $4 + 1 = 5$ |

* **Total Cost for 5 Appends**: $1 + 1 + 3 + 1 + 5 = 11$ (or 8 with amortized accounting).
* **Average Cost**: $\approx 1.6 \text{ to } 2.2 \implies \mathbf{O(1) \text{ Amortized}}$.
* **Worst-Case Append**: $O(n)$ (on the specific append triggering a resize).
* **Amortized Append**: $\mathbf{O(1)}$.

### Memory Locality & Hardware Efficiency of Arrays
* **Contiguous Memory**: Array elements sit adjacent in RAM.
* **Cache-Friendly**: CPUs fetch contiguous memory cache lines (L1/L2 cache), making sequential array traversal significantly faster than pointer chasing across scattered heap allocations.

---

## 4. Linear Data Structures: Array-Based vs. Linked Lists

### The List Abstract Data Type (ADT)
An ADT specifies **WHAT** operations can be performed, not **HOW** they are stored internally in memory.

**Core List ADT Operations**:
* `get(i)`: Return value at index $i$.
* `set(i, x)`: Overwrite value at index $i$ with $x$.
* `insert(i, x)`: Insert value $x$ at index $i$, shifting subsequent elements right.
* `delete(i)`: Remove element at index $i$, shifting remaining elements left.
* `append(x)`: Add element $x$ to the end.
* `size()`: Return the number of elements.
* `isEmpty()`: Check if size is 0.

### Big-O Comparison Table: Array List vs. Linked List

| Operation | Array-Based List (Python `list`) | Linked List | Explanation |
| :--- | :---: | :---: | :--- |
| **Access by index `get(i)`** | $\mathbf{O(1)}$ | $O(n)$ | Arrays calculate `base + i * size`. Linked lists must traverse node by node. |
| **Insert at Head** | $O(n)$ | $\mathbf{O(1)}$ | Arrays must shift all $n$ items right. Linked list just rewires `head` pointer. |
| **Insert at Tail** | $\mathbf{O(1)}$ amortized | $\mathbf{O(1)}$ (with tail pointer) | Array appends to capacity. Linked list appends to `tail.next`. |
| **Insert in Middle** | $O(n)$ | $O(n)$ | Both take linear time (array shifts items; linked list must traverse to target). |
| **Delete from Head** | $O(n)$ | $\mathbf{O(1)}$ | Array shifts $n-1$ items left; linked list updates `head = head.next`. |
| **Delete from Middle/Tail** | $O(n)$ | $O(n)$ | Array shifts elements; linked list must traverse to predecessor node. |

---

## 5. Linked List Types

### A. Singly Linked List
Each node contains two fields:
1. `data`: The value stored.
2. `next`: Reference pointer to the next node in line (or `None`/`NULL` at end).

```
head
 ↓
[Data: A | next] ──> [Data: B | next] ──> [Data: C | next: None]
```

### B. Doubly Linked List
Each node contains three fields:
1. `data`: The value stored.
2. `next`: Pointer to the next node.
3. `prev`: Pointer to the preceding node.

```
None <── [prev | A | next] <══=> [prev | B | next] <══=> [prev | C | next] ──> None
```
* **Advantage**: Bidirectional traversal and $O(1)$ deletion when a node pointer is already known.

### C. Circular Linked List
In a circular linked list, the tail node points back to the `head` instead of `None`:
```
head
 ↓
[A] ──> [B] ──> [C]
 ↑               │
 └───────────────┘
```
* **Real-World Applications**:
  * Round-robin CPU process scheduling in Operating Systems.
  * Multiplayer game turn-rotation systems.
  * Music streaming repeat-playlist queues.

---

## 6. Stacks and Queues Preview (Transition into Week 7)

### Stacks (LIFO — Last In, First Out)
* **Rule**: Last element inserted is the first one removed (analogy: stack of plates).
* **Operations**:
  * `push(x)`: Add to top $\to O(1)$
  * `pop()`: Remove and return top item $\to O(1)$
  * `peek()` / `top()`: Inspect top item without removing $\to O(1)$
* **Constraint**: No random indexed access permitted.

### Queues (FIFO — First In, First Out)
* **Rule**: First element inserted is the first one removed (analogy: line at a ticket counter).
* **Operations**:
  * `enqueue(x)`: Add to rear $\to O(1)$
  * `dequeue()`: Remove and return front item $\to O(1)$
  * `front()` / `peek()`: Inspect front item $\to O(1)$
