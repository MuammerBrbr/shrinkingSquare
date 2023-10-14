import turtle

drawing_board = turtle.Screen()
drawing_board.title("Shrinking Square")
drawing_board.bgcolor("light blue")

turtle_instance = turtle.Turtle()
turtle_instance.color("red")

def shrinkingSqurare(size,angle):
    for i in range(4):
         turtle_instance.forward(size)
         turtle_instance.left(angle)
         size = size - 5

shrinkingSqurare(200,90)
shrinkingSqurare(180,90)
shrinkingSqurare(160,90)
shrinkingSqurare(140,90)
shrinkingSqurare(120,90)
shrinkingSqurare(100,90)
shrinkingSqurare(80,90)
shrinkingSqurare(60,90)
shrinkingSqurare(40,90)
shrinkingSqurare(20,90)
shrinkingSqurare(0,90)

turtle.done()