# Order of Growth
*Source: GeeksforGeeks — Last Updated: 9 Apr, 2026*

Let `f(n)` and `g(n)` be the time taken by two algorithms where `n >= 0` and `f(n), g(n) >= 0`.  
A function `f(n)` is said to be **growing faster** than `g(n)` if:

$$\lim_{n \to \infty} \frac{g(n)}{f(n)} = 0 \quad \text{or equivalently} \quad \lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty$$

---

## Examples

**Example 1:** `f(n) = 1000`, `g(n) = n + 1`  
For `n > 999`, `g(n)` is always greater than `f(n)` — the order of growth of `g(n)` is higher.

**Example 2:** `f(n) = 4n²`, `g(n) = 2n + 2000`  
`f(n)` has a higher order of growth as it grows **quadratically** in terms of input size.

---

## How to Quickly Find the Order of Growth?

When `n >= 0`, `f(n) >= 0` and `g(n) >= 0`, apply these two steps:

1. **Ignore the lower order terms**
2. **Ignore the constants**

**Example 1:** `4n² + 3n + 100`
- After ignoring lower order terms → `4n²`
- After ignoring constants → `n²`
- ✅ Order of growth: **n²**

**Example 2:** `100n log n + 3n + 100 log n + 2`
- After ignoring lower order terms → `100n log n`
- After ignoring constants → `n log n`
- ✅ Order of growth: **n log n**

---

## Comparing Orders of Growth

The following standard hierarchy must be remembered:

$$c \ < \ \log\log n \ < \ \log n \ < \ n^{1/3} \ < \ n^{1/2} \ < \ n \ < \ n\log n \ < \ n^2 \ < \ n^2\log n \ < \ n^3 \ < \ n^4 \ < \ 2^n \ < \ n^n$$

> Where **c** is a constant.