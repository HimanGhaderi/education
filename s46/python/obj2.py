

class Animals:
    def __init__(self):
        print("Animal")
        self.name = ""
        self.sound = ""

    def set_sound(self, name):
        self.sound = name

    def get_sound(self):
        return self.sound
    
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Bird(Animals):
    def __init__(self):
        print("Bird")
        self.dondok = ""
    
    def set_dondok(self, name):
        self.dondok = name
    def get_dondok(self):
        return self.dondok



class Khazandh(Animals):
    def __init__(self):
        print("Khazandh")
        self.length = 0

    def set_length(self, length):
        self.length = length
    def get_length(self):
        return self.length
    

snake = Khazandh()
snake.set_length(10)
result = snake.get_length()
snake.set_name("snake")
print(result)

result = snake.get_name()
print(result)