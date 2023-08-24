from random import random
def getHollJjack():
    rnd = random()
    a =""
    if rnd>0.5:
        a="홀"
    else :
        a="짝"  
    return a
    
com = getHollJjack()
print("com",com)