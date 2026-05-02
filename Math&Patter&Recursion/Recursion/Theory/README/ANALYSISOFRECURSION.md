# Time Complexity Analysis of Recursive Functions
*Source: GeeksforGeeks — Last Updated: 7 Mar, 2026*

The analysis of a recursive function involves finding an **asymptotic upper bound** on the running time.

- Many algorithms use recursion, and analyzing their time complexity often leads to a **recurrence relation** — an expression of the running time for input size `n` in terms of smaller input sizes.
- For example, in **Merge Sort**, the array is divided into two halves, each half is sorted recursively, and the results are merged. This leads to the recurrence relation `T(n) = 2T(n/2) + cn`, where `cn` represents the time required to merge the two sorted halves.

---

## Example

Consider the following code:

```python
def fun(n):
    if n <= 1:
        return
    fun(n // 2)
    fun(n // 2)
    for i in range(n):
        print('GFG', end=' ')
```

The time complexity of this function is expressed as:

$$T(n) = 2T\left(\frac{n}{2}\right) + O(n)$$

To find the time complexity, we need to **solve this recurrence relation**.

---

## Methods to Solve Recurrence Relations

There are three main methods used to solve recurrence relations arising in the analysis of recursive algorithms:

### 1. Substitution Method
We **guess the form** of the solution and prove it correct using **mathematical induction**.

### 2. Recurrence Tree Method
This method represents the recurrence as a **tree** and computes the total cost by **summing the cost at each level**.

### 3. Master Theorem
Provides a **direct formula** to solve divide-and-conquer recurrences of the form:

$$T(n) = aT\left(\frac{n}{b}\right) + f(n)$$