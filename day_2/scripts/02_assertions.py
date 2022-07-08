# call: python3 -O 02_assertions.py
my_list = list(range(10))
print(f'my_list : {my_list}')

assert '9' in my_list, "9 is in my list"

print("All good in the Hood.")
