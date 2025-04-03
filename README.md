# 8-Puzzle Solver (Uninformed Search)
## 📌 Overview
----
## This project implements an 8-Puzzle Solver using uninformed search algorithms:

1.Breadth-First Search (BFS)

2.Depth-First Search (DFS)

3.Iterative Deepening Depth-First Search (IDDFS)

These algorithms explore possible moves to solve the puzzle without using heuristics.

# 🔢 What is the 8-Puzzle?
The 8-Puzzle is a sliding tile puzzle consisting of a 3×3 grid with numbered tiles (1-8) and one empty space. The goal is to arrange the tiles in the correct order by sliding them into the empty space.

## Example:
Initial State → Goal State

1 2 3       1 2 3  
4 _ 5   →   4 5 6  
7 8 6       7 8 _  
## 🛠️ Implementation
.The puzzle is represented as a graph, where each state (tile arrangement) is a node.

.Moves (Up, Down, Left, Right) generate new states.

.The search algorithms explore the state space to find a solution.

## 🔍 Search Algorithms Used
1.Breadth-First Search (BFS): Explores nodes level by level (guarantees shortest path).

2.Depth-First Search (DFS): Explores deeper nodes first but may get stuck in loops.

3.Iterative Deepening Depth-First Search (IDDFS): Combines DFS and BFS advantages.
