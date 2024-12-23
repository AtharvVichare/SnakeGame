from turtle import Turtle

Alignment = "center"
Font = ("bold", 25, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update_score()
        self.hideturtle()

    def inc_score(self):
        self.score += 1
        self.update_score()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} Highest Score = {self.high_score}", align=Alignment, font=Font)
