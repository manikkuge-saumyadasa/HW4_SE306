from Calculator_Code.calc import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(2, 7) == 5

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(2, 4) == 8

def test_divide():
    assert divide(10, 2) == 5



