# list_comp1.py
list_ = [(x, y) for x in ['a', 'b', 'c'] for y in ['first','b', 3] if x != y]
print(*list_)