class User:
    total_users = 0

    def __init__(self, username): #__init__ is called as a blueprint when the class is first called
        self.username = username
        User.total_users += 1 #needs to call up to the User class to use the variable

    def get_info(self):
        return (self.username, User.total_users) 

user1 = User("alice")
user2 = User("bob")
print(user1.get_info())
print(user2.get_info())