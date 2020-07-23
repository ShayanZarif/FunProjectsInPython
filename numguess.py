print('''This is a number guessing game. Think of a number between 0 to 100. I will output a number.
If your number is bigger enter "B".
If your number is bigger enter "S".
If your number matches the output enter "V"


Binary Search is used
''' )
l = [x for x in range(101)]
L = 0
R = 100
while(L<=R):
    mid = (L+R)//2
    print(l[mid])
    i = input()
    if(i == 'B'):
        L = mid
    elif(i == 'S'):
        R= mid
    elif(i == 'V'):
        print("Bingo!")
        break
    else:
        print("Wrong Input")
