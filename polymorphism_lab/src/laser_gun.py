
from prop import Prop

class Laser_gun(Prop):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return f"The {self.name} is making the sound bzzzzz"


laser_gun = Laser_gun("laser gun")

print(laser_gun.make_sound())
