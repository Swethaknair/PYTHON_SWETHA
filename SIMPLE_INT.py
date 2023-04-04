p=int(input("enter the principal amount:"))
n=int(input("enter the no. of years:"))
c=input("is the customer a senior citizen (Y/N):")
g=input("gender (m/f):")
if(c=="y"):
    if(g=="f"):
        r=15
    else:
        r=12
else:
    r=10
interest=(p*n*r)/100
print("interest:",interest)
