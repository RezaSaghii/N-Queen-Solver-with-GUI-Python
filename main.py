import sys
from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow
from algorithms.backtracking import BacktrackingSolver
from algorithms.genetic import GeneticSolver
from algorithms.csp import CSPSolver

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
