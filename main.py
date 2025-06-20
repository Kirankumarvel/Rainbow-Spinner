import turtle
import random
import time
from utils.color_utils import generate_gradient_colors

def setup_screen():
    """Set up the turtle screen with a dark background"""
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Rainbow Spinner")
    screen.tracer(0)  # Turn off automatic screen updates
    return screen

def create_spinner():
    """Create and configure the turtle for drawing"""
    spinner = turtle.Turtle()
    spinner.speed(0)  # Fastest speed
    spinner.width(3)
    spinner.hideturtle()
    return spinner

def draw_rainbow_spinner(spinner, size=300, speed=5):
    """Draw the rainbow spinner pattern"""
    colors = generate_gradient_colors(7)  # Get colors from our utility
    
    for i in range(size):
        spinner.color(colors[i % len(colors)])
        spinner.forward(i)
        spinner.right(45 + speed)
        
        if i % 20 == 0:
            spinner.width(random.randint(1, 5))

def main():
    screen = setup_screen()
    spinner = create_spinner()
    
    try:
        while True:
            spinner.clear()
            draw_rainbow_spinner(spinner)
            screen.update()  # Manual screen update
            time.sleep(0.05)
            spinner.right(2)
    except:
        print("Animation stopped")
        screen.bye()

if __name__ == "__main__":
    main()