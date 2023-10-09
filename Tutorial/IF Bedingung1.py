import random
num = random.randrange(100)

if(num<20):
    print("small",num)

if(num<50) and (num>20):
    print("medium",num)

if(num>50):
    print("large",num)
