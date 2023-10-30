import lab2.bmi as bmi
def test_bmi_normal_weight():
    result = []
    height = 1.8
    weight= 70
    result = bmi.calculate_bmi(height,weight)
    assert (result == 0)

def test_bmi_over_weight():
    result = []
    height = 1.6
    weight = 70
    result = bmi.calculate_bmi(height, weight)
    assert (result == -1)

def test_bmi_under_weight():
    result = []
    height = 2.0
    weight = 70
    result = bmi.calculate_bmi(height, weight)
    assert (result == 1)

