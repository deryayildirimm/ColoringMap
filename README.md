# ColoringMap

## Problem 

The problem is coloring the given map with 4 different color(red, green, blue, yellow) and adjacent countries not be the same color.

## Algorithm

To solve the problem, Backtracking Search Algorithm been used. 

Backtracking is the approach to solve the problem by testing all possible combinations. If any subproblem does not fit the given constraint then we discard the complete subproblem (backtrack), moves a step back then try other remaining possible combinations.

Program assign a color to each node, either randomly or choosing the next available color in the list, and if there is a conflict undoes the step and tries another solution. Keeps doing this until it finds a solution. It is guaranteed to find a solution if it is available. 
 
A paint_map function, uses backtracking search algorithm to color the regions such that no two regions share the same color. It takes a graph of neighborhood as input and gives a map of name to colors as result. 

There are multiple solutions to this kind of problems, colors chosen randomly in the implementation to see different results. To see a different colored map, rerun the program. 

plotly module is used to visualize the result. 

