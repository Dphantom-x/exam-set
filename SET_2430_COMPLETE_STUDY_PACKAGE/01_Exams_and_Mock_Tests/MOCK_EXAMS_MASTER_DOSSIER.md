# SET 2430 — MIDTERM MOCK EXAMINATIONS DOSSIER
## Algorithmic Design and Data Structures | Prof. Haiying Xiao (City Tech / CUNY)

---

### Dossier Overview
This repository contains two complete, authentic, 100-point Midterm Examinations for **SET 2430 (Algorithmic Design and Data Structures)**, engineered specifically for the paper-and-pencil examination environment where **no IDE, terminal, compiler, or calculator is available**.

The exams mirror the exact syllabus, lecture slides, Python OOP conventions, and homework assignments (Assignments 1–5) taught by **Prof. Haiying Xiao** through Weeks 1–7.

---

### Files in this Examination Suite
1. **[MOCK_EXAM_1_STANDARD.md](file:///c:/Users/aldom/Desktop/antigravity/degree/Fall%202026/SET%202430%20-%20Algorithmic%20Design%20and%20Data%20Structures/Exams%20%26%20Study/MOCK_EXAM_1_STANDARD.md)**
   - **Type:** Standard Departmental Benchmark Exam (100 Points, 75–90 Minutes)
   - **Target Audience:** Baseline mastery across all departmental topics.
   - **Focus:** Foundational ADT concepts, standard $T(n) = 2T(n/2) + n$ recurrence expansion, doubling array amortized analysis ($O(1)$), box-and-pointer memory diagrams, singly linked list deletion, and doubly linked list index insertion.
2. **[MOCK_EXAM_2_ADVANCED.md](file:///c:/Users/aldom/Desktop/antigravity/degree/Fall%202026/SET%202430%20-%20Algorithmic%20Design%20and%20Data%20Structures/Exams%20%26%20Study/MOCK_EXAM_2_ADVANCED.md)**
   - **Type:** Advanced Variant & Edge-Case Heavy Exam (100 Points, 75–90 Minutes)
   - **Target Audience:** High-scoring preparation and rigorous edge-case defense.
   - **Focus:** Deceptive asymptotic assertions, $+K$ linear resizing trap ($O(n)$ amortized!), two-stack browser history state engine tracing, $T(n) = T(n-1) + n$ vs $T(n) = 2T(n/2) + c$ expansions, premature pointer overwriting hazard, in-place reversal diagrams, circular linked list deletion, and 2-queue stack synthesis.

---

### Topic & Syllabus Mapping Matrix (Weeks 1 to 7)

| Week | Syllabus & Lecture Topic | Tested in Exam 1 | Tested in Exam 2 |
| :---: | :--- | :--- | :--- |
| **Week 1** | Python Review, ADTs vs Concrete Data Structures | Q A.1 (ADT vs Concrete Data Structure definitions & matching) | Q A.1 (Asymptotic limits, memory references) |
| **Week 2** | OOP in Python, `__init__`, `@property`, `@setter`, `*args`, `**kwargs` | Q B.1 (Trace of Staff class with property setter and `*args`/`**kwargs`) | Q B.1 (Object reference mutation vs local scope rebinding) |
| **Week 3** | Math Foundations, Summations ($\sum i$), Geometric series | Q A.2 (Gauss formula), Q C.2 (Geometric series for doubling) | Q A.2 (Gauss sum for $+K$ resize), Q C.1 (Gauss sum for $T(n-1)+n$) |
| **Week 4** | Algorithm Analysis (Part 1), Big-$O$, Best/Worst/Avg, Growth Hierarchy | Q A.2, Q A.4 (8-tier Growth hierarchy ranking) | Q A.1 (Deceptive Big-$O$ claims, worst vs best-case) |
| **Week 5** | Algorithm Analysis (Part 2), Lower bounds ($\Omega$), Tight bounds ($\Theta$), $T(n) = 2T(n/2) + n$ | Q C.1 (Full step-by-step expansion of $2T(n/2) + n$) | Q A.3 (Logarithmic nested loop $\Theta(n \log n)$), Q C.2 ($2T(n/2) + c$) |
| **Week 6** | Dynamic Arrays, Amortized $O(1)$, Singly Linked Lists, CPU Cache Locality | Q A.3 (RAM cache lines), Q C.2 (8-step doubling table), Q D.1, Q E.1 (`delete_by_value`) | Q A.2 (Proof of $+K$ failure), Q D.2 (In-place reversal diagram) |
| **Week 7** | Circular & Doubly Linked Lists (`val`, `left`, `right`), Stacks & Queues, Assignment 5 | Q B.2 (2-queue trace), Q D.2 (Doubly deletion diagram), Q E.2 (`insert_at_index`) | Q B.2 (2-stack browser history trace), Q D.1 (Circular hazard), Q E.1 (Circular deletion), Q E.2 (2-queue stack code) |

---

### The Paper-Test Survival Protocol (Crucial Rules for Taking CS Exams Without an IDE)

1. **Explicit Indentation Signaling:**
   - In Python, indentation defines block scope. On paper, sloppy handwriting can make it ambiguous whether `return False` is inside or outside a `while` loop.
   - *Strategy:* Always indent four distinct character widths or draw a subtle vertical guideline marking indentation blocks.

2. **The "Pointer Preservation" Rule (Save Before You Sever):**
   - Whenever you are rewiring pointers in a linked list (singly, doubly, or circular), you must NEVER overwrite a pointer if it is your only route to downstream nodes.
   - *Example:* Always write `next_node = curr.next` BEFORE assigning `curr.next = prev`.

3. **Check the Four Critical Linked List Edge Cases Before Submitting:**
   - Case 1: **Empty List** (`head is None`) $\to$ Does your code return immediately or crash with `AttributeError`?
   - Case 2: **Single-Element List** (`head.next is None` or `head.right == head`) $\to$ Does deleting or inserting properly update both `head` and `tail`?
   - Case 3: **Target at Head** $\to$ Does your code advance `head = head.next` (and in circular lists, rewire `tail.right`)?
   - Case 4: **Target Absent / Loop Termination** $\to$ In circular lists, does your loop exit cleanly when `curr.right == self.head`, or does it loop infinitely?

4. **Showing Work on Recurrences:**
   - Departmental graders deduct up to 50% of the points if you write the correct answer $\Theta(n \log n)$ without writing out Step 2, Step 3, the Step $k$ general pattern, and the base case substitution.
   - Always write: Initial $\to$ 1st substitution $\to$ 2nd substitution $\to$ Step $k$ general form $\to$ Base case condition $\to$ Final Big-$\Theta$.

5. **Doubly Linked List Conventions (Prof. Xiao):**
   - Be careful with attribute names! In Prof. Xiao's lectures, nodes use `self.value`, `self.left` (previous pointer), and `self.right` (next pointer).
   - Whenever deleting a node in the middle:
     ```python
     curr.left.right = curr.right
     curr.right.left = curr.left
     ```
   - Whenever inserting at the tail:
     ```python
     self.tail.right = new_node
     new_node.left = self.tail
     self.tail = new_node
     ```
