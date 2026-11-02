def grade_func(score, pass_marks = 40):
    if score < pass_marks:
        return "Fail"
    elif score >=90:
        return "A"
    elif score >= 75:
        return "B"
    else:
        return "C"
    
if __name__ == "__main__":
    print(grade_func(85))  # Output: B
    print(grade_func(92))  # Output: A
    print(grade_func(35))  # Output: Fail
    print(grade_func(70))  # Output: C