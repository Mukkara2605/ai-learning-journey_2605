# Pass or fail report (`report.py`): use a list of dictionaries (name, marks). Print `Pass` if marks are 40 or more, otherwise `Fail`, and the number of students who passed.
students = [
    {"name": "Asha", "marks": 88},
    {"name": "Ravi", "marks": 35},
    {"name": "Meena", "marks": 40},
    {"name": "John", "marks": 64},
]
passed = 0 

for s in students:
    if s["marks"] >= 40:
        result = "Pass"
        passed += 1
    else:
        result = "Fail"
    print(f"{s['name']}: {result}")

print(f"Number of students who passed: {passed}")