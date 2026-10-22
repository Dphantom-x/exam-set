# SET 2430 — Week 5: Algorithm Analysis (Part 2), Recurrence Relations & Space Complexity

Prof. Haiying Xiao · Fall 2026

---

## 1. Recurrence Relations

A **recurrence relation** expresses the total running time $T(n)$ of a recursive algorithm in terms of the running time on smaller input subproblems.

### Common Recurrence Patterns

| Pattern | Recurrence Equation | Typical Example | Big-O Complexity |
| :--- | :--- | :--- | :--- |
| **Linear Recurrence** | $T(n) = T(n-1) + c$ | Recursive Factorial, Linear search | $T(n) = c \cdot n + T(0) \implies \mathbf{O(n)}$ |
| **Divide and Conquer** | $T(n) = 2T(n/2) + n$ | MergeSort, Recursive Array Sum | $\mathbf{O(n \log n)}$ |
| **Branching / Exponential** | $T(n) = T(n-1) + T(n-2) + c$ | Naive Recursive Fibonacci | $\mathbf{O(2^n)}$ |

---

## 2. Practice 1: Solving $T(n) = 2T(n/2) + n$ (Expansion / Recursion Tree Method)

### Problem Statement
Prove that the recurrence $T(n) = 2T(n/2) + n$ with base case $T(1) = 1$ has time complexity $O(n \log n)$.

### Step-by-Step Expansion Method

1. **Step 1: Initial Equation**
   $$T(n) = 2T(n/2) + n$$

2. **Step 2: First Substitution (Substitute $T(n/2) = 2T(n/4) + n/2$)**
   $$T(n) = 2\left[2T(n/4) + \frac{n}{2}\right] + n = 4T(n/4) + n + n = 4T(n/4) + 2n$$

3. **Step 3: Second Substitution (Substitute $T(n/4) = 2T(n/8) + n/4$)**
   $$T(n) = 4\left[2T(n/8) + \frac{n}{4}\right] + 2n = 8T(n/8) + n + 2n = 8T(n/8) + 3n$$

4. **Step 4: General Pattern after $k$ Expansions**
   $$T(n) = 2^k T\left(\frac{n}{2^k}\right) + k \cdot n$$

5. **Step 5: Base Case Termination**
   We reach the base case when $\frac{n}{2^k} = 1 \implies 2^k = n \implies k = \log_2 n$.
   Substitute $k = \log_2 n$ and $2^k = n$:
   $$T(n) = n \cdot T(1) + (\log_2 n) \cdot n = n(1) + n \log_2 n$$

6. **Conclusion:**
   $$T(n) = n + n \log_2 n \implies \mathbf{O(n \log n)}$$

### Recursion Tree Visualization
* **Level 0 (Root):** 1 problem of size $n \implies \text{Work} = n$
* **Level 1:** 2 subproblems of size $n/2 \implies \text{Work} = 2 \times (n/2) = n$
* **Level 2:** 4 subproblems of size $n/4 \implies \text{Work} = 4 \times (n/4) = n$
* **Level $k$:** $2^k$ subproblems of size $n/2^k \implies \text{Work} = n$
* **Tree Height:** $\log_2 n$ levels.
* **Total Cost:** $\text{Work per level} \times \text{Height} = n \times \log_2 n = \mathbf{O(n \log n)}$.

---

## 3. Practice 2: Different Solutions, Different Big-O ($1 + 2 + \dots + n$)

### Solution A: Iterative Loop ($O(n)$)
```python
def sum_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
```
* **Operations:** Loop executes $n$ times. Each iteration performs 1 addition and 1 assignment. Total operations $\approx 2n$.
* **Time Complexity:** $\mathbf{O(n)}$ (Linear time).

### Solution B: Closed-Form Formula ($O(1)$)
```python
def sum_formula(n):
    return n * (n + 1) // 2
```
* **Operations:** Exactly 1 addition $(n + 1)$, 1 multiplication $(n \times \dots)$, and 1 integer division $(// 2)$, regardless of the size of $n$.
* **Time Complexity:** $\mathbf{O(1)}$ (Constant time).

---

## 4. Asymptotic Notations: $O$, $\Omega$, and $\Theta$

* **Big-O ($O$) — Upper Bound**: Guarantees the maximum growth rate (ceiling).
  * Example: Linear search worst case is $O(n)$.
* **Big-Omega ($\Omega$) — Lower Bound**: Guarantees the minimum growth rate (floor).
  * Example: Linear search best case is $\Omega(1)$ (found at index 0).
* **Big-Theta ($\Theta$) — Tight Bound**: True when upper bound and lower bound match.
  * Example: Nested loop summing triangular numbers:
    $$T(n) = \frac{n(n+1)}{2} = \mathbf{\Theta(n^2)}$$

### Multi-Parameter Complexity
When algorithms take multiple independent inputs:
```python
for i in range(n):
    for j in range(m):
        print(i, j)
```
* **Time Complexity:** $\mathbf{O(n \cdot m)}$
* **Important:** This is NOT $O(n^2)$ unless $n = m$. If $n$ and $m$ scale independently, both parameters must appear in the Big-O bound.

---

## 5. Binary Tree Complexity & Height

A **binary tree** is a hierarchical data structure where every node has at most two children (left child and right child), starting at the root node.

### Height ($h$) vs. Node Count ($n$)
* **Balanced Binary Tree**:
  * Nodes distributed evenly across both branches.
  * Height: $h = \mathbf{\log_2 n}$
  * Search, Insert, and Delete operations take $\mathbf{O(\log n)}$.
* **Skewed Binary Tree**:
  * Every node has only one child (essentially degenerates into a linked list).
  * Height: $h = \mathbf{n}$
  * Operations degrade to worst-case $\mathbf{O(n)}$.

---

## 6. Space Complexity & Auxiliary Space

**Space Complexity** measures the total memory an algorithm uses as a function of the input size $n$.

### The Three Components of Space Complexity
1. **Input Space**: Memory required to store the input data itself.
2. **Auxiliary Space**: Extra or temporary memory allocated by the algorithm outside the input.
3. **Call Stack Space**: Memory consumed by active recursion frames on the call stack.

### Case Study: Prefix Running Sum
```python
def running_sum(nums):
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    return result
```
* **Memory Analysis:**
  * `result` list allocates memory for $n$ accumulated values $\to O(n)$.
  * `total` scalar variable $\to O(1)$.
  * `num` loop variable $\to O(1)$.
* **Total Auxiliary Space:** $O(n) + O(1) + O(1) = \mathbf{O(n)}$.
