import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import turtle
import pygame
import time


pygame.mixer.init()
sound = pygame.mixer.Sound("sound\message_box.mp3")
sound.play()
wn = turtle.Screen()
wn.title("Connecting Dots")
wn.setup(width=750, height=625)
wn.bgcolor("#BCDD7A")

valid_input = False
while not valid_input:
    number_of_players = int(turtle.textinput("Connecting Dots", "Enter number of Players: "))
    if number_of_players >= 2:
        valid_input = True
    else:
        sound = pygame.mixer.Sound("sound\error.wav")
        sound.play()

sound = pygame.mixer.Sound("sound\message_box.mp3")
sound.play()

valid_input = False
while not valid_input:
    grid_size = int(turtle.textinput("Connecting Dots", "Enter Grid size: "))
    if 5 <= grid_size <= 10:
        valid_input = True
    else:
        sound = pygame.mixer.Sound("sound\error.wav")
        sound.play()

sound = pygame.mixer.Sound("sound\message_box.mp3")
sound.play()

count = 0
dots = []
connected_dots = []
points = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
time.sleep(1)

pygame.mixer.music.load("sound\life_grand_background_music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.5)

# drawing grid
for i in range(grid_size):
    for j in range(grid_size):
        dot = turtle.Turtle()
        dot.shapesize(.5, .5, 1)
        dot.speed(0)
        dot.color("#224E43")
        dot.penup()
        dot.shape("circle")
        dot.goto(-100-(grid_size-5)*25+j*50, 100+(grid_size-5)*25-i*50)
        dots.append(dot)

turn = turtle.Turtle()
turn.speed(0)
turn.hideturtle()
turn.penup()
turn.goto(0, 250)
turn.pencolor("#2A4A1A")
turn.write(f"PLAYER {count % number_of_players + 1}'S TURN", align="center", font=("Cheri", 30, "bold"))


def game_over(winner):
    pygame.mixer.music.stop()
    global count
    time.sleep(3)
    wn.clear()
    wn.bgcolor("#5CB9BA")
    
    sound = pygame.mixer.Sound("sound\end.wav")
    sound.play()
    
    message = turtle.Turtle()
    message.speed(0)
    message.hideturtle()
    message.penup()
    message.pencolor("#00011C")
    message.write("GAME OVER", align="center", font=("Jokerman", 40, "normal"))
    wn.update()
    time.sleep(4)
    message.clear()
    wn.clear()
    wn.bgcolor("#5CB9BA")
    
    sound = pygame.mixer.Sound("sound\end.mp3")
    sound.play()
    
    message.write(f"PLAYER {winner} WINS!", align="center", font=("Jokerman", 30, "normal"))
    wn.update()
    time.sleep(7)
    turtle.bye()


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def check_and_draw_square(line):
    global connected_dots, count, points
    n = 0
    connected_x = []
    connected_y = []
    for i in range(len(connected_dots)-1):
        if line[0] in connected_dots[i]:
            x1 = line[1][0]
            y1 = line[1][1]
            if line[0] == connected_dots[i][0]:
                x2 = connected_dots[i][1][0]
                y2 = connected_dots[i][1][1]
                if distance(x1, y1, x2, y2) < 80:
                    connected_x.append(connected_dots[i][1])
            else:
                x2 = connected_dots[i][0][0]
                y2 = connected_dots[i][0][1]
                if distance(x1, y1, x2, y2) < 80:
                    connected_x.append(connected_dots[i][0])

        if line[1] in connected_dots[i]:
            x1 = line[0][0]
            y1 = line[0][1]
            if line[1] == connected_dots[i][0]:
                x2 = connected_dots[i][1][0]
                y2 = connected_dots[i][1][1]
                if distance(x1, y1, x2, y2) < 80:
                    connected_y.append(connected_dots[i][1])
            else:
                x2 = connected_dots[i][0][0]
                y2 = connected_dots[i][0][1]
                if distance(x1, y1, x2, y2) < 80:
                    connected_y.append(connected_dots[i][0])

    for x in connected_x:
        for y in connected_y:
            for seg in connected_dots[:-1]:
                if len(x) > 0 and len(y) > 0 and x in seg and y in seg and distance(x[0], x[1], y[0], y[1]) == 50:
                    point = turtle.Turtle()
                    point.speed(0)
                    point.hideturtle()
                    point.penup()
                    a = min(line[0][0], line[1][0], x[0], y[0]) + 25
                    b = min(line[0][1], line[1][1], x[1], y[1]) + 5
                    point.goto(a, b)
                    point.pencolor("#050B2B")
                    time.sleep(1)
                    
                    sound = pygame.mixer.Sound("sound\get_bonus.wav")
                    sound.play()
                    
                    if n == 0:
                        point.write(f"{(count - 1) % number_of_players + 1}", align="center",
                                    font=("Berlin Sans FB", 30, "normal"))
                        points[(count - 1) % number_of_players + 1] += 1
                        count -= 1
                        n = 1
                    else:
                        point.write(f"{count % number_of_players + 1}", align="center",
                                    font=("Berlin Sans FB", 30, "normal"))
                        points[count % number_of_players + 1] += 1


def draw_line(x, y):
    turn.clear()
    global connected_dots, count
    line = []
    for dot in dots:
        if dot.distance(x, y) < 35:
            line.append(dot.position())
    if len(line) == 2 and line not in connected_dots:
        count += 1
        connected_dots.append(line)
        segment = turtle.Turtle()
        segment.hideturtle()
        segment.pencolor("#003554")
        segment.pensize(2)
        segment.penup()
        segment.goto(line[0])
        segment.pendown()
        segment.goto(line[1])
        
        sound = pygame.mixer.Sound("sound\click.wav")
        sound.play()
        
        check_and_draw_square(line)

    turn.goto(0, 250)
    turn.pencolor("#2A4A1A")
    turn.write(f"PLAYER {count % number_of_players + 1}'S TURN", align="center", font=("Cheri", 30, "bold"))
    if sum(points) == (grid_size - 1) ** 2:
        game_over(points.index(max(points)))


turtle.onscreenclick(draw_line)
turtle.mainloop()
