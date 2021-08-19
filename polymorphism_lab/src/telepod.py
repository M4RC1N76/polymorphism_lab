from prop import Prop


class Telepod(Prop):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return f"The {self.name} is making the sound schwoooof"


telepod = Telepod("telepod")

print(telepod.make_sound())
