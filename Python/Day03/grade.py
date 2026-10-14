# Grade checker (grade.py): ask for marks and print A (90+), B (75+), C (50+) or Fail.
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")