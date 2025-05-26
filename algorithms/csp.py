from typing import List, Tuple
from constraint import Problem, AllDifferentConstraint
from .base import NQueenSolver

class CSPSolver(NQueenSolver):
    def solve(self) -> List[Tuple[int, int]]:
        problem = Problem()
        variables = range(self.board_size)
        domain = range(self.board_size)
        for var in variables:
            problem.addVariable(var, domain)
        problem.addConstraint(AllDifferentConstraint())
        for i in range(self.board_size):
            for j in range(i + 1, self.board_size):
                problem.addConstraint(
                    lambda x, y, i=i, j=j: abs(x - y) != abs(i - j),
                    (i, j)
                )
        solution = problem.getSolution()
        if solution:
            return [(i, solution[i]) for i in range(self.board_size)]
        return [] 