from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("brown")
        self.penup()
        self.goto(0, -260)
        self.setheading(90)

    def move(self):
        self.forward(10)

    # TODO: Somehow the distance part is not working and the whole collision is fucked
    def check_collision(self, car):
        print(f"Checking collision with {car}")
        player_ycor = self.ycor()
        car_ycor = car.ycor()
        distance = self.distance(car)
        print(f"player_ycor {player_ycor}")
        print(f"car_ycor {car_ycor}")
        print(f"abs car_ycor - player_ycor {abs(car_ycor - player_ycor)}")
        print(f"self.distance(car) {distance}\n\n")
        if abs(car_ycor - player_ycor) <= 15 and distance <= 15:
            return False
        else:
            return True
