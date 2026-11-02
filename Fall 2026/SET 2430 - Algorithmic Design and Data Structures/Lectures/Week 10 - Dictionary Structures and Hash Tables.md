# SET 2430 — Week 10: Dictionary Structures & Hash Tables

**Prof. Haiying Xiao** · Fall 2026

---

## 1. Dictionary ADT (Abstract Data Type)

A **Dictionary** (Map / Associative Array / Hash Table) is an abstract data structure that stores collections of unique **key-value pairs**.
* **Key Invariant:** Keys must be unique and hashable (immutable in Python, such as strings, ints, or tuples).
* **Values:** Can be any arbitrary data type (lists, objects, integers, other dictionaries).

---

## 2. Core Python Dictionary Operations

```python
# Creation
student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Physics"]
}

student2 = dict(name="Bob", age=22, courses=["Chemistry"])

# Accessing Values
print(student["name"])                 # "Alice" (raises KeyError if key not found)
print(student.get("grade", "N/A"))     # "N/A" (safe lookup with fallback default)

# Adding / Updating Values
student["grade"] = "A"
student.update({"age": 21, "city": "New York"})

# Deletion
del student["city"]                    # Removes key
age = student.pop("age")               # Removes key and returns value (21)
last_item = student.popitem()          # Removes and returns last inserted key-value pair
```

---

## 3. Dictionary Comprehensions

Python provides expressive comprehension syntax for constructing and transforming dictionaries:

```python
# 1. Square numbers: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
squares = {x: x**2 for x in range(1, 6)}

# 2. Filtering with condition (even squares)
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}

# 3. Inverting / Swapping keys and values
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}   # {1: 'a', 2: 'b', 3: 'c'}
```

---

## 4. In-Class Practice: Word Frequency Counter

Counting frequencies of occurrences across a body of text:

```python
def word_frequency(text):
    # Normalize: lowercase and strip punctuation
    import re
    cleaned = re.sub(r'[^\w\s]', '', text.lower())
    words = cleaned.split()
    
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


# Example Usage:
text = "Python is great. Python is powerful. Learn Python!"
freqs = word_frequency(text)
print(freqs)
# Output: {'python': 3, 'is': 2, 'great': 1, 'powerful': 1, 'learn': 1}

# Finding the most frequent word:
most_common = max(freqs, key=freqs.get)
print("Most frequent word:", most_common, "with count:", freqs[most_common])
```

---

## 5. Advanced Applications & Specialized Structures

### A. Graph Representation (Adjacency List)
Dictionaries map each vertex to a list or set of adjacent neighboring vertices:
```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}
```

### B. LRU (Least Recently Used) Cache Concept
Combining a hash map for $O(1)$ key lookup with a doubly linked list (or `collections.OrderedDict`) to track access recency.

### C. `collections.defaultdict`
Eliminates explicit key existence checks by automatically initializing missing keys with a default factory function:
```python
from collections import defaultdict

freq = defaultdict(int)
for word in ["apple", "banana", "apple"]:
    freq[word] += 1  # No KeyError! Default is 0.
```

---

## 6. Time Complexity of Hash Table Operations

| Operation | Average Case | Worst Case (Extreme Hash Collisions) |
| :--- | :---: | :---: |
| **Lookup `dict[key]`** | $\mathbf{O(1)}$ | $O(n)$ |
| **Insert / Update** | $\mathbf{O(1)}$ | $O(n)$ |
| **Delete `del dict[key]`** | $\mathbf{O(1)}$ | $O(n)$ |
| **Iteration over $N$ items** | $O(n)$ | $O(n)$ |
