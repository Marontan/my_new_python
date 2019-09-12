from datetime import date
import csv
import networkx as nx
import matplotlib.pyplot as plt

class User:
    def __init__(self, _name, _birthday):
        self.name = _name
        self.date_of_dirth = date(_birthday[0], _birthday[1], _birthday[2])
    def get_age(self):
        return int((date.today() - self.date_of_dirth).days / 365)

class SocialNetwork:
    def __init__(self):
        self.graph_users = nx.Graph()

    def init_users(self):
        self.add_user(User("Rachel", [1999, 1, 23]))
        self.add_user(User("Monika", [1989, 8, 4]))
        self.add_user(User("Phoebe", [1995, 3, 12]))
        self.add_user(User("Ross", [1982, 7, 3]))
        self.add_user(User("Chandler", [1984, 9, 23]))
        self.add_user(User("Joey", [1985, 11, 14]))

        self.add_friendship("Rachel", "Monika")
        self.add_friendship("Rachel", "Chandler")
        self.add_friendship("Phoebe", "Joey")
        self.add_friendship("Phoebe", "Rachel")
        self.add_friendship("Chandler", "Ross")
        self.add_friendship("Chandler", "Phoebe")

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
network.init_users()

userFind = "Rachel"
print(f"Friends of {userFind}:", network.recommend_friends(userFind))

nx.draw_networkx(network.graph_users)
plt.show()

