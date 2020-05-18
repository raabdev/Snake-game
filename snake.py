import turtle
import time
import random

posponer = 0.1

#Configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego")
wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.tracer(0)

#Cabeza Serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.penup()
cabeza.color("white")
cabeza.shape("square")
cabeza.goto(0, 0)
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.penup()
comida.color("red")
comida.shape("circle")
comida.goto(random.randint(-280, 280), random.randint(-280, 280))

#Cuerpo Serpiente
segmentos = []

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0        High Score: 0", align="center", font=("Courier", 24, "normal"))

#Marcador
score = 0
high_score = 0

#Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

#Bucle
while True:
    wn.update()

    #Colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

        #Esconder los segmentos
        for segmento in segmentos:
            segmento.goto(1000, 1000)

        #Limpiar lista segmentos
        segmentos.clear()

        #Resetear marcador
        score = 0
        texto.clear()
        texto.write("Score: {}        High Score: {}".format(score, high_score), align="center",
                    font=("Courier", 24, "normal"))


    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.penup()
        nuevo_segmento.color("grey")
        nuevo_segmento.shape("square")
        segmentos.append(nuevo_segmento)

        #Aumentar marcador
        score += 10

        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Score: {}        High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg - 1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mov()

    #Colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"

            #Esconder los elementos
            for segmento in segmentos:
                segmento.goto(1000, 1000)

            segmentos.clear()

            # Resetear marcador
            score = 0
            texto.clear()
            texto.write("Score: {}        High Score: {}".format(score, high_score), align="center",
                        font=("Courier", 24, "normal"))

    time.sleep(posponer)
