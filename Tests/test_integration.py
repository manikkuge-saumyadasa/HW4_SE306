from Calculator_Code.calc import add, subtract, multiply, divide

def test_combined_operations():
    result = divide(multiply(add(2, 3), 4), 2)
    # ((2+3) * 4) / 2 = 10
    assert result == 10