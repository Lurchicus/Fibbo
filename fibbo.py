"""
fibbo.py by Dan Rhea

Fibbo contains a function getFib that given a number indicating which
fibonacci number you wish to see will display that number without using 
looping or recursion.

Also included is a calling routine that loops through the
function 1 to 10 digit fibonacci numbers.
"""

import cmath

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


#Demo using the function
Line = ''
Fibb = ''
Page = ''
NumPlaces = 100
for FibNum in range(0,NumPlaces+1):
    Fibb = "(" + str(FibNum) + "): " + str(getFib(FibNum)) + " "
    if len(Line) + len(Fibb) >= 80:
        Line += "\na"
        Page += Line
        Line = Fibb
    else:
        Line += Fibb
if len(Fibb) > 0:
    if len(Line) + len(Fibb) >= 80:
        Page += Line + "\n"
        Line = Fibb
        Fibb = ''
    else:
        Page += Line + "\n"
# This keeps printing a leading "a" after the first line. 
# Not sure why.
print(Page) 