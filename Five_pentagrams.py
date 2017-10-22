#Use turtle to draw five pentagrams on the screen.

import turtle


def draw_star(turtle):
    for i in range(5):
        turtle.forward(100)
        turtle.right(180-36)

def main():       
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    
    tess = turtle.Turtle() 
    tess.color("salmon","salmon")
    tess.penup()
    tess.back(170)
    tess.left(80)
    tess.forward(50)
    tess.right(80)
    tess.pendown()
    tess.speed(10)
    
    for i in range(5):
        tess.begin_fill()
        draw_star(tess)
        tess.end_fill()
        tess.penup()
        tess.forward(350)
        tess.right(144)
        tess.pendown()
        
    
if __name__ == "__main__":
    main()


