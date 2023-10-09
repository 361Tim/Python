import random
value = 0
randnum = 0

while(randnum !=15 and randnum !=25):
    randnum = random.randrange(10, 30)
    value += randnum
    print(randnum)

print(value)