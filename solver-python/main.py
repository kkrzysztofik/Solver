"""Start point of application"""
from kmk.solver import PuzzleState, SudokuState, AStarSearcher
import sys

try:
    while 1:
        print """
Select mode: 
   1: Sudoku 
   2: Puzzle
   other: Exit"""
        input = int(raw_input())
        if input == 1:
            print "Sudoku selected"
        elif input == 2:
            print "Puzzle selected"
        else:
            print "Exiting"
            break
except:
    print "Unexpected error:", sys.exc_info()[0]