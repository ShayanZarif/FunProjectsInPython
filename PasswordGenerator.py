import random

print("Press Q to quit and input the length of your password")
lu = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ll = list("abcdefghijklmnopqrstuvwxyz")
nu = list("0123456789")
while(True):
    k = input() #number of characters
    if(k == "Q" or k == 'q'):
        break
    else:
        n = int(k)
    gp = "" #generated password
    for i in range(n):
        ln = random.randint(0,2) #list of characters to choose from
        if(ln == 0):
            gp += lu[random.randint(0,25)]
        elif(ln == 1):
            gp += ll[random.randint(0,25)]
        else:
            gp += nu[random.randint(0,9)]
    print(gp)
