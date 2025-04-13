import pytest
from employee import Employee

@pytest.fixture
def employee():
  """Create a sample employee for use in multiple tests."""
  return Employee('John', 'Doe', 50000)

def test_give_default_raise():
  emp = Employee('John', 'Doe', 50000)
  emp.give_raise()
  assert emp.salary == 55000

def test_give_custom_raise():
  emp = Employee('Jane', 'Smith', 60000)
  emp.give_raise(10000)
  assert emp.salary == 70000
