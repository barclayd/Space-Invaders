import turtle
import math
import random
import os

# set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("./img/space.gif")
wn.tracer(0)

# register shapes
wn.register_shape("player.gif")
wn.register_shape("enemy.gif")

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
player.shape("player.gif")
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

# add a number of enemies
number_of_enemies = 7
enemies = []
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("red")
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-250, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

# speed controls
enemy_speed = 2
player_speed = 25
bullet_speed = 40


def move_left():
    x = player.xcor()
    if x > -275:
        x -= player_speed
    player.setx(x)


def move_right():
    x = player.xcor()
    if x < 275:
        x += player_speed
    player.setx(x)


def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        os.system("afplay ./audio/bullet.wav&")
        bullet.setposition(player.xcor(), player.ycor() + 10)
        bullet.showturtle()


def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 30:
        return True
    else:
        return False


# keybindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")


# game score
score = 0
aliens_killed = 0
aliens_score = "Aliens killed: %s" % aliens_killed
game_score = "Score: %s" % score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 305)
score_pen.write(game_score, False, align="left", font=("Mono", 14, "bold"))
score_pen.hideturtle()

aliens_pen = turtle.Turtle()
aliens_pen.speed(0)
aliens_pen.color("red")
aliens_pen.penup()
aliens_pen.setposition(-290, 280)
aliens_pen.write(aliens_score, False, align="left", font=("Mono", 14, "bold"))
aliens_pen.hideturtle()


game_over = "Game over! Try again?"

# title
title = turtle.Turtle()
title.speed(0)
title.color("white")
title.penup()
title.setposition(0, 305)
title.write("Space Invaders", False, align="center", font=("Mono", 24, "bold"))
title.hideturtle()

# main game loop
while True:
    wn.update()
    for enemy in enemies:

        # move enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # move enemy left, right and down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemy_speed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemy_speed *= -1

        # check for collision(bullet, enemy)
        if is_collision(bullet, enemy):
            os.system("afplay ./audio/explosion.wav&")
            score += 10
            game_score = "Score: %s" % score
            aliens_killed += 1
            aliens_score = "Aliens killed: %s" % aliens_killed
            score_pen.clear()
            aliens_pen.clear()
            score_pen.write(game_score, False, align="left", font=("Mono", 14, "bold"))
            aliens_pen.write(aliens_score, False, align="left", font=("Mono", 14, "bold"))
            # reset bullet
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(player.xcor(), player.ycor())
            # reset enemy
            x = random.randint(-250, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)

        # check for collision(player, enemy)
        if is_collision(player, enemy):
            # reset player
            os.system("afplay ./audio/collision.wav&")
            player.hideturtle()
            enemy.hideturtle()
            print(game_over)
            break

    # move bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # check if bullet has gone off the screen
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

