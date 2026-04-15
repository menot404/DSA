````markdown
# Asymptotic Analysis
*Source: GeeksforGeeks — Last Updated: 9 Apr, 2026*

Given two algorithms for a task, how do we find out which one is better?  
A naive approach is to implement both and compare their running times on different inputs, but this has major drawbacks:

- For some inputs, the first algorithm performs better; for others, the second does.
- Results may also vary depending on the machine used.

**Asymptotic analysis** evaluates an algorithm's performance based on **input size**, ignoring actual running time. It measures the *order of growth* of time or space:
- **Linear search** grows linearly
- **Binary search** grows logarithmically

---

## Example: Search in a Sorted Array

| Algorithm | Order of Growth |
|---|---|
| **Linear Search** | Linear — O(n) |
| **Binary Search** | Logarithmic — O(log n) |

---

## How is Asymptotic Analysis Machine Independent?

Consider running **Linear Search** on computer A (faster) and **Binary Search** on computer B (slower):

- For **small inputs**, Linear Search may be faster because computer A is faster.
- As **input size grows**, Binary Search eventually wins — even on the slower machine.
- This is because `O(n)` grows much faster than `O(log n)`.
- After a certain size, machine-dependent constants (e.g., A being 5000× faster than B) no longer matter.

### Running Time Comparison

| Input Size | Linear Search on A | Binary Search on B |
|---|---|---|
| 10 | 2 sec | ~1 min |
| 100 | 20 sec | ~1.8 min |
| 10⁶ | ~55.5 h | ~5.5 min |
| 10⁹ | ~6.3 years | ~8.3 min |

> **Formulas used:**
> - Linear Search on A: `0.2 × n` seconds
> - Binary Search on B: `1000 × log(n)` seconds

---

## Does Asymptotic Analysis Always Work?

Asymptotic analysis is the **best general method** for comparing algorithms, but it has limits:

- **Ignores constants:** Two algorithms both in `O(n log n)` — e.g., `1000n log n` vs `2n log n` — cannot be compared directly for practical speed.
- **Focuses on large inputs:** In real applications, those large inputs may never actually occur.
- **Can mislead in practice:** An asymptotically slower algorithm may outperform a faster one for specific input sizes, making it the better practical choice.
````