"""Scoreboard Class for Pong Game"""
from turtle import Turtle

ALIGNMENT = "center"
WELCOME_FONT = ("Courier", 18, "bold")
SCORE_FONT = ("Courier", 60, "bold")
LARGE_FONT = ("Courier", 28, "bold")
EXTRA_LARGE_FONT = ("Courier", 50, "bold")
PLAYER_WIN_FONT = ("Courier", 36, "bold")
WHITE = "#ECE3C9"
ORANGE = "#E3802A"
TEAL = "#2DC2C7"
WIN_SCORE = 2

class Scoreboard(Turtle):
    """Scoredboard Class"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.color(WHITE)
        self.goto(0, 180)
        self.write("PONG", align=ALIGNMENT, font=EXTRA_LARGE_FONT)
        self.goto(0, 110)
        self.color(ORANGE)
        self.write('L Player:', align=ALIGNMENT, font=LARGE_FONT)
        self.goto(0, 80)
        self.write('Use the "w" and "s" keys to', align=ALIGNMENT, font=WELCOME_FONT)
        self.goto(0, 50)
        self.write('move the paddle up and down', align=ALIGNMENT, font=WELCOME_FONT)
        self.color(TEAL)
        self.goto(0, -25)
        self.write('R Player:', align=ALIGNMENT, font=LARGE_FONT)
        self.goto(0, -55)
        self.write('Use the "up" and "down" arrow', align=ALIGNMENT, font=WELCOME_FONT)
        self.goto(0, -85)
        self.write('keys to move paddle up and down', align=ALIGNMENT, font=WELCOME_FONT)
        self.color(WHITE)
        self.goto(0, -170)
        self.write('Press "g" to start', align=ALIGNMENT, font=LARGE_FONT)

    def update_scoreboard(self):
        """Updates the scoreboard"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=SCORE_FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=SCORE_FONT)

    def l_point(self):
        """Adds a point to the left player's score"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Adds a point to the right player's score"""
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        """Writes 'Game Over' in the middle of the screen"""
        self.update_scoreboard()
        self.goto(0, 30)
        if self.l_score >= WIN_SCORE:
            self.write("GAME OVER", align=ALIGNMENT, font=EXTRA_LARGE_FONT)
            self.color(ORANGE)
            self.goto(0, -30)
            self.write("Left Player wins!", align=ALIGNMENT, font=PLAYER_WIN_FONT)
        if self.r_score >= WIN_SCORE:
            self.write("GAME OVER", align=ALIGNMENT, font=EXTRA_LARGE_FONT)
            self.color(TEAL)
            self.goto(0, -30)
            self.write("Right Player wins!", align=ALIGNMENT, font=PLAYER_WIN_FONT)
