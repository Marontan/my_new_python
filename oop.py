class Plane:
    number_of_motor = 1
    name = ""

    def __init__(self, _name):
        self.name = _name

    def up(self):
        print(f"I up, I am {self.name}")

    def down(self):
        print(f"I down, I am {self.name}")

    @staticmethod
    def get_wings_number():
        return 2

plane = Plane("Plane")
plane.up()
plane.down()
plane.get_wings_number()