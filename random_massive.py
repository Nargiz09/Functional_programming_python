import random
def massiv(start, stop):
    list1 = []
    for i in range(10):
        list1.append(random.randrange(start, stop))
    return list1
start = int(input('Enter min value of the range: '))
stop = int(input('Enter max value of the range: '))
print(massiv(start, stop))