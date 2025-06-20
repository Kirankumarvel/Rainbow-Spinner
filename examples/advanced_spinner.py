import turtle
import time
import math
from utils.color_utils import generate_gradient_colors

def advanced_spinner():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.tracer(0)
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    
    colors = generate_gradient_colors(12)
    size = 150
    
    try:
        while True:
            t.clear()
            for i in range(72):
                t.color(colors[i % len(colors)])
                t.width(1 + math.sin(i/10) * 3)
                t.forward(size)
                t.backward(size)
                t.right(5)
            screen.update()
            time.sleep(0.05)
            size = 150 + 50 * math.sin(time.time())
    except:
        screen.bye()

if __name__ == "__main__":
    advanced_spinner()