from datetime import date
import csv
import networkx as nx
import matplotlib.pyplot as plt
from peewee import SqliteDatabase, Model, CharField, DateField, BooleanField, ForeignKeyField

db = SqliteDatabase('SocialNetwork.db')

class User(Model):
    name = CharField()
    date_of_birth = DateField()
    class Meta:
        database = db

    def get_age(self):
        return int((date.today() - self.date_of_dirth).days / 365)



class Friendship(Model):
    friend1=CharField()
    friend2 = CharField()
    class Meta:
        database = db

class SocialNetwork(Model):
    def __init__(self):
        self.graph_users = nx.Graph()
        self.init_users()
        self.create_table()

    def create_table(self):
        User.create_table()
        if len(list(User.select())) == 0:
            User.create(name="Rachel", date_of_birth=date(1999, 1, 23))
            User.create(name="Monika", date_of_birth=date(1989, 8, 4))
            User.create(name="Phoebe", date_of_birth=date(1995, 3, 12))
            User.create(name="Ross", date_of_birth=date(1982, 7, 3))
            User.create(name="Chandler", date_of_birth=date(1984, 9, 23))
            User.create(name="Joey", date_of_birth=date(1985, 11, 14))
            Friendship.create_table()
            Friendship.create(friend1="Rachel", friend2="Monika")
            Friendship.create(friend1="Rachel", friend2="Chandler")
            Friendship.create(friend1="Phoebe", friend2="Joey")
            Friendship.create(friend1="Chandler", friend2="Ross")
            Friendship.create(friend1="Chandler", friend2="Phoebe")


    def init_users(self):
        User.create_table()
        list_user = list(User.select())
        for us in list_user:
            user = User(us.name, us.date_of_birth)
            self.add_user(user)
        Friendship.create_table()
        list_friendship = list(Friendship.select())
        for fr in list_friendship:
            self.add_friendship(fr.friend1, fr.friend2)


    def get_neighbours(self, user):
         return set(self.graph_users.neighbors(user))

    def recommend_friends(self, user):
        result_recommend = set()
        friends = self.get_neighbours(user)
        for friend in friends:
            friend_friend = self.get_neighbours(friend)
            for item in friend_friend:
                result_recommend.add(item)
        result_recommend = result_recommend.difference(friends)
        result_recommend.remove(user)
        return result_recommend

    def add_user(self, user):
        self.graph_users.add_node(user.name, data=user)

    def add_friendship(self, user1, user2):
        self.graph_users.add_edge(user1, user2)



network = SocialNetwork()


userFind = "Rachel"
print(f"Friends of {userFind}:", network.recommend_friends(userFind))

nx.draw_networkx(network.graph_users)
plt.show()

