# Schedule Moves for Robot

## Problem Description
There are two robots A and B moving on a weighted graph **G**. Since both robots are controlled
by radio waves, they cannot be close to each other for a distance **r**. Initially, two robots
stand at vertex A and vertex B on G. The robot at A wants to move to vertex C along a path
in G, and the robot at B wants to move to vertex D. This movement can be described as
***travel scheduling***: at each time, the travel schedule determines **only one** robot to move through an edge, from a vertex to a neighbor. Finally, the robot from vertex A should be at vertex A, and the robot from B should be at vertex D.

A travel schedule is said to be ***non-jamming*** if at no point in time are the two robots standing at 2 vertices have a distanc ≤ **r**, with a given parameter **r**.

Write a program to input a weighted graph **G**, two vertices starting A and B, two vertices
end C and D, and parameter **r** > 0. Displays a travel schedule if any; if not there is a message ***Cannot found!***.

**Input:**
* The first line is the number of vertices `n` < 100 and the number of edges `m` of graph G.
* The next `m` lines each contain 3 numbers `x`, `y`, `w` representing: Graph G has edges {`x`, `y`} with weight `w`.
* The next line contains four numbers `A`, `B`, `C`, `D` which are the **starting** and **ending** vertices of the 2 robots.
* The last line is the number `r`> 0.

**Output:** 
Includes multiple lines, each line is two numbers `u` and `v` representing the vertices that the two robots stand at each time in the travel schedule.

## Algorithms

## Reference
 
