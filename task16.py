class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1

user1=User('narayanan',20)
user2=User('priya',15)

user1.follow(user2)
print(f"My followers: {user1.followers}")
print(f"My following: {user1.following}")
print(f"Friend1 followers: {user2.followers}")
print(f"Friend1 following:  {user2.following}")

