from turtle import Turtle

STARTING_POSITION = (0, -260)
FINISH_LINE = 300

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("brown")
        self.penup()
        self.spawn()

    def spawn(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(10)

    def check_collision(self, car):
        player_ycor = self.ycor()
        car_ycor = car.ycor()
        distance = self.distance(car)
        # print(f"Checking collision with {car}")
        # print(f"player_ycor {type(player_ycor)}{player_ycor}")
        # print(f"car_ycor {type(car_ycor)}{car_ycor}")
        # print(f"abs car_ycor - player_ycor {type(abs(car_ycor - player_ycor))}{abs(car_ycor - player_ycor)}")
        # print(f"self.distance(car) {type(distance)}{distance}")
        if int(abs(car_ycor - player_ycor)) <= 15 and int(distance) <= 20:
            print("\t\t\t\t ************************ Collision ! Mayday !\n\n")
            return False
        else:
            return True

    def check_win(self):
        player_ycor = self.ycor()
        if player_ycor >= FINISH_LINE:
            return True
        else:
            return False
