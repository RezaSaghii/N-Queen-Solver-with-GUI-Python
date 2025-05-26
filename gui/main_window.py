from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QSpinBox, QLabel, QGridLayout
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QColor, QPen
from typing import List, Tuple
import sys
import time
from algorithms.backtracking import BacktrackingSolver
from algorithms.genetic import GeneticSolver
from algorithms.csp import CSPSolver

class ChessBoard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.queen_positions: List[Tuple[int, int]] = []
        self.board_size = 8
        self.setMinimumSize(400, 400)
    def set_positions(self, positions: List[Tuple[int, int]]):
        self.queen_positions = positions
        self.update()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        cell_size = min(self.width(), self.height()) / self.board_size
        for row in range(self.board_size):
            for col in range(self.board_size):
                x = col * cell_size
                y = row * cell_size
                color = QColor(240, 217, 181) if (row + col) % 2 == 0 else QColor(181, 136, 99)
                painter.fillRect(int(x), int(y), int(cell_size), int(cell_size), color)
                if (row, col) in self.queen_positions:
                    painter.setPen(QPen(Qt.GlobalColor.black, 2))
                    painter.setBrush(QColor(255, 0, 0))
                    painter.drawEllipse(int(x + cell_size * 0.2), int(y + cell_size * 0.2), int(cell_size * 0.6), int(cell_size * 0.6))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("N-Queen Solver")
        self.setMinimumSize(600, 500)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        controls_layout = QHBoxLayout()
        size_layout = QHBoxLayout()
        size_label = QLabel("Board Size:")
        self.size_spinbox = QSpinBox()
        self.size_spinbox.setRange(4, 20)
        self.size_spinbox.setValue(8)
        size_layout.addWidget(size_label)
        size_layout.addWidget(self.size_spinbox)
        algo_layout = QHBoxLayout()
        algo_label = QLabel("Algorithm:")
        self.algo_combo = QComboBox()
        self.algo_combo.addItems(["Backtracking", "Genetic", "CSP"])
        algo_layout.addWidget(algo_label)
        algo_layout.addWidget(self.algo_combo)
        self.solve_button = QPushButton("Solve")
        self.solve_button.clicked.connect(self.solve)
        controls_layout.addLayout(size_layout)
        controls_layout.addLayout(algo_layout)
        controls_layout.addWidget(self.solve_button)
        self.chess_board = ChessBoard()
        layout.addLayout(controls_layout)
        layout.addWidget(self.chess_board)
        self.statusBar().showMessage("Ready")
    def solve(self):
        board_size = self.size_spinbox.value()
        self.chess_board.board_size = board_size
        algo = self.algo_combo.currentText()
        if algo == "Backtracking":
            solver = BacktrackingSolver(board_size)
        elif algo == "Genetic":
            solver = GeneticSolver(board_size)
        else:
            solver = CSPSolver(board_size)
        start_time = time.time()
        solution = solver.solve()
        end_time = time.time()
        if solution:
            self.chess_board.set_positions(solution)
            self.statusBar().showMessage(f"Solution found in {end_time - start_time:.2f} seconds")
        else:
            self.statusBar().showMessage("No solution found") 