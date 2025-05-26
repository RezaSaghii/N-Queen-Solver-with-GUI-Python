from typing import List, Tuple
from .base import NQueenSolver

class BacktrackingSolver(NQueenSolver):
    
    def solve(self) -> List[Tuple[int, int]]:

        def is_safe(row: int, col: int, board: List[int]) -> bool:
            for i in range(row):
                if board[i] == col:
                    return False
                if abs(board[i] - col) == abs(i - row):
                    return False
            return True
            
        def solve_util(row: int, board: List[int]) -> bool:
            if row == self.board_size:
                return True
                
            for col in range(self.board_size):
                if is_safe(row, col, board):
                    board[row] = col
                    if solve_util(row + 1, board):
                        return True
                    board[row] = -1
            return False
            
        board = [-1] * self.board_size
        
        if solve_util(0, board):
            return [(i, board[i]) for i in range(self.board_size)]
        return [] 