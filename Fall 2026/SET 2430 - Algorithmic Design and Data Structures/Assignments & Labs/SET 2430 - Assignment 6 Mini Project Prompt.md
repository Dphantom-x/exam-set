# SET 2430 — Assignment 6 (Mini Project): Dice Battle Simulator

**Course:** SET 2430 — Algorithmic Design and Data Structures  
**Instructor:** Prof. Haiying Xiao  
**Term:** Fall 2026  

---

## Project Overview
Build an interactive or automated dice game where a player rolls a six-sided die and attempts to reach a score of **30 points**. The simulation models game events using fundamental linear data structures:
* **Python List / Dynamic Array** (Complete game history)
* **Queue / Deque** (Active scoring rolls)
* **Stack** (Special roll storage)
* **Big-O Theoretical Analysis** (Time complexity evaluation)

---

## Game Rules & Technical Requirements

### 1. Die Rolling
* Rolls simulate a fair six-sided die with values between `1` and `6` (`random.randint(1, 6)`).

### 2. Complete History (`List`)
* Every roll without exception must be appended to a Python `list` to preserve the complete chronological record of the game.

### 3. Active Rolls (`Queue`)
* Maintain active scoring dice in a FIFO **Queue** (or `collections.deque`).
* Only values currently sitting inside this queue contribute toward the player's current score.

### 4. Special Event Rules
* **Rolling a 6:**
  * Push the value `6` onto a **Stack** (LIFO).
  * *Important Rule Clarification:* As per Rule 5, values on the stack do **NOT** add to the current score (they are banked / sequestered on the stack).
* **Rolling a 1:**
  * If the active queue is not empty, remove (**dequeue**) the oldest roll from the front of the queue.
  * If the queue is empty, rolling a 1 does nothing to the queue.
* **Rolling 2, 3, 4, 5:**
  * Enqueue the value to the rear of the active queue.

### 5. Scoring Mechanism
$$\text{Score} = \sum(\text{Active Queue})$$
* Sum of all values currently in the queue.
* Elements stored on the stack do **not** contribute to the score.

### 6. Termination Condition
* Continue taking turns until the player's score reaches **30 or higher**.

### 7. Per-Turn Output & Logging
After every turn, the simulator must print:
* The current roll value.
* The state of the active queue.
* The current player score.
* (Optionally, state of the stack).

### 8. End-of-Game Summary
* Output victory notification (player reached $\ge 30$ points).
* Output total number of turns taken.
* Display the **complete history list** of every roll made during the game.

---

## Big-O Complexity Analysis Requirements
You must provide written theoretical time complexities for the four main operations:

1. **Adding a roll to the history list:**
   * Appending to a Python dynamic array $\implies \mathbf{O(1) \text{ Amortized}}$.
2. **Adding and removing items from the queue:**
   * Using `collections.deque` (`append` and `popleft`) $\implies \mathbf{O(1)}$.
   * (If using Python `list.pop(0)` $\implies O(n)$ due to element shifting).
3. **Pushing a value onto the stack:**
   * Appending to stack $\implies \mathbf{O(1) \text{ Amortized}}$.
4. **Calculating the current score:**
   * Direct summation `sum(queue)` $\implies \mathbf{O(k)}$ where $k$ is current queue size.
   * Or maintained running score accumulator variable $\implies \mathbf{O(1)}$.

---

## Bonus Feature (+10 Points)
* **Two-Player Turn-Based Mode:**
  * Two players (Player 1 vs. Player 2) alternate turns.
  * Each maintains their own active queue, stack, and score.
  * First player to reach 30 points wins!

---

## Grading Rubric (100 Points Total + 10 Bonus)

| Category | Points | Criteria |
| :--- | :---: | :--- |
| **Submission & Requirements** | 10 pts | Submitted on time following instructions (10 pts). Late within allowed window (5 pts). |
| **Core Game Functionality** | 25 pts | Random 1–6 rolling works (10 pts). Correct score calculation (10 pts). Game terminates at $\ge 30$ pts (5 pts). |
| **Data Structure Implementation** | 30 pts | Queue / Deque implemented (10 pts). Stack implemented (10 pts). Array / List implemented (10 pts). |
| **Special Rules Implementation** | 15 pts | Rolling 6 pushes to stack; rolling 1 removes oldest roll from queue. |
| **Output & Logging** | 10 pts | Prints turn roll, current queue, current score, and final complete history. |
| **Big-O Analysis** | 10 pts | Explains complexities of all 4 operations and overall program. |
| **Bonus: Two-Player Mode** | +10 pts | Turn-based 2-player competition until one reaches 30. |
