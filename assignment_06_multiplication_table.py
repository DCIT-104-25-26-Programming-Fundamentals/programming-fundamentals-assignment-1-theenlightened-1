# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def print_table(num):
    print("Multiplication Table for " + str(num) + ":")
    i = 1
    while i <= 12:
        print(str(num) + "  x  " + str(i) + "  =  " + str(num * i))
        i = i + 1


def print_tables_1_to_n(n):
    num = 1
    while num <= n:
        print_table(num)
        print("-----------------------------")
        num = num + 1


def part_a():
    print()
    print("--- Part A: Single Table ---")
    num = int(input("Enter a number: "))
    print_table(num)


def part_b():
    print()
    print("--- Part B: Tables from 1 to N ---")
    n = int(input("Enter a number N: "))

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    print_tables_1_to_n(n)


def main():
    part_a()
    part_b()


main()