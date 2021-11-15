# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 12:56:08 2021

@author: Nares
"""
import copy


def n_queens(n = 8):
    """"
    Solve the n queens problem of placing n non-attacking queens on an n-by-n
    chessboard. The return value is an array for which each element is a
    solution (i.e. a configuration of n queens on the board) to the problem.
    """
    
    def is_solution(state, n):
        stage = state["stage"]
        
        # Considering that the state is always viable for it to reach this
        # function, the state will be a solution simply when the stage equals n 
        if stage != n:
            return False
        
        return True

    def is_viable(state, n):
        board = state["board"]
        stage = state["stage"]
        
        column_latest_row = board[stage - 1].index("Q")
        
        # Check if the latest addition of a queen resulted in that queen facing 
        # a queen on another row
        for i in range(stage - 1):
            column_current_row = board[i].index("Q")
            
            # Check if the two queens are on the same column
            if column_current_row == column_latest_row:
                return False
            
            # Check if the two queens are on the same diagonal
            if (i + column_current_row == stage - 1 + column_latest_row or
                i - column_current_row == stage - 1 - column_latest_row):
                return False
            
        return True
        
    # Initialize an empty board
    board = [["." for j in range(n)] for i in range(n)]
    
    # The stage is the number of queens on the board, which initially equals 0
    stage = 0
    
    # Initialize a stack and a solutions array
    stack = []
    solutions =  []
    
    # The initial state is added to the stack
    stack.append({"board": board, "stage": stage})
    
    while stack != []:
        # Pop an element from the stack and set it as the current state
        current = stack.pop(-1)
        
        # If the current state is a solution, add it to the solutions array
        if is_solution(current, n):
            solutions.append(current["board"])
            
        if current["stage"] < n:
            next_row = current["stage"]
            
            # Check if the board is still viable when adding a queen at each of
            # the indices in the next row one at a time
            for j in range(n):
                new = copy.deepcopy(current)
                new["board"][next_row][j] = "Q"
                new["stage"] += 1
                
                if is_viable(new, n):
                    stack.append(new)
                    
    return solutions
                    

n = 8
solutions = n_queens(n)      