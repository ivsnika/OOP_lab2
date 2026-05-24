import turtle

class Petal:

    def __init__(self, color="hotpink", size=40):
        self.color = color
        self.size = size

    def draw(self, t):
        t.fillcolor(self.color)
        t.begin_fill()
        for _ in range(2):
            t.circle(self.size, 60)
            t.left(120)
        t.end_fill()


class Leaf:

    def __init__(self, color="forest green", size=30):
        self.color = color
        self.size = size

    def draw(self, t):
        t.fillcolor(self.color)
        t.begin_fill()
        t.left(90)
        for _ in range(2):
            t.circle(self.size, 90)
            t.left(90)
        t.right(90)
        t.end_fill()


class Stem:

    def __init__(self, color="dark green", thickness=3):
        self.color = color
        self.thickness = thickness

    def draw(self, t, length):
        t.pensize(self.thickness)
        t.pencolor(self.color)
        t.setheading(90)
        t.forward(length)


class Flower:

    def __init__(self, x, y, stem_length=150, petal_color="crimson", petal_count=6):
        self.x = x
        self.y = y
        self.stem_length = stem_length
        self.petal_count = petal_count

        self.stem = Stem()
        self.leaf = Leaf()
        self.petal = Petal(color=petal_color)

    def draw(self, t):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()

        self.stem.draw(t, self.stem_length * 0.5)

        self.leaf.draw(t)

        self.stem.draw(t, self.stem_length * 0.5)

        t.pencolor("orange")
        t.fillcolor("yellow")
        t.begin_fill()
        t.circle(10)
        t.end_fill()


        t.pencolor("black")
        t.pensize(1)
        angle = 360 / self.petal_count
        for _ in range(self.petal_count):
            self.petal.draw(t)
            t.left(angle)


def main():
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)

    bouquet = [
        Flower(x=-120, y=-150, stem_length=180),
        Flower(x=-60, y=-150, stem_length=230),
        Flower(x=0, y=-150, stem_length=260),
        Flower(x=60, y=-150, stem_length=230),
        Flower(x=120, y=-150, stem_length=180)
    ]

    for flower in bouquet:
        flower.draw(t)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()