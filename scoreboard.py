from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.goto(0, 250)

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.highscore}", align="center", font=("Courier", 25, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")

        self.score = 0

