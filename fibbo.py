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
Temp = ''
Page = ''
NumPlaces = 40
for FibNum in range(0,NumPlaces):
    #s = s + '(' + str(m) + ')' + str(getFib(m)) + ' '
    #s = s + str(getFib(m)) + ' '
    Temp = '(' + str(FibNum) + ')' + str(getFib(FibNum)) + ' '
    if len(Line) + len(Temp) > 80:
        #Page = Page + Line
        Page = Page + '\n'
        Line = Temp
    else:
        Line = Line + Temp    
    Page = Page + Line
Vals = Page.split(' ')
Final = Vals[-1*NumPlaces:]
print(Page)