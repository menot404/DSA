````markdown
# Asymptotic Analysis
*Source: GeeksforGeeks — Last Updated: 9 Apr, 2026*

Given two algorithms for a task, how do we find out which one is better?  
A naive approach is to implement both algorithms and compare their running times on different inputs, but this method has many drawbacks:

- For some inputs, the first algorithm performs better than the second, and vice versa.
- For some inputs, the first algorithm performs better on one machine, while the second works better on another machine.

**Asymptotic analysis** evaluates an algorithm's performance based on input size, ignoring actual running time. It measures the **order of growth** of time or space — for example, linear search grows linearly, while binary search grows logarithmically.

---

## Example: Search in a Sorted Array

Consider the problem of searching a given item in a sorted array. Two solutions exist:

- **Linear Search** — order of growth is *linear*
- **Binary Search** — order of growth is *logarithmic*

---

## How is Asymptotic Analysis Machine Independent?

- Suppose we run **Linear Search** on computer A *(faster)* and **Binary Search** on computer B *(slower)*.
- For small input sizes, Linear Search may take less time because computer A is faster.
- As the input size increases, Binary Search eventually becomes faster, even on the slower computer B.
- This happens because Linear Search grows **linearly**, while Binary Search grows **logarithmically**.
- After a certain input size, machine-dependent constants (e.g., A being 5000× faster than B) no longer matter.
- Asymptotic analysis focuses on this growth, allowing us to compare algorithms **independent of machine speed** for large inputs.

### Running Time Comparison

| Input Size | Running time on A | Running time on B |
|:----------:|:-----------------:|:-----------------:|
| 10         | 2 sec             | ~ 1 minute        |
| 100        | 20 sec            | ~ 1.8 minutes     |
| 10⁶        | ~ 55.5 hours      | ~ 5.5 minutes     |
| 10⁹        | ~ 6.3 years       | ~ 8.3 minutes     |

Running times for this example:
- **Linear Search** on A: `0.2 × n` seconds
- **Binary Search** on B: `1000 × log(n)` seconds

---

## Does Asymptotic Analysis Always Work?

- Asymptotic analysis is the **best general method** for analyzing algorithms, even though it is not perfect.
- It **ignores constant factors**, so two algorithms with the same asymptotic complexity (e.g., `1000 × n log n` vs `2 × n log n`) cannot be directly compared for practical speed.
- It focuses on **large input sizes**, but in real applications, these inputs may never occur.
- An algorithm that is asymptotically slower can perform better for specific inputs, so practical performance may lead to choosing it over a theoretically faster algorithm.
````
