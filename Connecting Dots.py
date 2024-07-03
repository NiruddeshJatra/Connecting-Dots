import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import turtle
import pygame
import time

class ConnectDotsGame:
    def __init__(self):
        self.init_pygame()
        self.setup_screen()
        self.get_player_count()
        self.get_grid_size()
        self.init_game_variables()
        self.setup_grid()
        self.display_turn()

    def init_pygame(self):
        pygame.mixer.init()

    def play_sound(self, sound_file):
        sound = pygame.mixer.Sound(sound_file)
        sound.play()

    def setup_screen(self):
        self.play_sound("sound\message_box.mp3")
        self.wn = turtle.Screen()
        self.wn.title("Connecting Dots")
        self.wn.setup(width=750, height=625)
        self.wn.bgcolor("#BCDD7A")

    def get_player_count(self):
        valid_input = False
        while not valid_input:
            number_of_players = int(
                turtle.textinput("Connecting Dots", "Enter number of Players: ")
            )
            if number_of_players >= 2:
                valid_input = True
                self.number_of_players = number_of_players
            else:
                self.play_sound("sound/error.wav")
        self.play_sound("sound/message_box.mp3")

    def get_grid_size(self):
        valid_input = False
        while not valid_input:
            grid_size = int(turtle.textinput("Connecting Dots", "Enter Grid size: "))
            if 5 <= grid_size <= 10:
                valid_input = True
                self.grid_size = grid_size
            else:
                self.play_sound("sound/error.wav")
        self.play_sound("sound/message_box.mp3")

    def init_game_variables(self):
        self.count = 0
        self.dots = []
        self.connected_dots = []
        self.points = [0] * 10
        self.init_background_music()

    def init_background_music(self):
        pygame.mixer.music.load("sound/life_grand_background_music.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

    def setup_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                dot = turtle.Turtle()
                dot.shapesize(0.5, 0.5, 1)
                dot.speed(0)
                dot.color("#224E43")
                dot.penup()
                dot.shape("circle")
                dot.goto(
                    -100 - (self.grid_size - 5) * 25 + j * 50, 
                    100 + (self.grid_size - 5) * 25 - i * 50
                )
                self.dots.append(dot)

    def display_turn(self):
        self.turn = turtle.Turtle()
        self.turn.speed(0)
        self.turn.hideturtle()
        self.turn.penup()
        self.turn.goto(0, 250)
        self.turn.pencolor("#2A4A1A")
        self.turn.write(
            f"PLAYER {self.count % self.number_of_players + 1}'S TURN",
            align="center",
            font=("Cheri", 30, "bold"),
        )

    def game_over(self, winner):
        pygame.mixer.music.stop()
        time.sleep(3)
        self.wn.clear()
        self.wn.bgcolor("#5CB9BA")
        self.play_sound("sound/end.wav")
        self.show_message("GAME OVER", "Jokerman", 40, "#00011C")
        time.sleep(4)
        self.wn.clear()
        self.wn.bgcolor("#5CB9BA")
        self.play_sound("sound/end.mp3")
        self.show_message(f"PLAYER {winner} WINS!", "Jokerman", 30, "#00011C")
        time.sleep(7)
        turtle.bye()

    def show_message(self, text, font, size, color):
        message = turtle.Turtle()
        message.speed(0)
        message.hideturtle()
        message.penup()
        message.pencolor(color)
        message.write(text, align="center", font=(font, size, "normal"))
        self.wn.update()

    def distance(self, x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def check_and_draw_square(self, line):
        n = 0
        connected_x = []
        connected_y = []
        for i in range(len(self.connected_dots) - 1):
            if line[0] in self.connected_dots[i]:
                x1, y1 = line[1]
                x2, y2 = self.connected_dots[i][1 if line[0] == self.connected_dots[i][0] else 0]
                if self.distance(x1, y1, x2, y2) < 80:
                    connected_x.append(self.connected_dots[i][1 if line[0] == self.connected_dots[i][0] else 0])
            if line[1] in self.connected_dots[i]:
                x1, y1 = line[0]
                x2, y2 = self.connected_dots[i][1 if line[1] == self.connected_dots[i][0] else 0]
                if self.distance(x1, y1, x2, y2) < 80:
                    connected_y.append(self.connected_dots[i][1 if line[1] == self.connected_dots[i][0] else 0])

        for x in connected_x:
            for y in connected_y:
                for seg in self.connected_dots[:-1]:
                    if x in seg and y in seg and self.distance(x[0], x[1], y[0], y[1]) == 50:
                        self.draw_square(line, x, y, n)
                        n = 1 if n == 0 else n

    def draw_square(self, line, x, y, n):
        point = turtle.Turtle()
        point.speed(0)
        point.hideturtle()
        point.penup()
        a = min(line[0][0], line[1][0], x[0], y[0]) + 25
        b = min(line[0][1], line[1][1], x[1], y[1]) + 5
        point.goto(a, b)
        point.pencolor("#050B2B")
        time.sleep(1)
        self.play_sound("sound/get_bonus.wav")
        player = (self.count - 1) % self.number_of_players + 1 if n == 0 else self.count % self.number_of_players + 1
        point.write(f"{player}", align="center", font=("Berlin Sans FB", 30, "normal"))
        self.points[player] += 1
        if n == 0:
            self.count -= 1

    def draw_line(self, x, y):
        self.turn.clear()
        line = [dot.position() for dot in self.dots if dot.distance(x, y) < 35]
        if len(line) == 2 and line not in self.connected_dots:
            self.count += 1
            self.connected_dots.append(line)
            segment = turtle.Turtle()
            segment.hideturtle()
            segment.pencolor("#003554")
            segment.pensize(2)
            segment.penup()
            segment.goto(line[0])
            segment.pendown()
            segment.goto(line[1])
            self.play_sound("sound/click.wav")
            self.check_and_draw_square(line)
        self.update_turn_display()
        if sum(self.points) == (self.grid_size - 1) ** 2:
            self.game_over(self.points.index(max(self.points)))

    def update_turn_display(self):
        self.turn.goto(0, 250)
        self.turn.pencolor("#2A4A1A")
        self.turn.write(
            f"PLAYER {self.count % self.number_of_players + 1}'S TURN",
            align="center",
            font=("Cheri", 30, "bold"),
        )

    def run(self):
        turtle.onscreenclick(self.draw_line)
        turtle.mainloop()

if __name__ == "__main__":
    game = ConnectDotsGame()
    game.run()
