# fibbo.py by Dan Rhea 1/24/2025

## python3 fibbo.py [HowMany(100) [LineLen(80)]]

Fibbo contains a function getFib that given a number indicating which
fibonacci number you wish to see will display that number without using 
looping or recursion.

Also included is a calling routine that loops through the
function 1 to n fibonacci numbers.

Here is the actual function. I will try to track down the original formula. The formula came from an article I read on the internet that I have not been able to find since. It can also be found in a Wikipedia article (link to be added once I find it).

```
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
```