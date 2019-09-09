from datetime import date
# date.today()
# date_n = date(2017, 10,5)

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

    def print_friends(self):
        print(f"Friends of {self.name}:")
        for us in self.friends:
            print(f"\t User {us.name}, birthday {us.date_of_dirth}")


class SocialNetwork:
    users=[]

    def init_users(self):
        # 1
        user_vic = User("Vic", [1999, 1, 23])
        user_pete = User("Pete", [1989, 8, 4])
        user_ross = User("Ross", [1995, 3, 12])
        # 2
        user_vic.add_friends(user_ross)
        user_vic.add_friends(user_pete)
        user_vic.print_friends()

        user_ross.add_friends(user_vic)
        user_ross.add_friends(user_pete)
        user_ross.print_friends()

        user_pete.add_friends(user_vic)
        user_pete.add_friends(user_ross)
        user_pete.print_friends()

        self.users.append(user_vic)
        self.users.append(user_pete)
        self.users.append(user_ross)
        # 3
        print(f"Name first user: {self.users[0].name}")
        # 4
        print(f"Age of {self.users[1].name} is {self.users[1].get_age()} years")
        # 5
        print(f"Count friends of {self.users[1].name} {len(self.users[2].friends)}")

pp = SocialNetwork()
pp.init_users()