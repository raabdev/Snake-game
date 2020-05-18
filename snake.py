import turtle
import time

posponer = 0.1

#Configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego")
wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.tracer(0)

#Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.penup()
cabeza.color("white")
cabeza.shape("square")
cabeza.goto(0, 0)
cabeza.direction = "up"

#Funciones
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


#Bucle
while True:
    wn.update()

    mov()
    time.sleep(posponer)
