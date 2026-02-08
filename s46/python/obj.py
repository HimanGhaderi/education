


class animals:

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def play_sound(self):
        print(self.sound)

    def print(self):
        print(self.name)


cat = animals("cat", "mio mio")
cat.play_sound()
cat.print()

dog = animals("dog", "hav hav")
dog.play_sound()
dog.print()

bird = animals("bird", "jik jik")
bird.play_sound()
bird.print()




