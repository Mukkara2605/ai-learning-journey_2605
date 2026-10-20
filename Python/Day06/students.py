students = [
    {"name": "Asha", "marks": 88},
    {"name": "Ravi", "marks": 72},
    {"name": "Meena", "marks": 95},
    {"name": "John", "marks": 64},
]

total = 0
top_name = ""
top_marks = 0

print("Students:")
for s in students:
    print(s["name"])
    total += s["marks"]
    if s["marks"] > top_marks:
        top_marks = s["marks"]
        top_name = s["name"]

average = total / len(students)

print(f"Class average: {average:.2f}")
print(f"Top scorer: {top_name} ({top_marks})")