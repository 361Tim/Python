import random
def add(x,y):
    return x+y

print( add(2,3))


def zufallszahl():
    return random.randrange(100,200)
print(zufallszahl())


def wort(arr, index):
    if index < len(arr):
            return arr[index]
    else:
        return "Index auerhalb von array"

array= ["Apfel","Birne","Banane","Orange"]
print(wort(array,2))