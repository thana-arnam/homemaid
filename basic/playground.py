a = 1
b = 'hello'
print(b)

if a == 1 and (a == 2):
    print('hello2')
    print('hi')
elif a == 2:
    print('a is 2')
else:
    print('else!')

if a is None:
    print('a is None')

if a:
    print('a')

if a is not None:
    print('a is not None')

def say():
    print('hi')

say()

def say1(number):
    print(f'hi {number}')

# not recommend
def say1(number: int):
    print('hi ' + str(number))

