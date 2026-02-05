# Linear Equation Solver: Systems of Two Variables

A Python module designed to solve systems of linear equations using Cramer's Rule. This project demonstrates modular programming by encapsulating algebraic logic into an importable function that handles both unique and non-unique mathematical solutions.

# 📐 Mathematical Logic

The module solves a system of equations in the following form:

    a1​x+b1​y=c1​

    a2​x+b2​y=c2
    
    
## Determinant Check

Before solving, the program checks the determinant (D):
D=(a1​⋅b2​)−(a2​⋅b1​)

    If D=0, the lines are parallel or coincident, meaning no unique solution exists.

    If D=0, the program calculates x and y using:
    x=Dc1​b2​−c2​b1​​,y=Da1​c2​−a2​c1​​​

## 🛠️ Features

- Error Handling: Detects non-unique solutions and returns a sentinel value (-9999) to prevent program crashes.

 - Modular Design: Optimized to be stored in a local directory and imported into other scripts.

 - Precision: Uses floating-point division for accurate coordinate results.
