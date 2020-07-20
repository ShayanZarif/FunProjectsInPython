print("List all the email addresses below. Input Q to stop and get output.")
l = []
while(True):
    i = input()
    if(i == "Q" or i=="q"):
        break #Quit
    else:
        s = i.strip()
        un = str(s[:s.index('@')])#username
        dm = str(s[s.index("@")+1:])#domain
        l.append("Username: "+un+"  Domain: "+dm)
for k in range(len(l)):
    print(l[k]) #output
