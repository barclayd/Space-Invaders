import turtle
import math
import os

# set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


# player
player = turtle.Turtle()
player.color("green")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)


# player shooter
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.hideturtle()
bullet.speed(0)
bullet.setheading(90)
bullet.setposition(player.xcor(), player.ycor())
bullet.shapesize(0.5, 0.5)

# bullet states
# ready - ready to fire
# fire - bullet has been shot

bullet_state = "ready"

# alien enemies
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("square")
enemy.penup()
enemy.speed(1)
enemy.setposition(-200, 250)


# speed controls
enemy_speed = 15
player_speed = 15
bullet_speed = 40


def move_left():
    x = player.xcor()
    if x > -280:
        x -= player_speed
    player.setx(x)


def move_right():
    x = player.xcor()
    if x < 280:
        x += player_speed
    player.setx(x)


def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.setposition(player.xcor(), player.ycor() + 10)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False



# keybindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


# game score
game_score = 0
# ASCI art
game_over = """

 ________  ________  _____ ______   _______           ________  ___      ___ _______   ________  ___       
|\   ____\|\   __  \|\   _ \  _   \|\  ___ \         |\   __  \|\  \    /  /|\  ___ \ |\   __  \|\  \      
\ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|        \ \  \|\  \ \  \  /  / | \   __/|\ \  \|\  \ \  \     
 \ \  \  __\ \   __  \ \  \\|__| \  \ \  \_|/__       \ \  \\\  \ \  \/  / / \ \  \_|/_\ \   _  _\ \  \    
  \ \  \|\  \ \  \ \  \ \  \    \ \  \ \  \_|\ \       \ \  \\\  \ \    / /   \ \  \_|\ \ \  \\  \\ \__\   
   \ \_______\ \__\ \__\ \__\    \ \__\ \_______\       \ \_______\ \__/ /     \ \_______\ \__\\ _\\|__|   
    \|_______|\|__|\|__|\|__|     \|__|\|_______|        \|_______|\|__|/       \|_______|\|__|\|__|   ___ 
                                                                                                      |\__\
                                                                                                      \|__|
                                                                                                           

 
"""


# main game loop
while True:

    # move enemy
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)

    # move enemy left, right and down
    if enemy.xcor() > 280:
        enemy_speed *= -1
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemy_speed *= -1
        enemy.sety(y)

    # move bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # check if bullet has gone off the screen
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

    # check for collision(bullet, enemy)
    if isCollision(bullet, enemy):
        game_score += 1
        print(game_score)
        # reset bullet
        bullet.hideturtle()
        bullet_state = "ready"
        bullet.setposition(player.xcor(), player.ycor())
        # reset enemy
        enemy.setposition(-200, 250)

    # check for collision(player, enemy)
    if isCollision(player, enemy):
        game_score += 1
        print(game_score)
        # reset player
        player.hideturtle()
        enemy.hideturtle()
        print(game_over)
        break

