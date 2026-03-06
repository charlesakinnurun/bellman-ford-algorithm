<h1 align="center">Bellman–Ford Algorithm</h1>

## Overview

The **Bellman–Ford Algorithm** is a **shortest path algorithm** used to find the minimum distance from a **single source vertex** to all other vertices in a **weighted graph**.

Unlike some other shortest-path algorithms, Bellman–Ford can handle **negative edge weights**.

It is known for:

* ✅ Handling **negative weight edges**
* ✅ Detecting **negative weight cycles**
* ❌ Being slower than some other algorithms like Dijkstra

<a href="/src/main.py">Check out source code</a>

---

## 📌 Key Concepts

### Weighted Graph

A graph where each edge has a **numerical cost (weight)**.

### Shortest Path

The path between two vertices with the **minimum total weight**.

### Negative Weight Edge

An edge whose weight is **less than zero**.

Example:

```
A → B  weight = -3
```

### Negative Cycle

A cycle where the **sum of weights is negative**.

This is important because it can make the shortest path **undefined**.

---

## ⚙️ How Bellman–Ford Works

1. Initialize the distance to all vertices as **infinity**
2. Set the **source vertex distance to 0**
3. Relax all edges **V − 1 times**
4. Check for **negative cycles**

Where:

* **V = number of vertices**
* **E = number of edges**

---

## 🧩 Example Graph

```
      (4)
   A ------ B
   |        |
 (5)|        |(-2)
   |        |
   C ------ D
       (3)
```

### Edge List

| Edge  | Weight |
| ----- | ------ |
| A → B | 4      |
| A → C | 5      |
| B → D | -2     |
| C → D | 3      |

---

## 🧪 Step-by-Step Example

### Step 1 — Initialize Distances

Source = **A**

| Vertex | Distance |
| ------ | -------- |
| A      | 0        |
| B      | ∞        |
| C      | ∞        |
| D      | ∞        |

---

### Step 2 — Relax Edges (Iteration 1)

Check every edge.

```
A → B (4)
Distance[B] = 0 + 4 = 4
```

```
A → C (5)
Distance[C] = 0 + 5 = 5
```

```
B → D (-2)
Distance[D] = 4 - 2 = 2
```

```
C → D (3)
Distance[D] = min(2, 5+3=8) = 2
```

---

### Step 3 — Repeat Relaxation

After **V − 1 iterations**, the distances stabilize.

Final shortest distances from **A**:

| Vertex | Shortest Distance |
| ------ | ----------------- |
| A      | 0                 |
| B      | 4                 |
| C      | 5                 |
| D      | 2                 |

---

## ⏱️ Time & Space Complexity

| Operation   | Complexity |
| ----------- | ---------- |
| Relax edges | O(V × E)   |

Where:

* **V** = number of vertices
* **E** = number of edges

**Space Complexity:** O(V)

---

## 🧠 Python Implementation

```python
def bellman_ford(vertices, edges, source):
    distance = {v: float('inf') for v in vertices}
    distance[source] = 0

    # Relax edges V-1 times
    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # Check for negative cycle
    for u, v, w in edges:
        if distance[u] + w < distance[v]:
            print("Graph contains a negative weight cycle")
            return None

    return distance


vertices = ['A', 'B', 'C', 'D']

edges = [
    ('A', 'B', 4),
    ('A', 'C', 5),
    ('B', 'D', -2),
    ('C', 'D', 3)
]

print(bellman_ford(vertices, edges, 'A'))
```

### Output

```
{'A': 0, 'B': 4, 'C': 5, 'D': 2}
```

---

## 👍 Advantages

* Handles **negative edge weights**
* Detects **negative cycles**
* Works on **directed graphs**

---

## 👎 Disadvantages

* Slower than **Dijkstra’s Algorithm**
* Not ideal for **very large graphs**
* Requires **multiple relaxations**

---

## 📊 Bellman–Ford vs Dijkstra

| Feature                  | Bellman–Ford | Dijkstra   |
| ------------------------ | ------------ | ---------- |
| Handles negative weights | ✅ Yes        | ❌ No       |
| Detects negative cycles  | ✅ Yes        | ❌ No       |
| Speed                    | Slower       | Faster     |
| Time Complexity          | O(VE)        | O(E log V) |

---

## 📌 Applications

Bellman–Ford is used in:

* Network routing protocols
* Distance vector routing (like **RIP**)
* Detecting **arbitrage opportunities in finance**
* Graphs with **negative edge weights**

---

## 🏁 Summary

The **Bellman–Ford Algorithm** is a powerful shortest-path algorithm capable of handling **negative weights and detecting negative cycles**. While slower than Dijkstra, it is essential for problems where negative edge costs exist.
