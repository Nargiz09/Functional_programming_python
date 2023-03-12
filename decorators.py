def upper_name(func):
    def wrapper(name):
        name = name.upper()
        func(name)
    return wrapper
@upper_name
def hello(name):
    print('Привет', name)
name = input('Enter the name: ')
hello(name)