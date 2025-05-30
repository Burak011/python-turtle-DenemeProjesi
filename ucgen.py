import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#F3F3E0") #kod ile de renk verilebilir
drawing_board.title("Üçgen Çizimi")

turtle_instance = turtle.Turtle()
for i in range(3):
    turtle_instance.forward(100)
    turtle_instance.left(120)

turtle.done() #çizim işlemi tamamlandıktan sonra pencereyi kapatmamak için kullanılır.