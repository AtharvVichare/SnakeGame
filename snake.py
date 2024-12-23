import turtle

Move_pos = 20
position = [(0, 0), (-20, 0), (-40, 0)]
Right = 0
Down = 270
Left = 180
Up = 90


class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def add_segment(self, pos):
        tim = turtle.Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(pos)
        self.parts.append(tim)

    def create_snake(self):
        for pos in position:
            self.add_segment(pos)

    def update(self):
        self.add_segment(self.parts[-1].pos())

    def collision(self):
        if self.head.xcor() >= 290 or self.head.xcor() <= -290:
            return True
        if self.head.ycor() >= 290 or self.head.ycor() <= -290:
            return True
        for part in self.parts[2:]:
            if self.head.distance(part) < 10:
                return True
        return False

    def move(self):
        for i in range(len(self.parts) - 1, 0, -1):
            tp = self.parts[i - 1].pos()
            self.parts[i].setpos(tp)
        self.parts[0].fd(Move_pos)

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)

    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    def reset(self):
        for part in self.parts:
            part.goto(1000, 1000)
        self.parts.clear()
        self.create_snake()
        self.head = self.parts[0]
