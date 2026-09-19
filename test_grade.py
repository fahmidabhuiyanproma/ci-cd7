from grade import calculate_total, calculate_average, get_grade


def test_calculate_total():
    assert calculate_total(80, 70, 90) == 240
    assert calculate_total(50, 60, 70) == 180


def test_calculate_average():
    assert calculate_average(80, 70, 90) == 80
    assert calculate_average(60, 70, 80) == 70


def test_get_grade():
    assert get_grade(85) == "A+"
    assert get_grade(75) == "A"
    assert get_grade(65) == "B"
    assert get_grade(55) == "C"
    assert get_grade(40) == "F"
