# https://coderraj07.medium.com/python-gotchas-and-tricky-questions-6b76f0c36c40

"""
1. Default mutable arguments are created once, not every function call.
"""

# def f(x, lst=[]):
#     lst.append(x)
#     return lst

# print(f(1))  # [1]
# print(f(2))  # [1, 2]

# ----------------------------#

"""
2. '*' operator replicates references, not copies.
"""

# lst = [[0]*3]*3
# lst[0][0] = 1
# print(lst)  # [[1,0,0],[1,0,0],[1,0,0]]

# -----------------------------#

"""
3. The '==' checks for equality of value while the 'is' keyword checks for object identity.
In simple terms: '==' answers "Do these two variables have the same data inside?", while 'is' answers "Do these two variables point to the exact same place in memory?".

But remember to always use 'is' when comparing anything with 'None'
"""

# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# print(l1 == l2)  # True
# print(l1 is l2)  # False

# l3 = l1
# print(l1 == l3)  # True
# print(l1 is l3)  # True

# -----------------------------#
"""
4. In a Dictionary, only a few types can become a key or in other words, are hashable.

Hashable: immutable types (int, float, str, tuple of immutables)
Unhashable: mutable types (list, dict, set)

Means any type that is 'mutable' cannot become a key for a dict.
"""
# d = {}
# d[[1,2,3]] = "hi"  # Error: unhashable type: 'list'
# d[(1,2,3)] = "hi"  # Works

# -----------------------------#
"""
5. There is a concept of Integer Caching in Python where Python caches small integers(-5 to 256). Large numbers are new objects.

This means that when we type 256, Python points a and b to that single pre-made memory spot, so 'a is b' is True.

Warning: BTW, this is not necessarily true. It also depends on how you're running the program. If this code is written in a .py file then both will return 'True'. If these are separate lines in a REPL terminal then the concept applies.

This is the reason why two integers should never be compared using 'is'.
"""
# a = 256
# b = 256
# print(a is b)  # True

# c = 257
# d = 257
# print(c is d)  # False


# -----------------------------#
"""
6. Floating point precision is a problem in Python because computers store these numbers like 0.3 as 0.300000000004 which is why their direct equality takes a hit.

In order to overcome this problem, one should use the built-in Decimal module.

Note: The Decimal function would work only if we pass a string of the floating-point number.
"""

# print(0.1 + 0.2 == 0.3)  # False

# from decimal import Decimal

# a = Decimal("0.1")
# b = Decimal("0.2")
# c = Decimal("0.3")

# print(a + b == c)  # True

# -----------------------------#
"""
"""

# -----------------------------#
"""
"""

# -----------------------------#
"""
"""

# -----------------------------#
"""
"""

# -----------------------------#
"""
"""

# -----------------------------#
"""
"""

# -----------------------------#
"""
"""

# -----------------------------#
"""
"""
# -----------------------------#
