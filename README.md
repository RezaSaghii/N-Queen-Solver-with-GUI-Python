# N-Queen Solver

A Python application that solves the N-Queen problem using three different algorithms:

- Backtracking
- Genetic Algorithm
- Constraint Satisfaction Problem (CSP)

## Features

- Interactive GUI with a chess board visualization
- Support for different board sizes (4x4 to 20x20)
- Multiple solving algorithms to choose from
- Real-time solution visualization
- Performance timing for each solution

## Requirements

- Python 3.8 or higher
- PyQt6
- numpy
- python-constraint

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd nqueen
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

1. Select the desired board size using the spin box
2. Choose an algorithm from the dropdown menu
3. Click "Solve" to find a solution
4. The solution will be displayed on the chess board
5. The status bar will show the time taken to find the solution

## Algorithm Details

### Backtracking

- Uses a systematic search approach
- Guarantees finding a solution if one exists
- Best for smaller board sizes

### Genetic Algorithm

- Uses evolutionary principles to find solutions
- May not always find the optimal solution
- Good for larger board sizes
- Uses tournament selection and mutation

### CSP (Constraint Satisfaction Problem)

- Uses constraint programming to find solutions
- Efficient for medium-sized boards
- Guarantees finding a solution if one exists

## Project Structure

```
nqueen/
├── algorithms/
│   ├── base.py
│   ├── backtracking.py
│   ├── genetic.py
│   └── csp.py
├── gui/
│   └── main_window.py
├── main.py
├── requirements.txt
└── README.md
```
