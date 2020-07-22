from matplotlib import pyplot as plt
def checkKey(dict, key):
    if key in dict.keys():
        return True
    return False

ccal = {} # Dictionary to store all expenses
print("""
Press I to input your finance data.
Press P to plot your finance.
Press O to output your finances.
Press Q to quit the program.
        """)
while(True):
    i = input()
    if(i == "I"):
        print("Category  Cost")
        a,b = map(str,input().split())
        try:
            d = int(b)
        except:
            print("Expected Input: Integer")
        try:
            c = a.upper()
            if(checkKey(ccal,c)):
                ccal[c]+=d
            else:
                ccal[c]=d
        except:
            print("Expected Input: String")
    if(i == "Q"):
        break
    if(i == "P"):
        y = list(ccal.values())
        x = [k  for  k in  ccal]
        plt.bar(x,y,align = "center")
        print("Make sure to cross out the histogram first before any other operations")
        plt.show()
    if(i == "O"):
        x = [h for h in ccal]
        y = list(ccal.values())
        for j in range(len(x)):
            print(str(x[j])+ "   " + str(y[j]))
