def calculate_grade(marks):
    if marks > 90:
        return "A+"
    elif marks > 80:
        return "A"
    elif marks > 70:
        return "B"
    elif marks > 60:
        return "C"
    elif marks > 50:
        return "D"
    else:
        return "F"

def calculate_overall_grade(percentage):
    return calculate_grade(percentage)