import employee_info as employee

def test_calculate_average_salary():
    result = []
    result = employee.calculate_average_salary()
    assert (result == 361000/6)

def test_get_employees_by_age_range():
    result = []
    test = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000}]
    result = employee.get_employees_by_age_range(25, 32)
    assert (result == test)
def test_get_employees_by_dept():
    result = []
    test = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    result = employee.get_employees_by_dept("Sales")
    assert (result == test)