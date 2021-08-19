from prop import Prop


class Movie(Prop):
    def __init__(self, title):
        self.title = title

    def use_prop(self, prop):
        return self(prop.make_sound)

movie = Movie("movie")