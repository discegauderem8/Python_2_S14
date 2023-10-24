import pytest
import S13_DB as main

@pytest.fixture
def test_company():
    company = main.Company("Некая компания")
    return company

@pytest.fixture
def test_employee():
    employee = main.Employee("Олег", 4, "123456")
    return employee

def test_successful_login(test_company, test_employee):
    company = test_company
    employee = test_employee
    assert company.login(employee.name, employee.employee_id) == employee

def test_successful_hiring(test_company):
    company = test_company
    company.hiring(main.Employee("Игорёха", 4, "654321"), "Вася", "654000", 3)
    employee = company.login("Вася", "654000")
    assert employee is not False
