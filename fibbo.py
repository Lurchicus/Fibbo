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

def getFib(n):
    """
    Given which fibonacci number we want, calculate its value.
    """
    lsa = (1 / cmath.sqrt(5)) * pow(((1 + cmath.sqrt(5)) / 2), n)
    rsa = (1 / cmath.sqrt(5)) * pow(((1 - cmath.sqrt(5)) / 2), n)
    fib = lsa-rsa
    #coerce to real so we can round the complex result
    fn = round(fib.real)
    return int(fn)


def main():
    """
    Main routine to demonstrate the getFib function.
    """
    #Demo using the function
    NumPlaces = 100
    WrapAt = 80
    #print(sys.argv)
    if len(sys.argv) == 3:
        NumPlaces = int(sys.argv[1])
        WrapAt = int(sys.argv[2])
    elif len(sys.argv) == 2:
        NumPlaces = int(sys.argv[1])
        WrapAt = 80
    print("python3 fibbo.py [HowMany(100) [LineLen(80)]]")
    print(" HowMany: " + str(NumPlaces))
    print(" LineLen: " + str(WrapAt))
    Line = ''
    Fibb = ''
    Page = ''
    for FibNum in range(0,NumPlaces+1):
        Fibb = "(" + str(FibNum) + "): " + str(getFib(FibNum)) + " "
        if len(Line) + len(Fibb) >= WrapAt:
            Line += "\n"
            Page += Line
            Line = Fibb
        else:
            Line += Fibb
    if len(Fibb) > 0:
        if len(Line) + len(Fibb) >= WrapAt:
            Page += Line + "\n"
            Line = Fibb
            Fibb = ''
        else:
            Page += Line + "\n"
    # This keeps printing a leading "a" after the first line.
    # Not sure why.
    print(Page)


if __name__ == "__main__":
    main()