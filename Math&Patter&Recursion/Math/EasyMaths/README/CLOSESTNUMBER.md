# Le plus proche de n et divisible par m
*Source: GeeksforGeeks — Dernière mise à jour : 23 mars 2026*

Étant donné deux entiers `n` et `m` (`m ≠ 0`), trouvez le nombre le plus proche de `n` et divisible par `m`. S'il en existe plusieurs, affichez celui dont la **valeur absolue est maximale**.

**Exemples :**
- Entrée : `n = 13, m = 4` → Sortie : `12` — 12 est le plus proche de 13 divisible par 4.
- Entrée : `n = -15, m = 6` → Sortie : `-18` — -12 et -18 sont tous deux les plus proches de -15, mais -18 a la valeur absolue maximale.

---

## [Approche naïve] Vérification itérative — O(m) Temps et O(1) Espace

L'idée est de vérifier tous les nombres de `n - m` à `n + m` un par un et de prendre le plus proche.

```python
def nombre_le_plus_proche(n, m):
    le_plus_proche = 0
    difference_min = float('inf')

    # Vérifier les nombres autour de n
    for i in range(n - abs(m), n + abs(m) + 1):
        if i % m == 0:
            difference = abs(n - i)

            if difference < difference_min or \
                    (difference == difference_min and abs(i) > abs(le_plus_proche)):
                le_plus_proche = i
                difference_min = difference
    return le_plus_proche

if __name__ == "__main__":
    n = 13
    m = 4
    print(nombre_le_plus_proche(n, m))
```

**Sortie :**
```
12
```

---

## [Approche attendue] En calculant le quotient — O(1) Temps et O(1) Espace

On calcule d'abord le quotient `q = n / m`, puis on détermine deux candidats :

- `n1 = m * q` — le multiple de `m` le plus proche **inférieur ou égal** à `n`.
- `n2 = m * (q + 1)` ou `m * (q - 1)` selon les signes de `n` et `m` :
  - Si `n` et `m` ont le **même signe** → `n2 = m * (q + 1)` — on avance vers `n` pour obtenir le multiple le plus proche au-dessus.
  - Si `n` et `m` ont des **signes opposés** → `n2 = m * (q - 1)` — augmenter `q` éloignerait de `n`, on recule donc pour obtenir le multiple le plus proche.

On retourne ensuite `n1` ou `n2` selon lequel a la plus petite différence absolue avec `n`. Si les deux sont équidistants, on retourne celui avec la **plus grande valeur absolue**.

```python
def nombre_le_plus_proche(n, m):
    q = int(n / m)

    # Premier nombre le plus proche possible
    n1 = m * q

    # Deuxième nombre le plus proche possible
    if (n * m) > 0:
        n2 = m * (q + 1)
    else:
        n2 = m * (q - 1)

    # Si vrai, alors n1 est le nombre le plus proche requis
    if abs(n - n1) < abs(n - n2):
        return n1

    # Sinon n2 est le nombre le plus proche requis
    return n2

if __name__ == "__main__":
    n = 13; m = 4
    print(nombre_le_plus_proche(n, m))
```

**Sortie :**
```
12
```