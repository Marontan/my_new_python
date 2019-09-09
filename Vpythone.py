import datetime
#datetime.date.today()

# from datetime import date
# date.today()
# date_n = date(2017, 10,5)

class User:
    friends = []

    def __init__(self, _name, _birthday):
        self.name = _name
        from datetime import date
        self.date_of_dirth = date(_birthday[0], _birthday[1], _birthday[2])

    def get_age(self):
        from datetime import date
        return (date.today() - self.date_of_dirth) / 365

    def add_friends(self, _user):
        self.friends.append(_user)

    def get_friends(self):
        return self.friends

    def print_friends(self):
        for us in self.friends:
            print(f"User {us.name}, birthday {us.date_of_dirth}")

user_vic = User("Vic", [1999, 1, 23])
user_pete = User("Pete", [1989, 8, 4])
user_ross = User("Ross", [1995, 3, 12])
print(f"Age of {user_vic.name} is {user_vic.get_age()}")

user_vic.add_friends(user_ross)
user_vic.add_friends(user_pete)
user_vic.print_friends()

