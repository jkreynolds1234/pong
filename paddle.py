"""Creates Paddle Class for Pong Game"""
from turtle import Turtle

WHITE = "#ECE3C9"

class Paddle(Turtle):
    """Paddle Class"""
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(WHITE)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    # Move Paddle Functions
    def go_up(self):
        """Moves the paddle up"""
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves the paddle down"""
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
