from grade import calculate_grade

def test_grade_A():
    assert calculate_grade(95) == "A"

def test_grade_B():
    assert calculate_grade(85) == "B"

def test_invalid_input():
    assert calculate_grade(-5) == "Invalid marks!"
