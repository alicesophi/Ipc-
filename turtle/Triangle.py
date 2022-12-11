import turtle
 
screen=turtle.Screen() 
my_turtle=turtle.Turtle() 
 
def triangle(x,y)
   
    my_turtle.penup()
    my_turtle.goto(x,y) # x e y são as coordenadas do triângulo
    my_turtle.pendown()
    
    for i in range(3):
        my_turtle.forward(100)
        my_turtle.left(120)
        my_turtle.forward(100)
         
turtle.onscreenclick(triangle,1)
turtle.listen()
turtle.done()