from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Winner", prompt="Guess which turtle win. Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]

all_turtles =[]
y_cor = -100
for turtle_index in range (0,6):
    a = Turtle(shape="turtle")
    a.color(colors[turtle_index])
    a.penup()
    a.goto(x=-230,y=y_cor)
    y_cor +=30
    all_turtles.append(a)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()> 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost!The {winning_color} turtle is the winner.")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
