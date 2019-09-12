from datetime import date
import csv

class User:
    def __init__(self, _name, _birthday):
        self.name = _name
        self.date_of_dirth = date(_birthday[0], _birthday[1], _birthday[2])
        self.friends = []

    def get_age(self):
        return int((date.today() - self.date_of_dirth).days / 365)

    def add_friends(self, _user):
        self.friends.append(_user)

    def get_friends(self):
        return self.friends
    def __str__(self):
        return f"This is {self.name}"
    def __len__(self):
        return len(self.friends)
    def __ge__(self, other):
        return len(self.friends) >= len(other.friends)
    def __gt__(self, other):
        return len(self.friends) > len(other.friends)
    def __le__(self, other):
        return len(self.friends) <= len(other.friends)
    def __lt__(self, other):
        return len(self.friends) < len(other.friends)
    def __eq__(self, other):
        return len(self.friends) == len(other.friends)

    def print_friends(self):
        print(f"Friends of {self.name}:")
        for us in self.friends:
            print(f"\t User {us.name}, birthday {us.date_of_dirth}")

class Avatar():
    def add_avatar(self, avatar):
        self.avatar = avatar

class PremiumMode():
    def __init__(self):
        self.premium_mode = False

    def enable_premium_mode(self):
        self.premium_mode = True

class Author(User, Avatar, PremiumMode):
    def __init__(self, _name, _birthday):
        super().__init__(_name, _birthday)
        self.posts = []

    def add_post(self, text):
      self.posts.append(text)

    def remove_post(self, index):
        if index > 0 and index < len(self.posts)+1:
            self.posts.pop(index-1)


class SocialNetwork:
    users=[]

    def init_users(self):
        # 1
        user_vic = User("Vic", [1999, 1, 23])
        user_pete = User("Pete", [1989, 8, 4])
        user_ross = User("Lis", [1995, 3, 12])
        # 2
        user_vic.add_friends(user_ross)
        user_vic.add_friends(user_pete)
        # user_vic.print_friends()

        user_ross.add_friends(user_vic)
        user_ross.add_friends(user_pete)
        # user_ross.print_friends()

        user_pete.add_friends(user_vic)
        user_pete.add_friends(user_ross)
        # user_pete.print_friends()

        self.users.append(user_vic)
        self.users.append(user_pete)
        self.users.append(user_ross)
        # 3
        # print(f"Name first user: {self.users[0].name}")
        # 4
        # print(f"Age of {self.users[1].name} is {self.users[1].get_age()} years")
        # 5
        # print(f"Count friends of {self.users[1].name} {len(self.users[2].friends)}")

    def add_user(self, user):
        self.users.append(user)

    def __getitem__(self, item):
        for i in self.users:
            if i.name == item:
                return i
        return None

    def export_users_to_json(self):
        with open("users.csv", "wt") as myFile:
            fieldnames = ["name", "birthday"]
            writer = csv.DictWriter(myFile, fieldnames = fieldnames)
            writer.writeheader()
            for us in self.users:
                writer.writerow({'name': us.name, 'birthday': f" {str(us.date_of_dirth)} "})




authorRoss = Author("Ross", [1982, 7, 3])
authorCh = Author("Chendler", [1984, 9, 23])
authorCh.add_avatar("avatar")
authorCh.add_friends(authorRoss)
authorJoe = Author("Joe", [1985, 11, 14])
authorJoe.enable_premium_mode()

network = SocialNetwork()
network.init_users()
network.add_user(authorRoss)
network.add_user(authorCh)
network.add_user(authorJoe)

network.export_users_to_json()



class Car:
    def __init__(self, *args):
        self.name = args[0]
        self.weight = args[1]

    def __str__(self):
           return f"This is {self.name}"
    def __ge__(self, other):
        return self.weight >= other.weight
    def __gt__(self, other):
        return self.weight > other.weight
    def __le__(self, other):
        return self.weight <= other.weight
    def __lt__(self, other):
        return self.weight < other.weight
    def __len__(self):
        return len(self.name)

carD = Car("D", 1)
carF = Car("F", 4)
# print(carD < carF)
# print(len(carD))
# list(filter(lambda x: x == "Alex", user))
