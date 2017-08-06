import turtle
import random
import time

turtle.tracer(1,0)

SIZE_X1=800
SIZE_Y1=500
turtle.setup(SIZE_X1, SIZE_Y1)
SIZE_X=700
SIZE_Y=400
turtle.penup()

SQUARE_SIZE=20
START_LENGTH=5

pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]
score=0
score_list=[]
snake=turtle.clone()
snake.shape("square")

turtle.hideturtle()

for loop1 in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)

    pos_list.append(my_pos)
    stamp1=snake.stamp()
    stamp_list.append(stamp1)

UP_ARROW="Up"

LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100
SPACEBAR="space"
UP=0
DOWN=1
LEFT=2
RIGHT=3

direction=UP
UP_EDGE=200
DOWN_EDGE=-200
RIGHT_EDGE=350
LEFT_EDGE=-350

box=turtle.clone()
box.shape("blank")
box.pensize(2)
box.color("magenta")
box.penup()
box.goto(-350,200)
box.pendown()
box.goto(350,200)
box.goto(350,-200)
box.goto(-350,-200)
box.goto(-350,200)
def up():
    global direction
    if direction!=DOWN:
        direction=UP
    print('you pressed the UP key!')

def left():
    global direction
    if direction!=RIGHT:
        direction=LEFT
    print('you pressed the LEFT key!')

def down():
    global direction
    if direction!=UP:
        direction=DOWN
    print('you pressed the DOWN key!')

def right():
    global direction
    if direction!=LEFT:     
        direction=RIGHT
    print('you pressed the RIGHT key!')

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.listen()

turtle.register_shape("trash.gif")
food=turtle.clone()
food.shape("trash.gif")
food.hideturtle()
def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    new_food = food.stamp()
    food_stamps.append(new_food)
num=turtle.clone()

def score_sleep():
    global num
    time.sleep(3)
    num.clear()
def move_snake():
    global score , score_list
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]

    if direction==RIGHT:
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
        print('you moved right')
    elif direction==LEFT:
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
        print('you moved left')
    elif direction==UP:
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print('you moved up')
    elif direction==DOWN:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
        print('you moved down')


    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)
    #special place for part 5
    
    if snake.pos() in food_pos:
        global num
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print('you have eaten the food!')
        make_food()
        make_food()
        num.clear()
        score = score + 1
        score_list.append(score)
        num.goto(-350,200)
        num.write(score,font=("Arial",18, "normal"))
        #score_sleep()
    else:
        old_stamp=stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]
    if new_x_pos >=RIGHT_EDGE:
        print('you hit the right edge! game over!')
        turtle.write("you hit the right edge! game over!",align="center",font=("Arial",18, "normal"))
        import time
        time.sleep(1) 
        quit()
    elif new_x_pos <=LEFT_EDGE:
        print('you hit the left edge! game over!')
        turtle.write("you hit the left edge! game over!",align="center",font=("Arial",18, "normal"))
        import time
        time.sleep(1)
        quit()
    elif new_y_pos <=DOWN_EDGE:
        print('you hit the down edge! game over!')
        turtle.write("you hit the down edge! game over!",align="center",font=("Arial",18, "normal"))
        import time
        time.sleep(1) 
        quit()
    elif new_y_pos >=UP_EDGE:
        print('you hit the up edge! game over!')
        turtle.write("you hit the up edge! game over!",align="center",font=("Arial",18, "normal"))
        import time
        time.sleep(1) 
        quit()
    
    if snake.pos() in pos_list[0:-1]:
        quit()
    turtle.ontimer(move_snake,TIME_STEP)
    
        
    
move_snake()
make_food()


##turtle.register_shape("trash.gif")
##food=turtle.clone()
##food.shape("trash.gif")
##
##food_pos=[(100,100),(-100,100),(-100,-100),(100,-100)]
##food_stamps=[]
##food.hideturtle()
##
##turtle.pendown()
##for this_food_pos in food_pos:
##    food.goto(this_food_pos)
##    food_stamp = food.stamp()
##    food_stamps.append(food_stamp)
    
    
    
if food.pos() in pos_list[:-1]:
    make_food()
    


















