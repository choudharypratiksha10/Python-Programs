#35. Remove empty tuple(s) from list of tuples

lst = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
result = [t for t in lst if t]
print(result)