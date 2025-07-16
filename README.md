# Triplet Packing Site

This repository presents a web-based interface for experimenting with the triplet_algo packing algorithm from the prtpy library. The algorithm finds groupings of item triplets such that each group sums exactly to a given bin size — a variation of the classic bin-packing problem with specific constraints.
Built to make advanced algorithms more approachable, this tool is ideal for students, researchers, and enthusiasts exploring combinatorial optimization.

---

## About Me

Hi! I'm **Miriam Nagar**, currently a third year computer science student at **Ariel University**.  
This project was developed as part of my final assignment for the **Research Algorithms** course.

---

## Project Overview

This project explores the Triplet Packing Problem – a constrained variation of the classic bin packing problem, where items must be partitioned into triplets such that each triplet sums exactly to a fixed bin size.

I implemented and exposed the triplet_algo module from the prtpy library —
an advanced algorithmic framework for solving packing problems, including those involving strict triplet constraints.

This implementation is based on the algorithm presented in the paper:

"Solution of Bin Packing Instances in Falkenauer T Class: Not So Hard"
by György Dósa, András Éles, Angshuman Robin Goswami, István Szalkai, Zsolt Tuza (2025), 
[Link to paper](https://www.mdpi.com/1999-4893/18/2/115#)

The site offers two solving strategies:

Backtracking – an exhaustive search that recursively assembles valid triplets.

Local Search – a heuristic that improves solutions through optimization over a search tree.

To support exploration and understanding, the interface includes configurable logging levels, runtime trace display, and randomly generated valid input examples.

---

##  Tools & Technologies

| Tech           | Usage                             |
| -------------- | --------------------------------- |
| 🐍 Python      | Core algorithm and backend        |
| ⚙️ Flask       | Lightweight web server            |
| 🌐 HTML/CSS/JS | Responsive frontend               |
| 📦 prtpy       | Triplet packing algorithm         |
| 📝 Logging     | Live log level selection + output |

---

## What You Can Do on the Site

- Enter a list of item weights and a target bin size.

- Choose algorithm mode:

    backtracking: systematic exhaustive search

    local search: heuristic improvement phase

- Select a log verbosity level (e.g., DEBUG or INFO).

- View results formatted as triplet groups.

- Inspect the log stream for step-by-step insights into the algorithm's behavior.

- Use example generator to create valid random test cases.

- Clear the form with one click to start over

---

## Resources & Credits

- Original prtpy library

- Research paper: [Solution of Bin Packing Instances in Falkenauer T Class: Not So Hard](https://www.mdpi.com/1999-4893/18/2/115#)

- Ariel University — Research Algorithms Course

---

## 🙏 Thanks for Visiting!