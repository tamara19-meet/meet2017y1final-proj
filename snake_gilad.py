import turtle
import random
import time


turtle.tracer(1, 0)

size_X = 800
size_Y = 500
turtle.setup(size_X, size_Y)

turtle.penup()

square_size = 20
start_length = 5

pos_list = []
stamp_list = []
food_pos = []
food_stamp = []
score = []

snake = turtle.clone()
snake.shape("square")

turtle.hideturtle()

for num in range(start_length):
        x_pos = snake.pos()[0]
        y_pos = snake.pos()[1]
        x_pos = x_pos + square_size
        my_pos = (x_pos, y_pos)
        snake.goto(my_pos)
        pos_list.append(my_pos)
        stamp_id = snake.stamp()
        stamp_list.append(stamp_id)

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
TIME_STEP = 100
SPACEBAR = "space"

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

#call functions
def up():
    global direction
    if direction != DOWN:
        direction = UP
        print("You pressed the up key!")
def left():
    global direction
    if direction != RIGHT:
        direction = LEFT
        print("You pressed the left key!")
def down():
    global direction
    if direction != UP:
        direction = DOWN
        print("You pressed the down key!")
def right():
    global direction
    if direction != LEFT:
        direction = RIGHT
        print("You pressed the right key!")

#make turtle listen
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()


#location of food

food = turtle.clone()
food.shape("circle")
food.hideturtle()
food_pos = []
food_stamps = []
def make_food():
    
    min_x = -int(size_X/2/square_size)+1
    max_x = int(size_X/2/square_size)-1
    min_y = -int(size_Y/2/square_size)+1
    max_y = int(size_Y/2/square_size)-1

    food_x = random.randint(min_x, max_x)*square_size
    food_y = random.randint(min_y, max_y)*square_size

    pos_food = (food_x, food_y)
    
    food.goto(food_x, food_y)
    food_id = food.stamp()
    food_stamps.append(food_id)
    food_pos.append(pos_food)

#make turtle move
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction == RIGHT:
        snake.goto(x_pos + square_size, y_pos)
        print("You moved right!")
    elif direction == LEFT:
        snake.goto(x_pos - square_size, y_pos)
        print("You moved left!")
    elif direction == UP:
        snake.goto(x_pos, y_pos + square_size)
        print("You moved up!")
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - square_size)
        print("You moved down!")

    # stamp and record the snake's head
    my_pos = snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)

    # if the snake is eating food
    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        score.append(food_ind)
        food_stamps.pop(food_ind)
        print("You have eaten a food!")
        make_food()
        turtle.clear()
        turtle.goto(200, 200)
        turtle.write(len(score), font = ("Arial", 30))
        turtle .goto(-300, 0)
    else:
        # cleartsamps the tail and makes storage edits
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        turtle.write("You hit the right edge! game over!", font = ("Ariel", 30))
        time.sleep(2)
        quit()

    elif new_x_pos <= LEFT_EDGE:
        turtle.write("You hit the left edge! game over!", font = ("Ariel", 30))
        time.sleep(2)
        quit()

    elif new_y_pos >= UP_EDGE:
        turtle.write("You hit the up edge! game over!", font = ("Ariel", 30))
        time.sleep(2)
        quit()

    elif new_y_pos <= DOWN_EDGE:
        turtle.write("You hit the down edge! game over!", font = ("Ariel", 30))
        time.sleep(2)
        quit(pos_list)
        
    if pos_list[-1] in pos_list[0:-1]:
        turtle.write("you hit yourself!", font = ("Ariel", 30))
        time.sleep(2)
        quit()
        
    turtle.ontimer(move_snake, TIME_STEP)

move_snake()
make_food()
