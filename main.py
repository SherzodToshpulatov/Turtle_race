from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title='Guess', prompt='Which turtle will win the race? Enter a color: ')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_axis = -100
all_turtle = []

for name_turtle in colors:
    y_axis += 30
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(name_turtle)
    new_turtle.goto(x=-230, y=y_axis)
    all_turtle.append(new_turtle)

if user_guess:
    race_is_on = True

while race_is_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"you've won! {winning_color} turtle is the winner")
            else:
                print(f"you've lose! {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()