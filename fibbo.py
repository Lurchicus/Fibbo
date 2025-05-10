"""
fibbo.py by Dan Rhea

Fibbo contains a function getFib that given a number indicating which
fibonacci number you wish to see will display that number without using 
looping or recursion.

Also included is a calling routine that loops through the
function 1 to 10 digit fibonacci numbers.
"""

import cmath
import sys
from rich import print

def getFib(n) -> int:
    """
    Given which fibonacci number we want, calculate its value.
    """
    left_side: complex = (1 / cmath.sqrt(5)) * pow(((1 + cmath.sqrt(5)) / 2), n)
    right_side: complex = (1 / cmath.sqrt(5)) * pow(((1 - cmath.sqrt(5)) / 2), n)
    fib_value: complex = left_side-right_side
    # coerce complex to real so we can round the complex result and rerurn
    # the result as an int.
    fn: int = round(fib_value.real)
    return int(fn)


def main():
    """
    Main routine to demonstrate the getFib function.
    """
    # Demo using the function...
    # Process command line arguments
    num_places: int = 100
    wrap_at: int = 80
    if len(sys.argv) == 3:
        num_places = int(sys.argv[1])
        wrap_at = int(sys.argv[2])
    elif len(sys.argv) == 2:
        num_places = int(sys.argv[1])
        wrap_at = 80
    print("python3 fibbo.py [HowMany(100) [LineLen(80)]]")
    print(f" HowMany: {str(num_places)}")
    print(f" LineLen: {str(wrap_at)}")
    # Collect results into a "page". This is not really for pagination,
    # it's actually to line wrap large output strings.
    line: str = ''
    fibb: str = ''
    page: str = ''
    for fibb_num in range(0,num_places+1):
        fibb = "(" + str(fibb_num) + "): " + str(getFib(fibb_num)) + " "
        if len(line) + len(fibb) >= wrap_at:
            line += "\n"
            page += line
            line = fibb
        else:
            line += fibb
    if len(fibb) > 0:
        if len(line) + len(fibb) >= wrap_at:
            page += line + "\n"
            line = fibb
            fibb = ''
        else:
            page += line + "\n"
    print(page)


if __name__ == "__main__":
    main()