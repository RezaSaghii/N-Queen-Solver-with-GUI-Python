from abc import ABC, abstractmethod
from typing import List, Tuple

class NQueenSolver(ABC):
    def __init__(self, board_size: int):
        self.board_size = board_size
    @abstractmethod
    def solve(self) -> List[Tuple[int, int]]:
        pass
    @staticmethod
    def is_valid_solution(queen_positions: List[Tuple[int, int]]) -> bool:
        if len(queen_positions) != len(queen_positions):
            return False
        for i in range(len(queen_positions)):
            for j in range(i + 1, len(queen_positions)):
                r1, c1 = queen_positions[i]
                r2, c2 = queen_positions[j]
                if r1 == r2:
                    return False
                if c1 == c2:
                    return False
                if abs(r1 - r2) == abs(c1 - c2):
                    return False
        return True 