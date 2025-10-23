class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1

user_1 = User(1, "Pesho")
user_2 = User(2, "Gosho")

print(user_1.id)
print(user_1.username)
print(user_1.followers)
print(user_1.following)

user_1.follow(user_2)

print(user_1.following)
print(user_2.followers)