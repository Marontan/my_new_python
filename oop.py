class Plane:
    def __init__(self, _name, _motors_number=1, _wings_number=2):
        self.name = _name
        self.motors_number = _motors_number
        self.wings_number = _wings_number

    def up(self):
        print(f"I am {self.name}, I up")
        raise NotImplementedError

    def down(self):
        print(f"I am {self.name}, I down")
        raise NotImplementedError

    @staticmethod
    def get_wings_number():
        return 2

# plane = Plane("Plane")
# plane.up()
# plane.down()
# plane.get_wings_number()

class ColorSetMixin():
    def cet_color(self, color):
        self.color = color


class CivilPlane(Plane):
    def __init__(self, name):
        super(CivilPlane, self).__init__(name)
        self.is_music = False
        self.is_ligth = False
    def up(self):
        print("up")
    def down(self):
        print("down")
    def passengers_num(self):
        print("passengers_num")
    def toggle_music(self):
        if self.is_music == False:
            self.is_music = True
            print("Music on")
        else:
            self.is_music = False
            print("Music off")
    def toggle_ligth(self):
        if self.is_ligth == False:
            self.is_ligth = True
            print("Ligth on")
        else:
            self.is_ligth = False
            print("Ligth off")

class BattlePlane(Plane, ColorSetMixin):
    def __init__(self, name, bombs=3):
        super().__init__(name)
        self.bombs_numbers = bombs
    def do_bombing(self):
        if self.bombs_numbers > 0:
            self.bombs_numbers-=1
            print(f"Bombing, there is {self.bombs_numbers} bombs")
        else:
            self.launch_catapulte()


    def launch_catapulte(self):
        print("Bye-bye")



civil = CivilPlane("Plane")
civil.up()
civil.down()
civil.toggle_music()
civil.toggle_music()
civil.toggle_ligth()
civil.toggle_ligth()

battle = BattlePlane("Waaaaaaar")
battle.do_bombing()
battle.do_bombing()
battle.do_bombing()
battle.do_bombing()
