from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)


user_bet = screen.textinput(title="Make your bet.", prompt="Choose the color od the turtle:")

is_race_on = True
colors = ["green", "yellow", "red", "purple", "blue", "orange"]
y_axis = [-60, -30, 0, 30, 60, 90]
turtle_list = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_axis[turtle_index])
    turtle_list.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The winner color is:{winner_color}")
            else:
                print(f"You've lost. The winner color is:{winner_color}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
