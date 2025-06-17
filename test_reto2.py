from reto2 import is_authentic_skewer
import sys

test_cases = [
    ("B--A--N--A--N--A--S", True),
    ("A--X--E", False),
    ("C-L-A-P", False),
    ("M--A---T-E-S", False),
]

all_passed = True
for s, expected in test_cases:
    result = is_authentic_skewer(s)
    print(f"Input: {s}, Output: {result}, Expected: {expected}")
    if result != expected:
        all_passed = False

if not all_passed:
    sys.exit(1)
