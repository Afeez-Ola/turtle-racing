import turtle
import random

COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]
screen = turtle.Screen()

is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ").lower()
turtles_list = []


def create_turtle(shape, color, x, y):
    t = turtle.Turtle(shape=shape)
    t.speed("fastest")
    t.penup()
    t.color(color)
    t.goto(x, y)
    turtles_list.append(t)


turtles = [
    create_turtle("turtle", COLORS[i], -238, -100 + i * 50)
    for i in range(5)
]
screen.setup(width=500, height=400)
winning_turtle = ""
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles_list:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_turtle = turtle.pencolor()
        random_movement = random.randint(0, 10)
        turtle.forward(random_movement)
screen.clear()
turtle.goto(0, 0)
if winning_turtle == user_bet:
    turtle.write(f"You Won! The winning color is {winning_turtle}", align="center", font=("Arial", 16, "normal"))
else:
    turtle.write("You Lost! The winning color is {winning_turtle}", align="center", font=("Arial", 16, "normal"))
screen.exitonclick()
