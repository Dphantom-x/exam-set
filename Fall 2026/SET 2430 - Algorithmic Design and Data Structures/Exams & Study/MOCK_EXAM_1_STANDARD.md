# NEW YORK CITY COLLEGE OF TECHNOLOGY (CUNY)
## Department of Computer Engineering Technology / Computer Systems
### SET 2430: Algorithmic Design and Data Structures
#### MIDTERM EXAMINATION 1 (Standard Departmental Benchmark)

**Instructor:** Prof. Haiying Xiao  
**Semester:** Fall 2026  
**Exam Duration:** 75 – 90 Minutes  
**Total Points:** 100 Points  
**Format:** Closed Book, Closed Notes, **Strictly Paper-Based (No IDE, No Computer, No Calculator)**

---

### STUDENT IDENTIFICATION:
- **Student Full Name:** ____________________________________________________
- **CUNY EmplID (8 Digits):** ________________________
- **Date:** ________________________
- **Seat / Room #:** ________________________

---

### INSTRUCTIONS TO STUDENTS (READ CAREFULLY BEFORE WRITING):
1. **Paper-Only Environment:** All code and mathematical derivations must be written by hand in the designated boxed spaces. No external electronic devices, compilers, or interpreters are permitted.
2. **Indentation and Python Syntax:** Because Python is space-sensitive, you must **clearly indicate indentation levels**. We recommend using bracketed guides `[Indent]` or clear 4-space tab stops. Ambiguous indentation will be penalized.
3. **Pointers & Memory Diagrams:** In Section D, clearly distinguish between *pointer variables* (references) and *heap objects* (nodes). Draw arrowheads unambiguously pointing to the target node's boundary.
4. **Mathematical Derivations:** In Section C, you must write out all intermediate substitution steps. Skipping directly from the recurrence to Big-O without showing algebraic expansion will forfeit credit.
5. **Partial Credit:** Partial credit is awarded generously for sound algorithmic reasoning, provided your code/derivation handles major edge cases.

---

### SCORE SUMMARY TABLE (OFFICIAL USE ONLY)

| Section | Topic Description | Max Points | Earned Score | Grader Initials |
| :---: | :--- | :---: | :---: | :---: |
| **A** | Conceptual Definitions, ADTs & Asymptotic Notation Matching | 20 | | |
| **B** | Code Tracing & Output Determination without an IDE | 20 | | |
| **C** | Recurrence Expansion & Amortized Doubling Math Proofs | 20 | | |
| **D** | Box-and-Pointer Memory Diagrams & Reference Manipulation | 15 | | |
| **E** | Handwritten Python Coding on Paper (Edge-Case Defenses) | 25 | | |
| **TOTAL** | **Comprehensive Midterm Exam 1** | **100** | | |

---
\pagebreak

## SECTION A: Conceptual Definitions, ADTs & Asymptotic Matching (20 Points)

### Question A.1: Abstract Data Types (ADTs) vs. Concrete Data Structures (4 Points)
**(a)** In 1–2 sentences, define an **Abstract Data Type (ADT)** and contrast it with a **Concrete Data Structure**. (2 pts)  
```
ANSWER SPACE:
__________________________________________________________________________________________
__________________________________________________________________________________________
__________________________________________________________________________________________
```

**(b)** Identify whether each of the following is an **ADT** or a **Concrete Data Structure**: (2 pts)
1. Python Built-in `list`: ___________________________________
2. The `Stack` concept (`push`, `pop`, `peek`, `is_empty`): ___________________________________
3. Singly Linked List (`Node` with `data` and `next` pointer): ___________________________________
4. The `Queue` concept (`enqueue`, `dequeue`, `front`): ___________________________________

---

### Question A.2: Asymptotic Notations: Big-$O$, $\Omega$, and $\Theta$ (6 Points)
Match each mathematical property or statement on the left with the most accurate asymptotic bound on the right. Write the Roman numeral in the blank.

| Statement / Scenario | Asymptotic Bound |
| :--- | :--- |
| **(1)** Provides a guaranteed mathematical ceiling / upper bound on the worst-case running time: _____ | **(I)** Big-Omega ($\Omega$) |
| **(2)** Provides a guaranteed mathematical floor / lower bound on the best-case running time: _____ | **(II)** Big-Theta ($\Theta$) |
| **(3)** Established when an algorithm's upper bound and lower bound match asymptotically: _____ | **(III)** Big-O ($O$) |
| **(4)** The running time of Linear Search on an array of size $n$ when the target is at index 0: _____ | **(IV)** $\Omega(1)$ |
| **(5)** The running time of evaluating the Gauss formula $n(n+1)//2$: _____ | **(V)** $\Theta(1)$ |
| **(6)** The tight bound for nested loops executing $1 + 2 + \dots + n$ inner iterations: _____ | **(VI)** $\Theta(n^2)$ |

---

### Question A.3: Hardware Realities & CPU Cache Locality (5 Points)
Explain why iterating sequentially through an array of $1,000,000$ integers is significantly faster in wall-clock time than traversing a Singly Linked List of $1,000,000$ integers, despite both algorithms performing $O(n)$ operations. Mention **CPU cache lines**, **spatial locality**, and **RAM memory allocation**.

```
ANSWER SPACE (Explain clearly in 3-5 sentences):
__________________________________________________________________________________________
__________________________________________________________________________________________
__________________________________________________________________________________________
__________________________________________________________________________________________
__________________________________________________________________________________________
```

---

### Question A.4: Asymptotic Growth Hierarchy (5 Points)
Order the following 8 complexity functions from **slowest growing (most efficient)** to **fastest growing (least efficient)** as $n \to \infty$:
$$n^2, \quad 2^n, \quad 1000, \quad n \log_2 n, \quad \sqrt{n}, \quad n!, \quad n, \quad \log_2 n$$

```
ANSWER SPACE:
_______ < _______ < _______ < _______ < _______ < _______ < _______ < _______
(Slowest / Best)                                            (Fastest / Worst)
```

---
\pagebreak

## SECTION B: Code Tracing & Output Determination without an IDE (20 Points)

### Question B.1: OOP, Property Decorators & Variable Arguments Trace (10 Points)
Carefully read the following Python script (written following Prof. Xiao's Week 2 OOP and variable argument conventions). Without executing the code on a machine, determine the exact contents of the execution trace table and the exact console output.

```python
class Staff:
    company_name = 'ProgramLab'
    
    def __init__(self, pName, pPosition, pPay):
        self.name = pName
        self._position = pPosition
        self.pay = pPay
        
    @property
    def position(self):
        return self._position
        
    @position.setter
    def position(self, value):
        valid = ['Manager', 'Developer', 'Intern']
        if value in valid:
            self._position = value
        else:
            print(f"REJECTED: {value}")

def register_team(lead, *assistants, **department_meta):
    print(f"Lead: {lead.name} [{lead.position}]")
    print(f"Assistants Count: {len(assistants)}")
    for asst in assistants:
        print(f"-- Asst: {asst.name} -> {asst.position}")
    for k, v in department_meta.items():
        print(f"Meta {k}: {v}")

# Execution sequence:
emp1 = Staff("Alice", "Developer", 95000)
emp2 = Staff("Bob", "Intern", 45000)
emp3 = Staff("Charlie", "Contractor", 60000)

emp2.position = "Manager"
emp3.position = "Senior Contractor"

register_team(emp1, emp2, emp3, budget=150000, room="A412")
```

**(a) Property Setter Execution Trace (4 Points):**
Fill in the state of `_position` for each employee after the property assignments:
- `emp2._position` = ___________________________
- `emp3._position` = ___________________________

**(b) Exact Console Output (6 Points):**
Write the exact lines printed to the console in sequential order. Every character and newline counts!

```
CONSOlE OUTPUT LINES:
Line 1: __________________________________________________________________________________
Line 2: __________________________________________________________________________________
Line 3: __________________________________________________________________________________
Line 4: __________________________________________________________________________________
Line 5: __________________________________________________________________________________
Line 6: __________________________________________________________________________________
Line 7: __________________________________________________________________________________
Line 8: __________________________________________________________________________________
```

---

### Question B.2: Two-Queue Stack State Tracing (10 Points)
In Assignment 5, you implemented a LIFO `MyStack` using two FIFO queues (`q1` and `q2`). Recall that `q1` always holds the current stack elements with the newest element at the front. The algorithm for `push(x)` is:
1. `q2.enqueue(x)`
2. While `q1` is not empty: `q2.enqueue(q1.dequeue())`
3. Swap `q1` and `q2`

Assume `dequeue()` removes from index 0 (Front) and `enqueue(v)` adds to the end (Rear).  
Trace the exact contents of `q1` and `q2` after each operation in the sequence below. Represent queue contents as a list: `[Front, ..., Rear]`.

| Step # | Operation | `q2` during operation | `q1` after operation (Front to Rear) | Output of call (if any) |
| :---: | :--- | :--- | :--- | :---: |
| 0 | Initial State | `[]` | `[]` | — |
| 1 | `push(10)` | `[10]` $\to$ swap | `[10]` | — |
| 2 | `push(20)` | | | — |
| 3 | `push(30)` | | | — |
| 4 | `top()` | | | |
| 5 | `pop()` | | | |
| 6 | `push(40)` | | | — |
| 7 | `pop()` | | | |

---
\pagebreak

## SECTION C: Recurrence Expansion & Amortized Doubling Math Proofs (20 Points)

### Question C.1: Recurrence Relation Expansion Proof (10 Points)
Consider the divide-and-conquer recurrence relation:
$$T(n) = 2T\left(\frac{n}{2}\right) + n, \quad \text{for } n > 1, \quad \text{with base case } T(1) = 1$$
(Assume $n$ is an exact power of $2$, i.e., $n = 2^m$).

Show the **complete, step-by-step algebraic expansion** to prove that $T(n) = \Theta(n \log_2 n)$.

**Step 1: Write the initial recurrence:**  
$$T(n) = 2T(n/2) + n$$

**Step 2: First substitution (substitute $T(n/2)$ into the equation):** (2 pts)
```
T(n) = 2 [                                        ] + n
     = 
```

**Step 3: Second substitution (substitute $T(n/4)$ into the equation):** (2 pts)
```
T(n) = 
     = 
```

**Step 4: Express the general pattern after $k$ expansions:** (2 pts)
```
T(n) = ___________________________________________________________________________________
```

**Step 5: Solve for the base case termination step $k$:** (2 pts)
```
Set n / 2^k = 1  ===>  k = _______________
```

**Step 6: Substitute $k$ back into the general pattern and derive the closed-form Big-$\Theta$ bound:** (2 pts)
```
T(n) = 
     = 
Conclusion: T(n) = \Theta(                    )
```

---

### Question C.2: Dynamic Array Amortized Doubling Proof (10 Points)
A dynamic array begins with **Capacity = 1**. When an element is appended and the array is full, the array allocates a new buffer of **double the current capacity** ($2 \times C$), copies all existing $n$ elements to the new buffer ($n$ copy operations), and then inserts the new element ($1$ insert operation).

**(a) Operations Cost Table (5 Points):**  
Fill in the table for appending the first 8 elements into an initially empty dynamic array (Capacity = 1).

| Append # | Element Added | Old Capacity | Trigger Resize? (Yes/No) | New Capacity | Elements Copied | Total Cost (Copies + 1) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | $x_1$ | 1 | No | 1 | 0 | 1 |
| **2** | $x_2$ | 1 | **Yes** | 2 | 1 | 2 |
| **3** | $x_3$ | 2 | **Yes** | 4 | 2 | 3 |
| **4** | $x_4$ | 4 | No | 4 | 0 | 1 |
| **5** | $x_5$ | 4 | **Yes** | 8 | 4 | 5 |
| **6** | $x_6$ | 8 | No | 8 | 0 | 1 |
| **7** | $x_7$ | 8 | No | 8 | 0 | 1 |
| **8** | $x_8$ | 8 | No | 8 | 0 | 1 |

**Total Cost for 8 Appends = _______ operations.**  
**Average Cost per Append = _______ operations.**

**(b) General Mathematical Proof of Amortized $O(1)$ (5 Points):**  
Using the summation of powers of 2 ($\sum_{j=0}^{k-1} 2^j = 2^k - 1$), prove that for an arbitrary sequence of $N$ appends, the total work is bounded by $< 3N$, and therefore the amortized cost per append is $O(1)$.

```
PROOF WORKSPACE:
__________________________________________________________________________________________
__________________________________________________________________________________________
__________________________________________________________________________________________
__________________________________________________________________________________________
__________________________________________________________________________________________
__________________________________________________________________________________________
```

---
\pagebreak

## SECTION D: Box-and-Pointer Memory Diagrams (15 Points)

### Question D.1: Singly Linked List Insertion Diagram (7 Points)
Given the following singly linked list in memory:
$$\text{head} \longrightarrow [\,10\,|\,\bullet\,] \longrightarrow [\,20\,|\,\bullet\,] \longrightarrow [\,30\,|\,\text{None}\,]$$
Let pointer `curr` point to the node with value `10`.

We execute the following two lines of code to insert `Node(15)` immediately after `curr`:
```python
new_node = Node(15)
new_node.next = curr.next     # Line 1
curr.next = new_node          # Line 2
```

**(a) Diagram Line 1:** Draw the memory state after Line 1 executes, but BEFORE Line 2 executes. (3 pts)
```
DIAGRAM SPACE FOR LINE 1:
```

**(b) Diagram Line 2:** Draw the final memory state after Line 2 executes. (3 pts)
```
DIAGRAM SPACE FOR LINE 2:
```

**(c) Conceptual Trap (1 pt):** What would happen if the student accidentally reversed the order of execution to:
```python
curr.next = new_node          # Line A
new_node.next = curr.next     # Line B
```
Explain the fatal pointer consequence: ____________________________________________________

---

### Question D.2: Doubly Linked List Deletion Diagram (Prof. Xiao Convention) (8 Points)
In Prof. Xiao's Doubly Linked List, each node has:
- `value`
- `left` (reference to previous node)
- `right` (reference to next node)

Given the doubly linked list:
```
head ──> [None | 'A' | right] <===> [left | 'B' | right] <===> [left | 'C' | None] <── tail
```
Let pointer `target` reference the middle node with value `'B'`.

We execute the 4-line standard deletion routine:
```python
target.left.right = target.right   # Line 1
target.right.left = target.left   # Line 2
target.left = None                # Line 3 (Clean up)
target.right = None               # Line 4 (Clean up)
```

**(a) Draw the Box-and-Pointer Diagram** immediately after Lines 1 and 2 execute. Clearly show all `left` and `right` pointer arrows, including orphaned or bypassing references. (5 pts)

```
DIAGRAM SPACE:
```

**(b) State the Time Complexity** of deleting `target` when a direct reference to `target` is already provided:
Time Complexity = ______________ (1 pt)

**(c) Contrast with Singly Linked List:** Why can a Doubly Linked List delete `target` in $O(1)$ time given only `target`, whereas a Singly Linked List requires $O(n)$ time given only `target`? (2 pts)
```
ANSWER: __________________________________________________________________________________
__________________________________________________________________________________________
```

---
\pagebreak

## SECTION E: Handwritten Python Coding on Paper (25 Points)

> **PAPER CODING CONSTRAINTS:**
> - Write syntactically valid Python 3 code in the boxes provided.
> - Clearly align your indentation.
> - You may NOT use Python built-in lists, arrays, `append()`, `pop()`, or slicing inside linked list methods. You must manipulate pointer references (`next`, `left`, `right`, `head`, `tail`) directly.
> - You MUST handle all edge cases (empty list, single element, head modifications).

---

### Question E.1: Singly Linked List: `delete_by_value(self, target)` (12 Points)

Given the `Node` and `SinglyLinkedList` class definitions:
```python
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
```

Write the method `delete_by_value(self, target)` by hand on paper.  
**Specification:**
- Searches the list for the first node whose `data == target`.
- Removes that node from the list, properly preserving all pointer links.
- Decrements `self.size` by 1.
- Returns `True` if a node was found and removed.
- Returns `False` if `target` was not found or if the list is empty.
- **Edge cases to guard:**
  1. Empty list (`self.head is None`).
  2. Target is located at the `head` node (including single-node list).
  3. Target is in the middle or at the tail.
  4. Target does not exist in the list.

```python
    def delete_by_value(self, target):
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

---
\pagebreak

### Question E.2: Doubly Linked List: `insert_at_index(self, index, val)` (13 Points)

Given Prof. Xiao's `DoublyNode` and `DoublyLinkedList` definitions:
```python
class DoublyNode:
    def __init__(self, val):
        self.value = val
        self.left = None    # previous pointer
        self.right = None   # next pointer

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
```

Write the method `insert_at_index(self, index, val)` by hand on paper.  
**Specification:**
- Inserts a new node containing `val` at the specified 0-based `index`.
- If `index < 0` or `index > self.size`, return `False` (out-of-bounds invalid insertion).
- If `index == 0`, insert at the head. (Must correctly update `self.head` and `self.tail` if list was empty).
- If `index == self.size`, insert at the tail. (Must correctly update `self.tail`).
- Otherwise, traverse to `index` and insert the node between `curr.left` and `curr`. Update all 4 pointers (`left` and `right` for the new node, `right` of previous node, `left` of current node).
- Increment `self.size` by 1.
- Return `True` upon successful insertion.

```python
    def insert_at_index(self, index, val):
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

## MASTER SOLUTIONS & GRADING RUBRICS (EXAM 1)

### Section A Solutions & Rubric (20 Points Total)

#### A.1 Solution:
**(a)** (2 pts)
- An **Abstract Data Type (ADT)** is a high-level mathematical specification of a data structure that defines **WHAT** operations can be performed and what behaviors they exhibit, without dictating how they are stored or implemented in memory.
- A **Concrete Data Structure** is an actual physical implementation in code/memory that defines **HOW** data is stored (e.g. contiguous RAM addresses vs pointers on heap).
- *Rubric:* 1 pt for ADT definition (interface / what), 1 pt for concrete data structure (implementation / how).

**(b)** (2 pts, 0.5 pt each)
1. Python Built-in `list`: **Concrete Data Structure** (specifically, a dynamic array of pointers).
2. The `Stack` concept: **ADT** (specifies LIFO operations: `push`, `pop`, `peek`).
3. Singly Linked List: **Concrete Data Structure** (specific node objects linked by pointers).
4. The `Queue` concept: **ADT** (specifies FIFO operations: `enqueue`, `dequeue`).

#### A.2 Solution: (6 pts, 1 pt each)
1. **(III)** Big-O ($O$) — Guaranteed upper bound ceiling.
2. **(I)** Big-Omega ($\Omega$) — Guaranteed lower bound floor.
3. **(II)** Big-Theta ($\Theta$) — Tight bound when upper and lower match.
4. **(IV)** $\Omega(1)$ (or $\Theta(1)$ / $O(1)$ best-case) — Target at index 0 takes 1 step.
5. **(V)** $\Theta(1)$ — Gauss closed formula executes in constant arithmetic time.
6. **(VI)** $\Theta(n^2)$ — Triangular sum $\sum_{i=1}^n i = \frac{n(n+1)}{2} = \Theta(n^2)$.

#### A.3 Solution: (5 pts)
- **Memory Layout:** Array elements occupy a single **contiguous block** of physical memory, whereas linked list nodes are dynamically allocated at arbitrary, scattered heap addresses. (1.5 pts)
- **CPU Cache Lines & Locality:** When the CPU reads an array element from RAM, hardware pre-fetching loads an entire 64-byte **cache line** containing adjacent elements into ultra-fast L1/L2 cache (high **spatial locality**), resulting in frequent **cache hits**. (2 pts)
- **Pointer Chasing & Cache Misses:** For linked lists, every traversal step requires dereferencing a pointer to an unknown memory location, causing frequent **cache misses** that force the CPU to stall while fetching each node from slow main RAM. (1.5 pts)

#### A.4 Solution: (5 pts)
$$1000 < \log_2 n < \sqrt{n} < n < n \log_2 n < n^2 < 2^n < n!$$
- *Rubric:* 5 pts for completely correct order. Deduct 1 pt per inversion/swap.

---

### Section B Solutions & Rubric (20 Points Total)

#### B.1 Solution: (10 Points)
**(a) Trace Table (4 pts, 2 pts each):**
- `emp2._position`: **'Manager'** (Valid input according to setter list `['Manager', 'Developer', 'Intern']`).
- `emp3._position`: **'Contractor'** (Rejected by setter because `'Senior Contractor'` is not in the valid list; setter prints error and leaves existing `_position` unchanged!).

**(b) Console Output (6 pts, 1 pt per correct block/line):**
```
REJECTED: Senior Contractor
Lead: Alice [Developer]
Assistants Count: 2
-- Asst: Bob -> Manager
-- Asst: Charlie -> Contractor
Meta budget: 150000
Meta room: A412
```
*Note on Line 1:* When `emp3.position = "Senior Contractor"` runs, the setter executes `print(f"REJECTED: {value}")` BEFORE `register_team()` is called!

#### B.2 Solution: (10 Points)
Trace Table:

| Step # | Operation | `q2` during operation | `q1` after operation (Front to Rear) | Output |
| :---: | :--- | :--- | :--- | :---: |
| 0 | Initial | `[]` | `[]` | — |
| 1 | `push(10)` | Enqueue 10 $\to$ `[10]`, swap | `[10]` | — |
| 2 | `push(20)` | Enqueue 20 $\to$ `[20]`, dequeue 10 from `q1` into `q2` $\to$ `[20, 10]`, swap | `[20, 10]` | — |
| 3 | `push(30)` | Enqueue 30 $\to$ `[30]`, transfer `q1` $\to$ `[30, 20, 10]`, swap | `[30, 20, 10]` | — |
| 4 | `top()` | Peek at `q1[0]` | `[30, 20, 10]` | **30** |
| 5 | `pop()` | `q1.dequeue()` removes index 0 | `[20, 10]` | **30** |
| 6 | `push(40)` | Enqueue 40 $\to$ `[40]`, transfer `q1` $\to$ `[40, 20, 10]`, swap | `[40, 20, 10]` | — |
| 7 | `pop()` | `q1.dequeue()` removes index 0 | `[20, 10]` | **40** |

*Rubric:* 1 pt per step correctly traced. 2 pts for recognizing LIFO retrieval from front of `q1`.

---

### Section C Solutions & Rubric (20 Points Total)

#### C.1 Solution: (10 Points)
- **Step 1:** $T(n) = 2T(n/2) + n$
- **Step 2 (2 pts):**
  $$T(n) = 2\left[2T\left(\frac{n}{4}\right) + \frac{n}{2}\right] + n = 4T\left(\frac{n}{4}\right) + n + n = 4T\left(\frac{n}{4}\right) + 2n$$
- **Step 3 (2 pts):**
  $$T(n) = 4\left[2T\left(\frac{n}{8}\right) + \frac{n}{4}\right] + 2n = 8T\left(\frac{n}{8}\right) + n + 2n = 8T\left(\frac{n}{8}\right) + 3n$$
- **Step 4 (2 pts):** General pattern after $k$ steps:
  $$T(n) = 2^k T\left(\frac{n}{2^k}\right) + k \cdot n$$
- **Step 5 (2 pts):** Base case condition:
  $$\frac{n}{2^k} = 1 \implies 2^k = n \implies k = \log_2 n$$
- **Step 6 (2 pts):** Substitute $k = \log_2 n$ and $2^k = n$:
  $$T(n) = n \cdot T(1) + (\log_2 n) \cdot n = n(1) + n \log_2 n = n + n \log_2 n$$
  $$\mathbf{T(n) = \Theta(n \log_2 n)}$$

#### C.2 Solution: (10 Points)
**(a) Table (5 pts, full credit if costs match):**
- Total Cost = $1 + 2 + 3 + 1 + 5 + 1 + 1 + 1 = \mathbf{15\text{ operations}}$.
- Average Cost = $15 / 8 = \mathbf{1.875\text{ operations per append}}$.

**(b) Math Proof (5 pts):**
- Let $N$ appends be executed. Each append does 1 basic insertion $\implies N$ insertions total. (1 pt)
- Resizing occurs when capacity $2^j$ is exceeded ($j = 0, 1, 2, \dots, k-1$, where $2^k$ is the smallest power of 2 $\ge N$). (1 pt)
- The copy cost incurred at step $j$ is $2^j$. Sum of all copy costs:
  $$\text{Total Copies} = \sum_{j=0}^{k-1} 2^j = 2^0 + 2^1 + 2^2 + \dots + 2^{k-1} = 2^k - 1$$ (2 pts)
- Since $2^{k-1} < N \implies 2^k < 2N$, we have:
  $$\text{Total Cost} = \text{Insertions} + \text{Copies} = N + (2^k - 1) < N + 2N = 3N$$
- Amortized cost per operation:
  $$\text{Amortized Cost} = \frac{\text{Total Cost}}{N} < \frac{3N}{N} = 3 = \mathbf{O(1)}$$ (1 pt)

---

### Section D Solutions & Rubric (15 Points Total)

#### D.1 Solution: (7 Points)
**(a) Diagram Line 1 (3 pts):**
```
curr
  ↓
[ 10 | • ] ─────────────> [ 20 | • ] ──> [ 30 | None ]
                           ▲
new_node                   │
  ↓                        │
[ 15 | • ] ────────────────┘
```
*Key:* `curr.next` still points to 20! `new_node.next` now ALSO points to 20.

**(b) Diagram Line 2 (3 pts):**
```
curr                      new_node
  ↓                         ↓
[ 10 | • ] ─────────────> [ 15 | • ] ──> [ 20 | • ] ──> [ 30 | None ]
```
*Key:* `curr.next` is rewired to point to `new_node`. The list is now cleanly `10 -> 15 -> 20 -> 30`.

**(c) Trap (1 pt):**
If `curr.next = new_node` is executed first, `curr.next` overwrites the pointer to node `20`. When `new_node.next = curr.next` runs next, it sets `new_node.next = new_node`, creating an **infinite 1-node self-cycle**, while permanently **orphaning / leaking nodes 20 and 30** in memory!

#### D.2 Solution: (8 Points)
**(a) Diagram (5 pts):**
```
head                                                           tail
 ↓                                                               ↓
[None | 'A' | right] ───────────────────────────> [left | 'C' | None]
         ▲                                           │
         │                                           │
         └───────────────────────────────────────────┘
                       target
                         ↓
               [left | 'B' | right]
               (Orphaned from the main list chain)
```
- Line 1 (`target.left.right = target.right`): Sets `A.right = C`.
- Line 2 (`target.right.left = target.left`): Sets `C.left = A`.
- Lines 3 & 4: Clear `target.left` and `target.right` to `None`.

**(b) Time Complexity (1 pt):** $\mathbf{O(1)}$ (Constant time).

**(c) Contrast (2 pts):**
In a Doubly Linked List, `target` has a direct backward reference `target.left` to its predecessor node. In a Singly Linked List, nodes only point forward; to delete `target`, an algorithm must traverse from `head` all the way to `target`'s predecessor ($O(n)$ steps) to rewire `prev.next = target.next`.

---

### Section E Solutions & Rubric (25 Points Total)

#### E.1 Master Code Solution: `delete_by_value(self, target)` (12 Points)

```python
    def delete_by_value(self, target):
        # 1. Edge Case: Empty list
        if self.head is None:
            return False

        # 2. Edge Case: Target is at the head node
        if self.head.data == target:
            self.head = self.head.next
            self.size -= 1
            return True

        # 3. Target is in middle or tail: Traverse with predecessor pointer
        curr = self.head
        while curr.next is not None:
            if curr.next.data == target:
                curr.next = curr.next.next  # Rewire pointer past target
                self.size -= 1
                return True
            curr = curr.next

        # 4. Target not found
        return False
```

**Grading Rubric for E.1:**
- **[+2 pts] Empty List Check:** Checks `if self.head is None` and returns `False`.
- **[+4 pts] Head Node Match:** Checks `if self.head.data == target`, updates `self.head = self.head.next`, decrements `size`, and returns `True`.
- **[+4 pts] Traversal & Pointer Rewiring:** Correct `while curr.next:` traversal; accurately rewires `curr.next = curr.next.next` on match without losing subsequent nodes.
- **[+1 pt] Size Decrement:** Correctly decrements `self.size` on successful deletion.
- **[+1 pt] Not Found Return:** Returns `False` when target does not exist.
- **Common Penalties:**
  - `-3 pts:` Infinite loop (e.g. forgot `curr = curr.next` inside loop).
  - `-3 pts:` Crashed on empty list (`AttributeError: 'NoneType' object has no attribute 'data'`).
  - `-2 pts:` Replaced `curr.next = curr.next.next` with `curr = curr.next` (didn't delete).
  - `-2 pts:` Major indentation ambiguity.

---

#### E.2 Master Code Solution: `insert_at_index(self, index, val)` (13 Points)

```python
    def insert_at_index(self, index, val):
        # 1. Bounds check
        if index < 0 or index > self.size:
            return False

        new_node = DoublyNode(val)

        # 2. Case: Insert at head (index == 0)
        if index == 0:
            if self.head is None:  # List was empty
                self.head = self.tail = new_node
            else:
                new_node.right = self.head
                self.head.left = new_node
                self.head = new_node
            self.size += 1
            return True

        # 3. Case: Insert at tail (index == self.size)
        if index == self.size:
            self.tail.right = new_node
            new_node.left = self.tail
            self.tail = new_node
            self.size += 1
            return True

        # 4. Case: Insert in middle (0 < index < self.size)
        curr = self.head
        for _ in range(index):
            curr = curr.right

        # curr is now at the position where new_node will be placed
        prev_node = curr.left

        # Wire new_node pointers
        new_node.right = curr
        new_node.left = prev_node

        # Rewire surrounding pointers
        prev_node.right = new_node
        curr.left = new_node

        self.size += 1
        return True
```

**Grading Rubric for E.2:**
- **[+2 pts] Boundary Validation:** Checks `index < 0 or index > self.size` and returns `False`.
- **[+3 pts] Insert at Head:** Handles `index == 0`. Handles both empty list (`self.head = self.tail = new_node`) and non-empty list (`new_node.right = self.head`, `self.head.left = new_node`, `self.head = new_node`).
- **[+3 pts] Insert at Tail:** Handles `index == self.size`. Correctly links `self.tail.right = new_node`, `new_node.left = self.tail`, `self.tail = new_node`.
- **[+4 pts] Middle Insertion (4 Pointers):** Correctly traverses to target node and accurately rewires all 4 pointers (`new_node.right`, `new_node.left`, `prev_node.right`, `curr.left`).
- **[+1 pt] Size & Return:** Increments `self.size += 1` and returns `True`.
- **Common Penalties:**
  - `-3 pts:` Forgetting to update `self.tail` when inserting into empty list or at end.
  - `-3 pts:` Overwriting pointers in wrong order resulting in disconnected node.
  - `-2 pts:` Missing `None` checks causing crash on empty list.
  - `-2 pts:` Indentation failure.

---
\pagebreak

## "RED PEN ALERTS" & COMMON PAPER-EXAM BLUNDERS (EXAM 1)

1. **The "Virtual Python Terminal" Hallucination:**
   - On paper, there is no traceback error to warn you that `curr.next.next` crashes when `curr.next` is `None`. Always check `while curr.next:` before accessing `curr.next.next`!
2. **The "Pointer Overwrite Amnesia":**
   - Students frequently write:
     ```python
     curr.next = new_node
     new_node.next = curr.next  # ERROR: curr.next is ALREADY new_node!
     ```
   - *Rule:* Always save or link downstream references BEFORE breaking upstream links.
3. **The "Sole Node Oblivion" in Doubly Linked Lists:**
   - When inserting into an empty doubly linked list, many students set `self.head = new_node` but forget `self.tail = new_node`. Subsequent `append()` calls immediately crash.
4. **Indentation Shifts:**
   - In Python on paper, writing a `return False` aligned under an `if` block instead of outside a `while` loop terminates the loop prematurely on iteration 1.
5. **Recurrence General Pattern Guesswork:**
   - Do NOT jump directly from Step 2 to Step $k$. Show Step 3 explicitly ($4T(n/4) + 2n \to 8T(n/8) + 3n$). This proves the coefficients $2^k$ and $k \cdot n$.
