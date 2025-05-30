import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#537D5D")
drawing_board.title("Yıldız Çizimi")

turtle_instance = turtle.Turtle()
for i in range(5):
    turtle_instance.forward(100)
    turtle_instance.right(144)  # Yıldız çizimi için 144 derece döndürülür

turtle.done()  # Çizim işlemi tamamlandıktan sonra pencereyi kapatmamak için kullanılır.