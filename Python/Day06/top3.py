# Top 3 scores (top3.py): ask for scores separated by spaces and print the three highest.
scores = input("Enter scores separated by spaces: ")
score_list = [int(score) for score in scores.split()]
#print("Top 3 scores:", sorted(score_list, reverse=True)[:3])
sorted_scores = sorted(score_list)
top_scores = reversed(sorted_scores)
top_three = list(top_scores)[:3]
print("Top 3 scores:", top_three)