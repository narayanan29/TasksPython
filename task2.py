#roller hoster using nexted if else
print("Welcome to RollerHoster")
height=int(input("Enter your height: "))
bill=0
if height>=155:
    print("You can ride the rollerCoaster")
    age=int(input("Enter your age: "))
    if age<=12:
        bill+=5
        print("Your ticket is 5")
    elif age<=18:
        bill+=10
        print("Your ticket is 10")
    elif age<=25:
        bill+=15
        print("Your ticket is 15")
    want_photo=input("Do you want take photo(y/n): ").lower()
    if want_photo=="y":
        bill+=4
    print(f"Your total bill is {bill}")
else:
    print("Sorry you are not allowed to ride the rollerCoaster")