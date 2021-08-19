from prop import Prop

class Lightsaber(Prop):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return f"The {self.name} is making sound whoooosh"

lightsaber = Lightsaber("lightsaber")

print(lightsaber.make_sound())