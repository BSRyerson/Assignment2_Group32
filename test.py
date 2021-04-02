from Calculator import Calculator

# Tests addition method in Calculator
def test_add():
    x,y = 1,2
    instance = Calculator(x,y)
    assert instance.add() == x + y, "Add method doesnt work"

# Tests subtraction method in Calculator
def test_subtract():
    x,y=1,2
    instance = Calculator(x,y)
    assert instance.subtract() == x-y, "Subtract method doesnt work"
