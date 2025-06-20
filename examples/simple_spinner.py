import turtle

def simple_spinner():
    screen = turtle.Screen()
    screen.bgcolor("black")
    
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    
    for i in range(100):
        t.color(colors[i % len(colors)])
        t.circle(100)
        t.left(10)
    
    screen.mainloop()

if __name__ == "__main__":
    simple_spinner()