class Horse:
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx, dy):
        self.dx = dx
        Horse.x_distance += dx
        super().fly(dy)


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'
    def fly(self, dy):
        self.dy = dy
        Eagle.y_distance += dy


class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super().run(dx, dy)

    def get_pos(self):
        return (Horse.x_distance, Eagle.y_distance)

    def voice(self):
        print(Eagle.sound)  # Если пишу super().sound, наследует от класса Horse.
        # Не пойму, как продолжить наследование атрибута вне методов.

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
