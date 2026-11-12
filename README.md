
# Fermat's Last Theorem - Near Misses

## Software Engineering Assignment 1

**Course:** CPSC 60500 - Software Engineering  
**Programmer:** Mohammed Azhaan Ali  
**Language:** Python 3

## Project Description

This program searches for near misses of Fermat's Last
Theorem by examining combinations of positive integers.

Fermat's Last Theorem states that there are no positive
integers x, y, and z satisfying:

x^n + y^n = z^n

for any integer n greater than 2.

The program searches for combinations where the two
sides are as close as possible.

## Program Features

- Accepts user input for n and k.
- Validates the input values.
- Searches combinations of x and y from 10 to k.
- Finds the closest integer power of z.
- Calculates actual and relative misses.
- Displays each new smallest relative miss.
- Prints the final best result.

## Requirements

- Python 3.10 or newer
- No external Python libraries required

## How to Run

1. Open a terminal in the project folder.
2. Run:

   py fermat_near_misses.py

3. Enter n (3 through 11).
4. Enter k (greater than 10).
5. Review the results displayed in the terminal.

On systems where Python is available as `python3`,
use `python3 fermat_near_misses.py` instead.

## Running the Windows Executable

The project also includes a standalone Windows executable.

1. Download or clone the GitHub repository.
2. Open PowerShell in the downloaded project folder.
3. Run the following command:

```powershell
.\fermat_near_misses.exe
```

4. Enter n (3 through 11) and k (greater than 10).
5. The program will display the near-miss results and the final smallest relative miss.

The executable does not require a separate Python installation.

## Example

Input:
n = 3
k = 20

Final result:
x = 18
y = 20
z = 24
Actual miss = 8
Relative miss = 0.0578368999%

## Files

- fermat_near_misses.py - Python source code
- README.md - Project documentation
- fermat_near_misses.exe - Windows executable
  (provided after packaging)

## Notes

The program uses Python's arbitrary-precision integers
to handle large calculations. Larger k values may
require more processing time.

## References

- Lewis University Software Engineering HW1 instructions
- Python 3 Documentation: https://docs.python.org/3/
- Fermat's Last Theorem mathematical background
