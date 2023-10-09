import random
num1 = random.randrange(100)
num2 = random.randrange(100)

if(num1<num2) and (num1<50):
    print("Zahl 1 ist kleiner als 2 und Mini",num1,num2)

if(num1<30) or (num2<30):
    print("Eine der Zahlen ist kleiner als 30",num1,num2)

if (num1<50) and (num2!=50):
    print("erste klein, zweite nicht 50",num1,num2)