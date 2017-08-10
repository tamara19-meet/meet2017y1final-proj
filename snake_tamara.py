import turtle
import random
import time
  


level = input("In level 1, both snakes' speeds are the same. In level 2, they are different! Pick a level 1/2")
if level == '1':
    TIME_STEP = 100
    TIME_STEP1 = 100
elif level == '2':
    TIME_STEP = 50
    TIME_STEP1 = 150

turtle.tracer(1, 0)

size_X1 = 1000
size_Y1 = 700
turtle.setup(size_X1, size_Y1)
size_X=700
size_Y=400
turtle.penup()


square_size = 20
start_length = 5
wn=turtle.Screen()
wn.title("2 players snake")


pos_list = []
stamp_list = []
pos_list1 = []
stamp_list1 = []
food_pos = []
food_stamp = []
score = []
score1 = []

turtle1 = turtle.clone()
turtle.hideturtle()
turtle1.hideturtle()
turtle3= turtle.clone()
turtle3.hideturtle()
turtle2 = turtle.clone()
turtle2.hideturtle()

###
if level == "2":
    turtle.goto(0,200)
    turtle.color("blue")
    turtle.write("The blue snake player plays with the arrow keys", font = ("Ariel", 30), align="center")
    turtle1.goto(0,100)
    turtle1.color("blue")
    turtle1.write("In addition, he is FASTER than the other", font = ("Ariel", 30), align="center")
    turtle2.goto(0,-100)
    turtle2.color("yellow")
    turtle2.write("The yellow snake player plays with the W,S,A,D keys", font = ("Ariel", 28), align="center")
    turtle3.goto(0,-200)
    turtle3.color("yellow")
    turtle3.write("In addition, he is SLOWER than the other", font = ("Ariel", 30), align="center")
    time.sleep(5)
    turtle.clear()
    turtle1.clear()
    turtle2.clear()
    turtle3.clear()

elif level == "1":
    turtle.goto(0,200)
    turtle.color("blue")
    turtle.write("The blue snake player plays with the arrow keys", font = ("Ariel", 30), align="center")
    turtle1.goto(0,100)
    turtle1.color("blue")
    turtle2.goto(0,-100)
    turtle2.color("yellow")
    turtle2.write("The yellow snake player plays with the W,S,A,D keys", font = ("Ariel", 28), align="center")
    turtle3.goto(0,-200)
    turtle3.color("yellow")
    time.sleep(5)
    turtle.clear()
    turtle1.clear()
    turtle2.clear()
    turtle3.clear()
###

snake = turtle.clone()
snake.shape("square")
snake.color('blue')

snake1 = turtle.clone()
snake1.shape("square")
snake1.color('yellow')

###
snake.home()
snake1.home()
###

for num in range(start_length):
        x_pos = snake.pos()[0]
        y_pos = snake.pos()[1]
        x_pos = x_pos + square_size
        my_pos = (x_pos, y_pos)
        snake.goto(my_pos)
        pos_list.append(my_pos)
        stamp_id = snake.stamp()
        stamp_list.append(stamp_id)

for num1 in range(start_length):
        x_pos1 = snake1.pos()[0]
        y_pos1 = snake1.pos()[1]
        x_pos1 = x_pos1 + square_size
        my_pos1 = (x_pos1, y_pos1)
        snake1.goto(my_pos1)
        pos_list1.append(my_pos1)
        stamp_id1 = snake1.stamp()
        stamp_list1.append(stamp_id1)

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"

RIGHT_ARROW1 = "d"
LEFT_ARROW1 = "a"
UP_ARROW1 = "w"
DOWN_ARROW1 = "s"




SPACEBAR = "space"

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

UP1 = 4
LEFT1 = 5
DOWN1 = 6
RIGHT1 = 7

direction = UP
direction1 = DOWN1

UP_EDGE = 300
DOWN_EDGE = -300
RIGHT_EDGE = 450
LEFT_EDGE = -450

box=turtle.clone()
box.shape("blank")
box.pensize(2)
box.color("green")
box.penup()
box.goto(-450,300)
box.pendown()
box.goto(450,300)
box.goto(450,-300)
box.goto(-450,-300)
box.goto(-450,300)

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


def up1():
    global direction1
    if direction1 != DOWN1:
        direction1 = UP1
        print("Player2 pressed the up key!")
def left1():
    global direction1
    if direction1 != RIGHT1:
        direction1 = LEFT1
        print("You pressed the left key!")
def down1():
    global direction1
    if direction1 != UP1:
        direction1 = DOWN1
        print("You pressed the down key!")
def right1():
    global direction1
    if direction1 != LEFT1:
        direction1 = RIGHT1
        print("You pressed the right key!")

#make turtle listen snake
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

#make turtle listen snake1
turtle.onkeypress(up1, UP_ARROW1)
turtle.onkeypress(left1, LEFT_ARROW1)
turtle.onkeypress(down1, DOWN_ARROW1)
turtle.onkeypress(right1, RIGHT_ARROW1)
turtle.listen()

#location of food

turtle.register_shape("sushi.gif")
food=turtle.clone()
food.shape("sushi.gif")
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

#make turtle move snake
def move_snake():

    global direction
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
        turtle.goto(0,0)
        turtle.write("The blue snake hit the right edge! game over!", font = ("Ariel", 30), align="center")
        time.sleep(2)
        quit()

    elif new_x_pos <= LEFT_EDGE:
        turtle.goto(0,0)
        turtle.write("The blue snake hit the left edge! game over!", font = ("Ariel", 30), align="center")
        time.sleep(2)
        quit()

    elif new_y_pos >= UP_EDGE:
        turtle.goto(0,0)
        turtle.write("The blue snake hit the up edge! game over!", font = ("Ariel", 30), align="center")
        time.sleep(2)
        quit()

    elif new_y_pos <= DOWN_EDGE:
        turtle.goto(0,0)
        turtle.write("The blue snake hit the down edge! game over!", font = ("Ariel", 30), align="center")
        time.sleep(2)
        quit(pos_list)
        
    if pos_list[-1] in pos_list[0:-1]:
        turtle.goto(0,0)
        turtle.write("The blue snake hit herself!", font = ("Ariel", 30), align="center")
        time.sleep(2)
        quit()
        
    turtle.ontimer(move_snake, TIME_STEP)

def move_snake1():

    global direction1
    my_pos1 = snake1.pos()
    x_pos1 = my_pos1[0]
    y_pos1 = my_pos1[1]
    
    if direction1 == RIGHT1:
        print("player2 is moving")
        snake1.goto(x_pos1 + square_size, y_pos1)
        print("You moved right!")
    elif direction1 == LEFT1:
        snake1.goto(x_pos1 - square_size, y_pos1)
        print("You moved left!")
    elif direction1 == UP1:
        snake1.goto(x_pos1, y_pos1 + square_size)
        print("You moved up!")
    elif direction1 == DOWN1:
        snake1.goto(x_pos1, y_pos1 - square_size)
        print("You moved down!")

    # stamp and record the snake's head
    my_pos1 = snake1.pos()
    pos_list1.append(my_pos1)
    new_stamp1 = snake1.stamp()
    stamp_list1.append(new_stamp1)

    # if the snake is eating food
    if snake1.pos() in food_pos:
        food_ind1 = food_pos.index(snake1.pos())
        food.clearstamp(food_stamps[food_ind1])
        food_pos.pop(food_ind1)
        score1.append(food_ind1)
        food_stamps.pop(food_ind1)
        print("You have eaten a food!")
        make_food()
        turtle1.clear()
        turtle1.goto(-200, 200)
        turtle1.color("yellow")
        turtle1.write(len(score1), font = ("Arial", 30), align="center")
        turtle1.goto(-300, 0)
    else:
        # cleartsamps the tail and makes storage edits
        old_stamp1 = stamp_list1.pop(0)
        snake1.clearstamp(old_stamp1)
        pos_list1.pop(0)

    new_pos1 = snake1.pos()
    new_x_pos1 = new_pos1[0]
    new_y_pos1 = new_pos1[1]

    if new_x_pos1 >= RIGHT_EDGE:
        turtle.goto(0,0)
        turtle.color("yellow")
        turtle.write("The yellow snake hit the right edge! game over!", font = ("Ariel", 30), align="center")
        time.sleep(2)
        quit()

    elif new_x_pos1 <= LEFT_EDGE:
        turtle.goto(0,0)
        turtle.color("yellow")
        turtle.write("The yellow snake hit the left edge! game over!", font = ("Ariel", 30), align="center")
        time.sleep(2)
        quit()

    elif new_y_pos1 >= UP_EDGE:
        turtle.goto(0,0)
        turtle.color("yellow")
        turtle.write("The yellow snake hit the up edge! game over!", font = ("Ariel", 30), align="center")
        time.sleep(2)
        quit()

    elif new_y_pos1 <= DOWN_EDGE:
        turtle.goto(0,0)
        turtle.color("yellow")
        turtle.write("The yellow snake hit the down edge! game over!", font = ("Ariel", 30), align="center")
        time.sleep(2)
        quit(pos_list)
        
    if pos_list1[-1] in pos_list1[0:-1]:
        turtle.goto(0,0)
        turtle.color("yellow")
        turtle.write("The yellow snake hit himself!", font = ("Ariel", 30), align="center")
        time.sleep(2)
        quit()
        
    turtle.ontimer(move_snake1, TIME_STEP1)


move_snake()
move_snake1()
make_food()






