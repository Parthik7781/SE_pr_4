no=int(input("Enter no."))
sum=0
cpy=no
while no!=0:
    r=no%10
    sum=sum+(r*r*r)
    no=int(no/10)
if sum==cpy:
    print("It is armstrong no.")
else:
    print("It is not armstrong no")