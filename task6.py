#password
import random
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9']
symbols=['@','#','$','%','^','&','*']

print("//////Welcome to python Password Generator !//////")
no_letters=int(input("How many letters would you like to generate? "))
no_num=int(input("How many numbers would you like to generate? "))
no_symbols=int(input("How many symbols would you like to generate? "))

#Easy
# password=""
# for char in range(no_letters):
#     password+=random.choice(letter)
# for char in range(no_num):
#     password+=random.choice(numbers)
# for char in range(no_symbols):
#     password+=random.choice(symbols)
# print(password)

password_lst=[]
for char in range(no_letters):
    password_lst.append(random.choice(letter))
for char in range(no_num):
    password_lst.append(random.choice(numbers))
for char in range(no_symbols):
    password_lst.append(random.choice(symbols))
print(password_lst)
random.shuffle(password_lst)
print(password_lst)

password=""
for i in password_lst:
    password+=i
print(password)
