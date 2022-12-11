import turtle
import random

player_one = turtle.Turtle()
player_one.color("red")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)
player_one.goto(300, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200, 100)

player_two = player_one.clone()
player_two.color("pink")
player_two.penup()
player_two.goto(-200, -100)
player_two.goto(300, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)

die = [1, 2, 3, 4, 5, 6]

for i in range(20):
    if player_one.pos() >= (300, 100):
        print("Player One Wins!")
        break
    elif player_two.pos() >= (300, -100):
        print("Player Two Wins!")
        break
    else:
        player_one_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print(f"The result of the die roll is: {die_outcome}")
        print(f"The number of steps will be: {20*die_outcome}")
        player_one.forward(20*die_outcome)
        player_two_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print(f"The result of the die roll is: {die_outcome}")
        print(f"The number of steps will be: {20*die_outcome}")
        player_two.forward(20*die_outcome)
