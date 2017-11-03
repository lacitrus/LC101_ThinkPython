# creat n-pointed star

import turtle

def draw_star(turtle, n):
    for i in range(n):
        turtle.forward(100)
        turtle.right(180-180/n)
        
def main():
    tess = turtle.Turtle()
    draw_star(tess, 9)  
    
if __name__ == "__main__":
    main()
