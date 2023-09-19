import turtle
import random
import S1510_turtle_hunt_classes_constants as Tclass
from S1520_turtle_hunt_service import distance

# Do NOT change these global constants!
MAX_POS = 300
BOUNCE_STEP_SIZE = 2 * Tclass.STEP_SIZE
START_ANGLES_MIN = [0, 90, 180, 270]
START_ANGLES_MAX = [30, 120, 210, 300]
START_DISTANCE_MIN = int(MAX_POS * 0.6)
START_DISTANCE_MAX = int(MAX_POS * 0.9)


def move(turtle_):
    turtle_.forward(Tclass.STEP_SIZE)
    x, y = turtle_.position()
    if abs(x) > MAX_POS or abs(y) > MAX_POS:
        turtle_.right(180)
        turtle_.forward(BOUNCE_STEP_SIZE)
        turtle_.right(180)


def caught(turtles_, max_distance):
    positions = [t.position() for t in turtles_]
    for hunter_position in positions[1:]:
        if distance(positions[0], hunter_position) < max_distance:
            return True
    return False


def init_positions(turtles_):
    for turtle_, min_angle, max_angle in zip(turtles_, START_ANGLES_MIN, START_ANGLES_MAX):
        angle = random.randint(min_angle, max_angle)
        turtle_.right(angle)
        turtle_.penup()
        turtle_.forward(random.randint(START_DISTANCE_MIN, START_DISTANCE_MAX))
        turtle_.right(-angle)
        turtle_.pendown()


def hunt(prey_class, hunter_class, color):
    screen = turtle.Screen()
    screen.setup(2 * MAX_POS, 2 * MAX_POS)
    prey = prey_class()
    hunters = [hunter_class() for _ in range(3)]
    turtles = [prey] + hunters
    prey.pencolor(color)
    for t in turtles:
        t.speed(Tclass.SPEED)
        t.shape("turtle")
    init_positions(turtles)

    turn = 0
    positions = [t.position() for t in turtles]
    while not caught(turtles, Tclass.CAUGHT_DISTANCE) and turn < Tclass.MAX_TURNS:
        turn += 1
        for h in hunters:
            h.right(h.rotate_hunter(positions))
        prey.right(prey.rotate_prey(positions))
        for t in turtles:
            move(t)
            positions = [t.position() for t in turtles]

    turtle.clearscreen()
    if turn < Tclass.MAX_TURNS:
        print(f'Caught after {turn} turns.')
    else:
        print(f'Prey not caught after {turn} turns. Prey receives {turn} bonus points on top.')
        turn *= 2
    return turn


score1 = score2 = 0
for r in range(Tclass.ROUNDS):
    print(f"{Tclass.class1.__name__} is hunting {Tclass.class2.__name__}")
    score1 += hunt(Tclass.class1, Tclass.class2, "red")
    print(f"{Tclass.class2.__name__} is hunting {Tclass.class1.__name__}")
    score2 += hunt(Tclass.class2, Tclass.class1, "green")
    print(f"##### Score after round {r + 1}: {Tclass.class1.__name__}: {score1}    {Tclass.class2.__name__}: {score2} #####")

turtle.done()
