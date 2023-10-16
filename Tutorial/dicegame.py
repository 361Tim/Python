import random

casts = 0
playersum = 0
computersum = 0

for casts in range(5):
    playernum = random.randrange(1,7)
    computernum = random.randrange(1,7)
    playersum += playernum
    computersum += computernum
    print(playernum,computernum)

if(playersum>computersum):
    print("Player wins, Playersum is:", playersum, "Computersum is:",computersum)

elif(playersum<computersum):
    print("Computer wins, Playersum is:", playersum, "Computersum is:",computersum)
