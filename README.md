# fibbo.py by Dan Rhea 1/24/2025

## python3 fibbo.py [HowMany(100) [LineLen(80)]]

Fibbo contains a function getFib that given a number indicating which
fibonacci number you wish to see will display that number without using 
looping or recursion.

Also included is a calling routine that loops through the
function 1 to n fibonacci numbers.

Here is the actual function. It uses Binet's Formula. The formula can be found here "https://en.wikipedia.org/wiki/Fibonacci_sequence".

Modified 3/15/2025 to use the "if __name__ == "__main__" construct.

Added uv package managment to the project. Also added the rich package.

```python3
def getFib(n) -> int:
    """
    Given which fibonacci number we want, calculate its value.
    """
    left_side: complex = (1 / cmath.sqrt(5)) * pow(((1 + cmath.sqrt(5)) / 2), n)
    right_side: complex = (1 / cmath.sqrt(5)) * pow(((1 - cmath.sqrt(5)) / 2), n)
    fib_value: complex = left_side-right_side
    # coerce complex to real so we can round the complex result and return
    # the result as an int.
    fn: int = round(fib_value.real)
    return int(fn)
```

Example rum:

```text
> python3 fibbo.py 100 80
python3 fibbo.py [HowMany(100) [LineLen(80)]]
 HowMany: 100
 LineLen: 80
(0): 0 (1): 1 (2): 1 (3): 2 (4): 3 (5): 5 (6): 8 (7): 13 (8): 21 (9): 34
(10): 55 (11): 89 (12): 144 (13): 233 (14): 377 (15): 610 (16): 987 (17): 1597
(18): 2584 (19): 4181 (20): 6765 (21): 10946 (22): 17711 (23): 28657
(24): 46368 (25): 75025 (26): 121393 (27): 196418 (28): 317811 (29): 514229
(30): 832040 (31): 1346269 (32): 2178309 (33): 3524578 (34): 5702887
(35): 9227465 (36): 14930352 (37): 24157817 (38): 39088169 (39): 63245986
(40): 102334155 (41): 165580141 (42): 267914296 (43): 433494437
(44): 701408733 (45): 1134903170 (46): 1836311903 (47): 2971215073
(48): 4807526976 (49): 7778742049 (50): 12586269025 (51): 20365011074
(52): 32951280099 (53): 53316291173 (54): 86267571272 (55): 139583862445
(56): 225851433717 (57): 365435296162 (58): 591286729879 (59): 956722026041
(60): 1548008755920 (61): 2504730781961 (62): 4052739537881
(63): 6557470319842 (64): 10610209857723 (65): 17167680177565
(66): 27777890035288 (67): 44945570212853 (68): 72723460248141
(69): 117669030460994 (70): 190392490709135 (71): 308061521170129
(72): 498454011879264 (73): 806515533049393 (74): 1304969544928657
(75): 2111485077978050 (76): 3416454622906706 (77): 5527939700884756
(78): 8944394323791463 (79): 14472334024676218 (80): 23416728348467676
(81): 37889062373143896 (82): 61305790721611584 (83): 99194853094755488
(84): 160500643816367040 (85): 259695496911122528 (86): 420196140727489600
(87): 679891637638612096 (88): 1100087778366101632 (89): 1779979416004713728
(90): 2880067194370815488 (91): 4660046610375529472 (92): 7540113804746344448
(93): 12200160415121872896 (94): 19740274219868217344
(95): 31940434634990092288 (96): 51680708854858301440
(97): 83621143489848410112 (98): 135301852344706695168
(99): 218922995834555138048 (100): 354224848179261800448
```