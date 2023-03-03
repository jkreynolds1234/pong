"""Creates Ball Class for Pong Game"""
from turtle import Turtle

WHITE = "#ECE3C9"

class Ball(Turtle):
    """Ball Class"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(WHITE)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Ball moves NE"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Makes ball bounce off wall in opp of og direction"""
        self.y_move *= -1

    def bounce_x(self):
        """Makes ball bounce off paddle in opp of og direction"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Resets the ball's position to the center of the screen"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
