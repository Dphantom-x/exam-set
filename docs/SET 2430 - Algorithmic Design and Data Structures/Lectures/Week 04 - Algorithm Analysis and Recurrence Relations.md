# SET 2430 — Week 4: Algorithm Analysis, Recurrence Relations & Math Foundations

## 1. Recurrence Relations

A **recurrence relation** expresses the running time $T(n)$ of a recursive algorithm in terms of the running time on smaller inputs.

### Common Recurrence Patterns

| Pattern | Recurrence Form | Typical Algorithm | Closed Form / Big-O |
| :--- | :--- | :--- | :--- |
| **Linear Recurrence** | $T(n) = T(n-1) + c$ | Recursive Factorial, Linear search | $T(n) = c \cdot n + T(0) \implies \mathbf{O(n)}$ |
| **Divide and Conquer** | $T(n) = 2T(n/2) + n$ | Merge Sort, Recursive Sum Array | $T(n) = \mathbf{O(n \log n)}$ |
| **Branching / Exponential** | $T(n) = T(n-1) + T(n-2) + c$ | Naive Fibonacci | $T(n) = \mathbf{O(2^n)}$ |

---

## 2. Practice 1: Solving $T(n) = 2T(n/2) + n$ (Expansion / Recursion Tree Method)

### Problem
Prove that the recurrence $T(n) = 2T(n/2) + n$ has complexity $O(n \log n)$ assuming base case $T(1) = 1$.

### Step-by-Step Expansion Method
1. Start with the recurrence:
   $$T(n) = 2T(n/2) + n$$

2. Substitute $T(n/2) = 2T(n/4) + \frac{n}{2}$:
   $$T(n) = 2\left[2T(n/4) + \frac{n}{2}\right] + n = 4T(n/4) + n + n = 4T(n/4) + 2n$$

3. Substitute $T(n/4) = 2T(n/8) + \frac{n}{4}$:
   $$T(n) = 4\left[2T(n/8) + \frac{n}{4}\right] + 2n = 8T(n/8) + n + 2n = 8T(n/8) + 3n$$

4. Identify the general pattern after $k$ expansions:
   $$T(n) = 2^k T\left(\frac{n}{2^k}\right) + k \cdot n$$

5. Reach the base case where $\frac{n}{2^k} = 1 \implies 2^k = n \implies k = \log_2 n$:
   $$T(n) = n \cdot T(1) + (\log_2 n) \cdot n = n(1) + n \log_2 n$$

6. **Conclusion:**
   $$T(n) = n + n \log_2 n \implies \mathbf{O(n \log n)}$$

### Recursion Tree View
* **Level 0 (Root):** 1 node of size $n$, work done = $n$.
* **Level 1:** 2 nodes of size $n/2$, work done = $2 \times (n/2) = n$.
* **Level 2:** 4 nodes of size $n/4$, work done = $4 \times (n/4) = n$.
* ...
* **Level $k$:** $2^k$ nodes of size $n/2^k$, work done = $n$.
* **Tree Height:** $\log_2 n$ levels.
* **Total Work:** $\text{Work per level} \times \text{Number of levels} = n \times \log_2 n = \mathbf{O(n \log n)}$.

---

## 3. Practice 2: Different Solutions, Different Big-O ($1 + 2 + \dots + n$)

### Solution A: Iterative Loop
```python
def sum_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
```
* **Operations:** Loop runs $n$ times; each iteration does 1 addition. Total operations $\approx n$.
* **Time Complexity:** $\mathbf{O(n)}$ (Linear time).

### Solution B: Closed-Form Formula (Gauss)
```python
def sum_formula(n):
    return n * (n + 1) // 2
```
* **Operations:** Exactly 1 addition, 1 multiplication, 1 division regardless of $n$. Total operations = constant.
* **Time Complexity:** $\mathbf{O(1)}$ (Constant time).

### Why the difference matters
For $n = 1,000,000,000$:
* `sum_loop` takes a billion operations (several seconds).
* `sum_formula` takes 3 arithmetic operations (fractions of a nanosecond).

---

## 4. Best-Case, Worst-Case, and Average-Case Analysis

| Case | Definition | Practical Purpose | Example (Linear Search in array of size $n$) |
| :--- | :--- | :--- | :--- |
| **Best-Case** | Minimum steps possible on favorable input | Optimistic scenario | Target is at index 0 $\implies \mathbf{1 \text{ step}} \to \mathbf{O(1)}$ |
| **Worst-Case** | Maximum steps possible on adversarial input | Guaranteed ceiling / safety | Target is last or absent $\implies \mathbf{n \text{ steps}} \to \mathbf{O(n)}$ |
| **Average-Case** | Expected steps across all random uniform inputs | Realistic daily performance | Target is in middle $\approx \mathbf{n/2 \text{ steps}} \to \mathbf{O(n)}$ |

---

## 5. Asymptotic Notation: $O$, $\Omega$, $\Theta$

* **Big-O ($O$): Upper Bound.** Running time will grow *no faster than* this rate.
  * Linear search worst case: $O(n)$
* **Omega ($\Omega$): Lower Bound.** Running time will grow *at least as fast as* this rate.
  * Linear search best case: $\Omega(1)$
* **Theta ($\Theta$): Tight Bound.** The upper bound and lower bound match; exact growth rate.
  * Nested loop summing $1 \dots n$: $T(n) = \frac{n(n+1)}{2} = \mathbf{\Theta(n^2)}$

### Multi-Parameter Complexity
```python
for i in range(n):
    for j in range(m):
        print(i, j)
```
* Runs $n \times m$ times.
* Time complexity is $\mathbf{O(nm)}$, **not** $O(n^2)$ unless $n = m$.

---

## 6. Space Complexity

Measures memory growth as input size $n$ scales.

### Three Types of Memory:
1. **Input Space:** Memory used by the original inputs.
2. **Auxiliary Space:** Extra memory created by the algorithm during its run (variables, temporary lists).
3. **Recursion Stack Space:** Memory consumed on the call stack by nested recursive calls.

### Example: Running Sum
```python
def running_sum(nums):
    result = []      # size n -> O(n)
    total = 0        # O(1)
    for num in nums: # loop variable num -> O(1)
        total += num
        result.append(total)
    return result
```
* Note: We are storing $n$ elements in `result`, not triangular memory.
* Auxiliary space = $O(n) + O(1) + O(1) = \mathbf{O(n)}$.

---

## 7. Summations, Series & Logarithms

### Summation Formulas
1. $\sum_{i=1}^n 1 = n \implies \mathbf{O(n)}$ (Linear)
2. $\sum_{i=1}^n i = \frac{n(n+1)}{2} \implies \mathbf{O(n^2)}$ (Triangle numbers, quadratic)
3. $\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6} \approx \frac{1}{3}n^3 \implies \mathbf{O(n^3)}$ (Sum of squares, cubic)

### Geometric Series: $\sum_{i=0}^n r^i = \frac{r^{n+1}-1}{r-1}$
* **$|r| < 1$:** Converges to a constant $\implies \mathbf{O(1)}$.
* **$r = 1$:** Adds 1 $(n+1)$ times $\implies \mathbf{O(n)}$.
* **$r > 1$:** Dominated by the final term $r^n \implies \mathbf{O(r^n)}$ (Exponential growth).

### Harmonic Series: $H_n = \sum_{i=1}^n \frac{1}{i} \approx \ln n + \gamma$
* Growth rate: $\mathbf{\Theta(\log n)}$.
* Seen in average-case QuickSort and hash table chaining analysis.

### Logarithms ($\log_b n$)
* Occur whenever a problem is repeatedly cut by a constant factor (e.g. cut in half).
* **Binary Search:** $O(\log n)$
* **Balanced Binary Tree Height:** $O(\log n)$
* **Heap Insert / Delete:** $O(\log n)$
* Log base does not matter in Big-O: $\log_2 n = \Theta(\log_{10} n) = \Theta(\ln n)$ (differ only by a constant multiplier).

---

## 8. Data Structures Preview

### Array (Contiguous Memory)
* Elements stored in adjacent RAM memory addresses.
* Fast random access by index: $\mathbf{O(1)}$.
* Python `list` is implemented under the hood as a **dynamic array**.

### Linked List (Non-Contiguous Nodes)
* Elements stored in separate node objects: `[Data | Next Pointer]`.
* Nodes are scattered across memory; sequential traversal required.
* Python does not have a built-in linked list; implemented manually with a `Node` class.

### Binary Tree
* Hierarchical structure starting from a root node.
* Each node has at most 2 children (left child, right child).
* **Height ($h$):**
  * **Balanced Tree:** $h = \log_2 n \implies$ operations take $O(\log n)$.
  * **Skewed Tree (degenerate to a linked list):** $h = n \implies$ operations degrade to $O(n)$.
