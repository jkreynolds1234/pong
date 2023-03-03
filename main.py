"""Pong Game Main File"""
from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

BGCOLOR = "#22201A"
WIN_SCORE = 2

class PongGame():
    """Class for Pong Game"""
    def __init__(self):
        # Don't start game on program start
        self.game_is_on = False

        # Screen Setup
        self.screen = Screen()
        self.screen.bgcolor(BGCOLOR)
        self.screen.setup(width=800, height=600)
        self.screen.title("Pong")
        # Turns off animation (manually updated in the while loop later)
        self.screen.tracer(0)

        # Welcome Message
        self.scoreboard = Scoreboard()

        # Listen for key presses
        self.screen.listen()
        # Starts game on key press "g"
        self.screen.onkey(self.start_game, "g")
        # Prevents screen from exiting immediately
        self.screen.exitonclick()

    def start_game(self):
        """Starts the Pong Game and changes game status to on"""
        self.game_is_on = True
        self.ball = Ball()
        self.r_paddle = Paddle((350, 0))
        self.l_paddle = Paddle((-350, 0))

        # Controls for left and right paddles
        self.screen.onkeypress(self.r_paddle.go_up, "Up")
        self.screen.onkeypress(self.r_paddle.go_down, "Down")
        self.screen.onkeypress(self.l_paddle.go_up, "w")
        self.screen.onkeypress(self.l_paddle.go_down, "s")

        while self.game_is_on:
            # Pause during each update to have animation move at speed I want
            time.sleep(self.ball.move_speed)
            self.screen.update()
            self.scoreboard.update_scoreboard()
            self.ball.move()

            # Detect collision with wall
            if self.ball.ycor() > 275 or self.ball.ycor() < -275:
                self.ball.bounce_y()

            # Detect collision with right paddle
            if self.ball.ycor() < (self.r_paddle.ycor() + 60) and self.ball.ycor() > (self.r_paddle.ycor() - 60):
                if self.ball.xcor() > 320 and self.ball.xcor() < 360 and self.ball.move_speed > 0:
                    self.ball.bounce_x()

            # Detect collision with left paddle
            if self.ball.ycor() < (self.l_paddle.ycor() + 60) and self.ball.ycor() > (self.l_paddle.ycor() - 60):
                if self.ball.xcor() < -320 and self.ball.xcor() > -360 and self.ball.move_speed < 0:
                    self.ball.bounce_x()

            # Detect R paddle miss
            if self.ball.xcor() > 380:
                self.ball.reset_position()
                self.scoreboard.l_point()

            # Detect L paddle miss
            if self.ball.xcor() < -380:
                self.ball.reset_position()
                self.scoreboard.r_point()

            if self.scoreboard.l_score >= WIN_SCORE or self.scoreboard.r_score >= WIN_SCORE:
                self.scoreboard.game_over()
                self.game_is_on = False

game = PongGame()
