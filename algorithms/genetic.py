import random
from typing import List, Tuple
import numpy as np
from .base import NQueenSolver

class GeneticSolver(NQueenSolver):
    def __init__(self, board_size: int, population_size: int = 100, generations: int = 1000, mutation_rate: float = 0.1):
        super().__init__(board_size)
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
    def _create_individual(self) -> List[int]:
        return random.sample(range(self.board_size), self.board_size)
    def _fitness(self, individual: List[int]) -> int:
        score = 0
        for i in range(len(individual)):
            for j in range(i + 1, len(individual)):
                if abs(individual[i] - individual[j]) != abs(i - j):
                    score += 1
        return score
    def _crossover(self, parent1: List[int], parent2: List[int]) -> List[int]:
        point = random.randint(0, self.board_size - 1)
        child = parent1[:point] + parent2[point:]
        return child
    def _mutate(self, individual: List[int]) -> List[int]:
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(self.board_size), 2)
            individual[i], individual[j] = individual[j], individual[i]
        return individual
    def solve(self) -> List[Tuple[int, int]]:
        population = [self._create_individual() for _ in range(self.population_size)]
        for _ in range(self.generations):
            fitness_scores = [self._fitness(ind) for ind in population]
            for ind in population:
                solution = [(i, ind[i]) for i in range(self.board_size)]
                if self.is_valid_solution(solution):
                    return solution
            new_population = []
            best_idx = fitness_scores.index(max(fitness_scores))
            new_population.append(population[best_idx])
            while len(new_population) < self.population_size:
                tournament = random.sample(range(self.population_size), 3)
                parent1 = population[max(tournament, key=lambda i: fitness_scores[i])]
                tournament = random.sample(range(self.population_size), 3)
                parent2 = population[max(tournament, key=lambda i: fitness_scores[i])]
                child = self._crossover(parent1, parent2)
                child = self._mutate(child)
                new_population.append(child)
            population = new_population
        return [] 