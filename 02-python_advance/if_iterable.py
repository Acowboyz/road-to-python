from collections import Iterable

print(isinstance("abc", Iterable))

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance(100, Iterable))
