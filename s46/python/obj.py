


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






class Car:
    def __init__(self):
        self.sound = ""
        self.color = "" 
        self.motor = ""

    
    def set_color(self, color):
        self.color = color
    
    def get_color(self):
        print(self.color)

    def set_motor(self,motor):
        self.motor = motor
    def get_motor(self):
        print(self.motor)
    
    def set_sound(self, sound):
        self.sound = sound
    def get_sound(self):
        print(self.sound)

    def car_type(self,):
        print(self.color)
        print(self.motor)
        print(self.sound)


car1 = Car()
car1.set_color("red")
car1.set_motor("Samand")
car1.set_sound("beeeeeb")


car22 = Car()
car22.set_color("black")
car22.set_motor("zantia")
car22.set_sound("Miavvvv")


car22.get_color()
car1.get_color()





class Button:
    def __init__(self):
        self.color = "black"
        self.shape = "circle"
        self.size = "2"


    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color
    


btn = Button()
btn.set_color("yellow")
result = btn.get_color()
print(result)



