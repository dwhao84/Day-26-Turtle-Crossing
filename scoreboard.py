from turtle import Turtle
GAMEOVER = "Game Over"
FONT = ("Courier", 24, "normal")
CENTER = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_score = 1
        self.hideturtle()
        self.penup()
        self.goto(-230, 250)
        self.color("white")
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Level { self.level_score }", align=CENTER, font=FONT)
        
    def got_score_level(self):
        self.level_score += 1
        self.update_score()
        
    def show_game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(GAMEOVER, align=CENTER, font=FONT)

        