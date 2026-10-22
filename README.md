# 🏆 SET 2430: Midterm Master Examination Suite & Study Hub
**New York City College of Technology (CUNY) • Department of Computer Engineering Technology**  
*Course:* **SET 2430 — Algorithmic Design and Data Structures** (Fall 2026)  
*Instructor:* **Professor Haiying Xiao**

---

## 🌐 Live Online Study Portal
The entire interactive examination suite is hosted live on GitHub Pages:  
👉 **[https://dphantom-x.github.io/exam-set/](https://dphantom-x.github.io/exam-set/)**

*Study on your phone, tablet, laptop, or campus library computer. All embedded prompt PDFs, full Python source files, interactive 3D flashcards, and step-by-step rubrics are available online.*

---

## 📚 What's Inside the Study Suite

### 1. 🏆 Full Past Exams Archive & Timed Mocks
* **Mock Exam 1 (Standard Departmental Benchmark):** 100 points, 5 sections covering Asymptotics, Variable State Tracing, Recurrence Expansion Proofs, Box-and-Pointer Memory Diagrams, and Handwritten Class Implementations.
* **Mock Exam 2 (Advanced Edge-Case Variant):** 100 points focusing on tricky pointer rewiring, single-node deletions, circular list bounds, and queue-stack simulations.
* **CUNY Historical Question Bank:** Authentic multi-choice and free-response problem sets from past City Tech midterms.
* **Dual View:** Toggle between Full Paper View (simulating physical paper) and Section-by-Section Mode with teacher's master key reveals.

### 2. 📚 Interactive Topic-by-Topic Drill & 3D Flashcards
* **Topic 1: Recurrences** — 6-step algebraic paper substitution method + **7 Recurrence Tree Variations**.
* **Topic 2: Math & Summations** — $\sum i$, $\sum i^2$, $\sum 2^i$, set rules ($\in$ vs $\subseteq$) + **6 Series Variations**.
* **Topic 3: Asymptotics & Growth Hierarchy** — $O$, $\Omega$, $\Theta$ definitions and 8-tier growth rankings.
* **Topic 4: Dynamic Arrays & Amortized Doubling** — Geometric doubling vs $+K$ fixed expansion trap table.
* **Topic 5: Linked Lists** — Singly, Doubly, and Circular Linked Lists with Prof. Xiao's `val`, `left`, `right` convention.
* **Topic 6: Stacks & Queues** — Circular array modulo arithmetic, 2-stack `BrowserHistory`, and 2-queue `MyStack`.
* **Topic 7: Deque & Built-in** — Double-ended queues and `collections.deque`.
* **Universal Shortcuts:**
  * 🌲 **Tree Shortcut:** *Inside* = Height ($\log_2 n$ vs $n$), *Front* = Nodes ($2^k$), *Outside* = Work per node.
  * ⚡ **Sum Shortcut:** Loop is always $O(n)$ time / $O(1)$ space; Closed form is always $O(1)$ time / $O(1)$ space.

### 3. 📁 Side-by-Side Class Assignments & Python Code Studio
Inspect the authentic assignment prompt PDFs alongside verified, submitted Python code:
* **Assignment 2:** OOP Encapsulation (`@property`), `*args/**kwargs`, $O(\sqrt{n})$ Prime Check, Stack Adjacent De-duplication.
* **Assignment 3:** Nested Loop Triangular Summations ($\sum i = \frac{n(n+1)}{2} = \Theta(n^2)$) and 1D Running Prefix Sum.
* **Assignment 4:** Binary Tree Recursion (`count_nodes`, `max_depth` DFS/BFS) and Recurrence $T(h) = 2T(h-1) + c \implies O(2^h) = O(n)$.
* **Assignment 5:** Dual-Stack `BrowserHistory` (clearing forward stack on new visit) and Two-Queue LIFO `MyStack`.
* **Master 10 Linear Data Structures Code:** Full implementations of Singly, Doubly, Circular Singly, Circular Doubly Linked Lists, Array/Linked Stacks, Circular Array/Linked Queues, and Array/Linked Deques.

### 4. 🛡️ No-IDE Paper Survival Protocol
* Hand-drawn indentation guidelines (combating the "Colons & Self" point-loss trap).
* The 5-column Trace Table methodology for predicting variable states without running code.
* Box-and-pointer diagramming rules (wire new node arrows *first* before severing old links).
* The 7 Universal Edge Cases checklist required for every paper implementation.

### 5. 📄 Official Course Outline & Syllabus
* Complete departmental syllabus embedded directly in-page.

---

## 📂 Repository File Structure

```text
├── index.html                                 # Live GitHub Pages Root Entry
├── SET_2430_Midterm_Master_Hub.html           # Master Exam Hub Application
├── README.md                                  # Repository documentation
├── docs/                                      # Embedded PDFs & course documents
│   └── SET 2430 - Algorithmic Design and Data Structures/
│       └── Syllabus & Course Info/
│           └── SET2430 Course Outline (Prof Xiao, Fall 2026).pdf
├── Fall 2026/
│   └── SET 2430 - Algorithmic Design and Data Structures/
│       ├── Assignments & Labs/
│       │   ├── ALL_10_DATA_STRUCTURES_MASTER_CODE.py
│       │   ├── SET 2430 - Assignment 2 Prompt.pdf
│       │   ├── SET 2430 - Assignment 3 Prompt.pdf
│       │   ├── SET 2430 - Assignment 4 Prompt.pdf
│       │   ├── SET 2430 - Assignment 5 Prompt.pdf
│       │   ├── assignment2.py
│       │   ├── assignment3.py
│       │   ├── assignment4.py
│       │   ├── assignment5.py
│       │   ├── oct7_linked_list_practice.py
│       │   ├── week4_practice.py
│       │   └── week7_linked_lists_code.py
│       ├── Lectures/                          # Lecture slides and notes
│       ├── Exams & Study/                     # Study dossiers and cheat sheets
│       └── Syllabus & Course Info/            # Course outline PDF
└── SET_2430_COMPLETE_STUDY_PACKAGE/           # Portable 5-module study package
    ├── 00_START_HERE_COURSE_PORTAL.md
    ├── 01_Exams_and_Mock_Tests/
    ├── 02_Lectures_and_Class_Notes/
    ├── 03_Assignments_and_Labs/
    ├── 04_Syllabus_and_Policies/
    └── 05_Study_Portal_Topics/
```

---

## 🎯 Quick High-Yield Review Matrix

| Topic | Critical Formula / Rule to Write on Paper | Asymptotic Complexity |
| :--- | :--- | :--- |
| **Gauss Sum** | $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$ | $\Theta(n^2)$ |
| **Sum of Squares** | $\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$ | $\Theta(n^3)$ |
| **Geometric Doubling** | $\sum_{i=0}^{k} 2^i = 2^{k+1} - 1$ | $\Theta(2^k)$ |
| **Divide-and-Conquer** | $T(n) = 2T(n/2) + n \implies n + n \log_2 n$ | $\Theta(n \log n)$ |
| **Tree Height Recurrence** | $T(h) = 2T(h-1) + c \implies c \cdot (2^h - 1)$ | $O(2^h) = O(n)$ |
| **Dynamic Array Doubling** | Amortized work per append: $\frac{3N}{N}$ | $O(1)$ amortized |
| **Circular Queue Pointers**| `(rear + 1) % capacity` / `(front + 1) % capacity` | $O(1)$ without shifting |
| **Two-Queue Stack Push**   | Enqueue $x \to q2$, dump $q1 \to q2$, swap `q1, q2 = q2, q1` | $O(n)$ push, $O(1)$ pop |
| **Doubly Linked List**    | Prof. Xiao convention: `self.value`, `self.left` (prev), `self.right` (next) | Wire new first! |

---

*Compiled and published for City Tech CET / SET 2430 Students.*
