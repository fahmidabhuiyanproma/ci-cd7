def calculate_total(mark1, mark2, mark3):
    return mark1 + mark2 + mark3 


def calculate_average(mark1, mark2, mark3):
    return calculate_total(mark1, mark2, mark3) / 3


def get_grade(average):
    if average >= 80:
        return "A+"
    elif average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"
