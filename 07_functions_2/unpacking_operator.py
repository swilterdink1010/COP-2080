# unpacking_operator.py
a_tuple = (1,2,3,4,5,6,7)
a_list = [22,33,44,55]
def some_dict():
  a_dict = {'abe': 123, 'doe': 345, 'ken': 789}
  return a_dict
print(*a_tuple)
print(*a_list)
print(*some_dict())