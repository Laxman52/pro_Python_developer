# Tuples are very easy.
# A tuple is similar to a list: it can store heterogeneous (different) data types,
# BUT unlike lists, tuples are **immutable** (cannot be changed after creation).

# Creating a tuple without parentheses
a = 10, 92, 23
print(type(a))  # Output: <class 'tuple'>

# Creating a tuple with parentheses (recommended)
a = (10, 203, 45, 78, 456)
print(a)  # Output: (10, 203, 45, 78, 456)

# Trying to change a value in the tuple (will raise an error because tuples are immutable)
# a[0] = 3545  # ❌ This will cause an error: TypeError: 'tuple' object does not support item assignment

# Tuple methods:
# - len(): returns the length of the tuple
# - min() / max(): return the minimum / maximum values in the tuple (only for comparable elements)
# - count(): returns how many times an element appears
# - index(): returns the index of the first occurrence of an element
# - sorted(): returns a sorted list (not a tuple)

b = (1, 2, 4, 5, 6, 7, 5)

print(b[0])       # ✅ Output: 1
print(len(b))     # ✅ Output: 7
print(min(b))     # ✅ Output: 1
print(max(b))     # ✅ Output: 7
print(b.count(5)) # ✅ Output: 2
print(b.index(4)) # ✅ Output: 2
print(sorted(b))  # ✅ Output: [1, 2, 4, 5, 5, 6, 7] => Notice this is a list, not a tuple


print(b[0:4:1])


# use tuple to store the data which not changes any time , if have data that changes then use list to store it
