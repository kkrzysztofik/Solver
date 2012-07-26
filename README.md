Solver
======

Simple program designed to solve Puzzle 2^n-1 and Sudoku problems.

Structure:
----------
 - AbstractState.py - Abstract class for problems being solved
 - AbstractSeacher.py - Abstract class for searching/solving algorithms
 - AStarSearcher.py - Implementation of AStar graph algorithm
 - PuzzleState.py - Implementation of Puzzle 2^n-1 problem
 - SudokuSlot.py - Helper class for Sudoku problem
 - SudokuState.py - Implementation of Sudoku problem
 - main.py - Start point of application

Sources:
--------
 - Klesk P.: Algorytmy przeszukiwania grafow i drzew dla gier i lamiglowek, [online] 
   http://www.wikizmsi.zut.edu.pl/uploads/b/be/2_search.pdf                          
 - Norvig P.: Solving Every Sudoku Puzzle, [online] - http://norvig.com/sudoku.html  
 - Wade M.: A* Sudoku Solver, [online]                                               
   http://iammyownorg.org/wp-content/uploads/2009/03/mjw-sudokusolver-astar.pdf    