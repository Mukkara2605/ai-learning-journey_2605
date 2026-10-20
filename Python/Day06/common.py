# Common friends (common.py): with two sets of names, print who is in both, and who is only in the first.
friends1 = {"Alice", "Bob", "Charlie", "David"}
friends2 = {"Charlie", "David", "Eve", "Frank"}
common_friends = friends1.intersection(friends2)
only_in_first = friends1.difference(friends2)
print("Common friends:", common_friends)
print("Only in first set:", only_in_first)