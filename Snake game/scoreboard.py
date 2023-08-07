from turtle import Turtle

#HIGH_SCORE = 0
with open("data.txt") as file:
    HIGH_SCORE = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.score = 0
        self.high_score = int(HIGH_SCORE)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Arial", 10, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    #def game_over(self):
        #self.goto(0, 0)
        #self.write("GAME OVER", move=False, align="center", font=("Arial", 36, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.show_score()
