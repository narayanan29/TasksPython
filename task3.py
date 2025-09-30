#pizza delivery
size=input("what size pizza do you want?s,m,l  ").lower()
pepperonion=input("Do you want pepperonion?y/n: ").lower()
extra_cheese=input("Dou you want extra cheese?y/n: ").lower()
bill=0
if size=='s':
    bill=bill+10
elif size=='m':
    bill+=15
elif size=='l':
    bill+=20
else:
    print("You entered wroung input")
if pepperonion=='y':
    if size=='s':
        bill+=4
    else:
        bill+=7
if extra_cheese=='y':
    bill+=2
print(f"Your final bill is {bill}")
