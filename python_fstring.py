# output alignment
var: str = "value"
print(f"{var: >20}")
print(f"{var:_>20}")
print(f"{var:#<20}")
print(f"{var:|^20}")

# date time format
from datetime import datetime
now: datetime = datetime.now()
date_spec: str = '%d.%m.%y'
print(f'{now: {date_spec}}') # nested f-string

# round a float number
n: float = 12345.6789
print(f'{n:.2f}')
print(f'{n:,.3f}')
print(f'{n:_.4f}')


#debug using f-string
a: int = 5
b: int = 10
my_var: str = "who are you"
print(f'{a + b = }')

print(f'{my_var = }') # my_var = 'who are you'
print(f'{my_var = !s}') # my_var = who are you



from datetime import datetime, date

banana: str = 'image of banana'
name: str = 'bob'
today: date = datetime.now().date()

print(f'[{today!s}] {name!s} says: {banana!s}')
print(f'[{today!r}] {name!r} says: {banana!r}')
print(f'[{today!a}] {name!a} says: {banana!a}')