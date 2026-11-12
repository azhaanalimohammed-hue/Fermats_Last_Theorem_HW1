

# ============================================================
# Program Title: Fermat's Last Theorem - Near Misses
# File Name: fermat_near_misses.py
#
# Programmer: Mohammed Azhaan Ali
# Email Address: azhaanalimohammed@lewisu.edu
#
# Course: CPSC 44000 - Software Engineering
# Section:  N/A (No separate course section)
# Date Completed: 11-11-2026
#
# External Files Required: None
# External Files Created: None
#
# Program Description:
# This program searches for near misses of Fermat's Last
# Theorem using positive integers x, y, and z.
#
# The user enters a power n (3 through 11) and an upper
# limit k (greater than 10). The program systematically
# tests combinations of x and y from 10 through k.
#
# For each combination, it calculates x^n + y^n and
# identifies the closest integer power z^n.
#
# It calculates the actual miss and relative miss,
# displays each new smallest relative miss, and
# prints the best result after completing the search.
#

# Resources Used:
# 1. Software Engineering Assignment 1 (HW1) instructions,
#    Lewis University, CPSC 44000.
#
# 2. Python Software Foundation - Python 3 Documentation
#    https://docs.python.org/3/
#
# 3. Python Software Foundation - Built-in Functions
#    https://docs.python.org/3/library/functions.html
#
# 4. GeeksforGeeks - Binary Search Algorithm
#    https://www.geeksforgeeks.org/dsa/binary-search/
#
# 5. Encyclopaedia Britannica - Fermat's Last Theorem
#    https://www.britannica.com/science/Fermats-last-theorem
#
# 6. Python Software Foundation - Control Flow Tools
#    https://docs.python.org/3/tutorial/controlflow.html

# 
#
# ============================================================


def get_integer(prompt, minimum, maximum=None):
    """Ask the user for an integer within the allowed range."""
    # Keep requesting input until the user enters a valid integer
# that satisfies the required minimum value.
    while True:
        try:
            # Read the user's input and convert it to an integer.
            value = int(input(prompt))

            if value < minimum:
                print(f"Please enter a number >= {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Please enter a number <= {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def find_near_misses(n, k):
    """Find and display new smallest relative misses."""

    # Track the smallest relative miss found so far.
    best_relative_miss = None
    
# Store the values associated with the smallest relative miss found.
# None indicates that no candidate has been evaluated yet.
    best_result = None

    # Search all allowed values of x.
    for x in range(10, k + 1):

        # Search all allowed values of y.
        for y in range(10, k + 1):

            # Calculate the sum of the two powers.
            target = x ** n + y ** n

            # Find the largest integer z with z^n <= target.
            # Set the lower and upper bounds for the binary search.
            low = 1
            high = 2 * k + 1

            # Binary search avoids floating-point rounding errors.
            while low < high:
                # Calculate the midpoint of the current search interval.
                middle = (low + high + 1) // 2

                if middle ** n <= target:
                    low = middle
                else:
                    high = middle - 1
# Identify the two neighboring integer values whose powers
# may be closest to the calculated target.
            lower_z = low
            upper_z = lower_z + 1

            # Calculate the distance to each neighboring power.
            lower_miss = target - lower_z ** n
            upper_miss = upper_z ** n - target

            # Select the closer integer power.
            if lower_miss <= upper_miss:
                z = lower_z
                actual_miss = lower_miss
            else:
                z = upper_z
                actual_miss = upper_miss

            # Calculate the relative miss.
            relative_miss = actual_miss / target

            # Display a result only when a new record is found.
            if (best_relative_miss is None or
                    relative_miss < best_relative_miss):

                best_relative_miss = relative_miss
 # Save the current combination and its actual miss
# because it improves the smallest relative miss.
                best_result = (x, y, z, actual_miss)

                print(
                    f"x={x}, y={y}, z={z}, "
                    f"actual miss={actual_miss}, "
                    f"relative miss={relative_miss:.10%}"
                )

   
    print("\n========== FINAL BEST RESULT ==========")
    print(f"Power (n): {n}")
    print(f"Upper limit (k): {k}")
    print(f"Best x: {best_result[0]}")
    print(f"Best y: {best_result[1]}")
    print(f"Best z: {best_result[2]}")
    print(f"Actual miss: {best_result[3]}")
    print(f"Smallest relative miss: {best_relative_miss:.10%}")


def main():
    """Collect the parameters for the near-miss search."""
    print("======================================")
    print(" Fermat's Last Theorem - Near Misses")
    print("======================================")
# Get the exponent n and the upper search limit k
# from the user after validating both inputs.
    n = get_integer("Enter n (3 to 11): ", 3, 11)
    k = get_integer("Enter k (greater than 10): ", 11)

    print("\nInput values accepted!")
    print(f"Power (n): {n}")
    print(f"Upper limit (k): {k}")


    print("\nSearching for near misses...\n")
    find_near_misses(n, k)

if __name__ == "__main__":
    main()
