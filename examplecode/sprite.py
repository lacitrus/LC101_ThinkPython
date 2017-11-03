#draw sprite with n number of legs and leg length

import turtle

def draw_sprite(sprite, n, length):
    
    for i in range(n):
        sprite.right(360/n)
        sprite.forward(length)
        sprite.stamp()
        sprite.right(180)
        sprite.forward(length)
        sprite.right(180)
def main():

    tess = turtle.Turtle()
    tess.speed(10)
    draw_sprite(tess, 15, 120)
    
if __name__ == "__main__":
    main()
