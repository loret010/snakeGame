import turtle
import time
import random

delay = 0.1

# Punteggio iniziale
score = 0
high_score = 0
paused = False  # Serve per mettere in pausa il gioco

# Imposta la finestra e il background.
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.bgpic("background.gif")
wn.setup(width=600, height=600)
wn.tracer(0)

# IMPORTANTE -- In questa parte bisogna ancora lavorarci, non togliere il # oppure si rompe tutto.

# Registra le immagini
# try:
   # turtle.register_shape("snakeHead.gif")  # Foto snake
   # turtle.register_shape("food.gif")    # Foto cibo
# except turtle.TurtleGraphicsError as e:
  #  print(f"Errore mentre registra le immagini: {e}")

# Testa snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("darkGreen")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Cibo snake
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Funzioni
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def toggle_pause():
    global paused
    paused = not paused  # Mette in pausa/toglie la pausa
    if paused:
        pen.goto(0, 0)
        pen.write("In pausa", align="center", font=("Courier", 24, "normal"))
    else:
        pen.clear()
        pen.goto(0, 260)
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

def quit_game():
    wn.bye()  # Chiude il gioco


# Comandi tastiera
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(toggle_pause, "p")
wn.onkeypress(quit_game, "q")


# Main Loop del gioco
while True:
    wn.update()

    if paused:
        continue  # Salta il loop se il gioco è in pausa

    # Controlla se va sul bordo
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        # Nasconde i segmenti
        for segment in segments:
            segment.goto(1000, 1000)

        # Cancella i segmenti
        segments.clear()

        # Reset del punteggio
        score = 0

        # Ritardo del reset
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Controlla se va a contatto con il cibo
    if head.distance(food) < 20:
        # Porta il cibo in un'altra posizione random
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Aggiunge un segmento allo snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Ritardo
        delay -= 0.001

        # Aggiunge al punteggio
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Segmento 0 è la testa
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Controlla se va a contatto con il corpo dello snake
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            # Nasconde i segmenti
            for segment in segments:
                segment.goto(1000, 1000)

            # Cancella i segmenti
            segments.clear()

            # Reset il punteggio
            score = 0

            # Ritardo del reset
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)
