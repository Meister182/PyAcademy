# Day 4 - Journeyman
Exploring the innerworkings.
>_Listen To Me, Morty. I Know That New Situations Can Be Intimidating. You're Lookin’ Around, And It’s All Scary And Different, But Y’know … Meeting Them Head-On, Charging Into ‘Em Like A Bull — That’s How We Grow As People._

- ## Objects anatomy
    - Dunders (revisiting dir)
    - Operators overload
    - Context managers
    - SubClasses
- ## Advanced features
    - decorators
    - lambda
    - map, reduce, filter
- ## Good Practices
    - Typehinting
    - Docstrings
    - pytest
    - Linters (black, tox, PEP8)

## Exercises

Copy this functions into a Python file and create tests that coverage all the code.

Run Pylint and make the recommendations that it suggests.

```python
def isPrime(number):
    """Return True if *number* is prime."""
    for element in range(2, number):#Don't use 0 and 1
        if number % element == 0:
            return False
    return True


def find_next_prime(number):
    index=number
    while True:
        index += 1
        if isPrime(index):
            return index
```