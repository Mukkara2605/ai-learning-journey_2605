students = [
    {"name": "Asha", "marks": 82},
    {"name": "Ravi", "marks": 35},
    {"name": "Meena", "marks": 91},
    {"name": "John", "marks": 58},
]

sorted_students = sorted(students, key=lambda x: x["marks"], reverse=True)
for student in sorted_students:
    print(f"{student['name']}: {student['marks']}")
    
passed_students = list(filter(lambda x:x["marks"] >= 40, students))
for student in passed_students:
    print(f"{student['name']} passed with marks: {student['marks']}")