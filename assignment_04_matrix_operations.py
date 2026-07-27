# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols, label):
    matrix = []
    row_num = 1
    while row_num <= rows:
        line = input("Enter row " + str(row_num) + label + ": ")
        values = line.split()
        row = []
        for v in values:
            row.append(int(v))
        matrix.append(row)
        row_num = row_num + 1
    return matrix


def print_matrix(matrix, title):
    print(title)
    for row in matrix:
        line = ""
        for value in row:
            line = line + str(value) + "  "
        print(line)
    print()


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(0)
        result.append(new_row)

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)

    return result


def multiply_matrices(matrix_a, matrix_b):
    m = len(matrix_a)
    n = len(matrix_b)
    p = len(matrix_b[0])

    result = []
    for i in range(m):
        new_row = []
        for j in range(p):
            total = 0
            for k in range(n):
                total = total + matrix_a[i][k] * matrix_b[k][j]
            new_row.append(total)
        result.append(new_row)

    return result


def part_a_transpose():
    print()
    print("--- Part A: Transpose a Matrix ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols, "")

    print_matrix(matrix, "Original Matrix:")
    transposed = transpose_matrix(matrix)
    print_matrix(transposed, "Transposed Matrix:")


def part_b_addition():
    print()
    print("--- Part B: Add Two Matrices ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Matrix A:")
    matrix_a = read_matrix(rows, cols, " of A")
    print("Matrix B:")
    matrix_b = read_matrix(rows, cols, " of B")

    print_matrix(matrix_a, "Matrix A:")
    print_matrix(matrix_b, "Matrix B:")
    result = add_matrices(matrix_a, matrix_b)
    print_matrix(result, "A + B:")


def part_c_multiplication():
    print()
    print("--- Part C: Multiply Two Matrices ---")
    m = int(input("Enter rows of A: "))
    n = int(input("Enter columns of A (must equal rows of B): "))
    p = int(input("Enter columns of B: "))

    print("Matrix A:")
    matrix_a = read_matrix(m, n, " of A")
    print("Matrix B:")
    matrix_b = read_matrix(n, p, " of B")

    print_matrix(matrix_a, "Matrix A:")
    print_matrix(matrix_b, "Matrix B:")
    result = multiply_matrices(matrix_a, matrix_b)
    print_matrix(result, "A x B:")


def main():
    while True:
        print("Matrix Operations")
        print("1. Transpose a Matrix")
        print("2. Add Two Matrices")
        print("3. Multiply Two Matrices")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            part_a_transpose()
        elif choice == "2":
            part_b_addition()
        elif choice == "3":
            part_c_multiplication()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")
            print()


main()