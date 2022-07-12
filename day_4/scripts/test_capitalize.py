import pytest

# Function
def capital_case(x):
    return x.capitalize()

# A simple test
def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

# A better function
def better_capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()

# Another test
def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        better_capital_case(9)
