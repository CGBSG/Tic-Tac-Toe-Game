
# Required libraries
# First, turtle for graphics
# Second, for single-player mode
# Third, for stopping the game
from turtle import *
from sys import *  # Library used for exiting the game
from random import *
from time import *

# Initial settings for the turtle
title("                               XO _GAME ")
shape('turtle')
speed(0.1)
ht()  # Hide the turtle
up()  # Lift the pen
# Clear the screen
setup(0, 0)

# Variables for AI (to remember which squares the user clicked to avoid re-clicking)
cfg = ["933",
       "y", "y", "y",
       "y", "y", "y",
       "y", "y", "y"]
# 933 in two variables to ignore the 0th index
index = [993,
         0, 0, 0,
         0, 0, 0,
         0, 0, 0]

# Function for correct selection in hard and normal modes
# This function is similar to the Minimax algorithm
# The Minimax algorithm is the algorithm used to bring this game into the virtual world
def Help_Bot(lists, numberes, D_or_S: str):
    # If it's for drawing, it sends suitable positions for the AI to draw
    if D_or_S == "D":
        n = numberes
    # But if it's to prevent the user from winning
    elif D_or_S == "S":
        a = numberes
        notn = ["X", "O"]
        if a == notn[0]:
            n = notn[1]
        else:
            n = notn[0]

    functions = [0]
    # Choosing the best move
    for i in n:
        if (((lists[1] == i and lists[2] == i and cfg[3] == "y") or # 3
            (lists[2] == i and lists[3] == i and cfg[1] == "y") or  # 1
            (lists[4] == i and lists[5] == i and cfg[6] == "y") or  # 6
            (lists[5] == i and lists[6] == i and cfg[4] == "y") or  # 4
            (lists[7] == i and lists[8] == i and cfg[9] == "y") or  # 9
            (lists[8] == i and lists[9] == i and cfg[7] == "y")) or # 7
            (lists[1] == i and lists[4] == i and cfg[7] == "y") or  # 7
            (lists[4] == i and lists[7] == i and cfg[1] == "y") or  # 1
            (lists[2] == i and lists[5] == i and cfg[8] == "y") or  # 8
            (lists[5] == i and lists[8] == i and cfg[2] == "y") or  # 2
            (lists[3] == i and lists[6] == i and cfg[9] == "y") or  # 9
            (lists[6] == i and lists[9] == i and cfg[3] == "y") or  # 3
            ((lists[1] == i and lists[5] == i and cfg[9] == "y") or # 9
            (lists[5] == i and lists[9] == i and cfg[1] == "y") or  # 1
            (lists[3] == i and lists[5] == i and cfg[7] == "y") or  # 7
            (lists[5] == i and lists[7] == i and cfg[3] == "y")) or # 3
            (lists[1] == i and lists[3] == i and cfg[2] == "y") or  # 2 #
            (lists[4] == i and lists[6] == i and cfg[5] == "y") or  # 5 #
            (lists[7] == i and lists[9] == i and cfg[8] == "y") or  # 8 #
            (lists[1] == i and lists[7] == i and cfg[4] == "y") or  # 4 #
            (lists[2] == i and lists[8] == i and cfg[5] == "y") or  # 5 #
            (lists[3] == i and lists[9] == i and cfg[6] == "y") or  # 6 #
            (lists[1] == i and lists[9] == i and cfg[5] == "y") or  # 5 #
            (lists[7] == i and lists[3] == i and cfg[5] == "y")):   # 5 #
            functions.remove(0)
            if lists[1] == i and lists[2] == i and cfg[3] == "y":  # 3
                # Adding the move
                functions.append(3)
            if lists[2] == i and lists[3] == i and cfg[1] == "y":  # 1
                functions.append(1)
            if lists[4] == i and lists[5] == i and cfg[6] == "y":  # 6
                functions.append(6)
            if lists[5] == i and lists[6] == i and cfg[4] == "y":  # 4
                functions.append(4)
            if lists[7] == i and lists[8] == i and cfg[9] == "y":  # 9
                functions.append(9)
            if lists[8] == i and lists[9] == i and cfg[7] == "y":  # 7
                functions.append(7)
            if lists[1] == i and lists[4] == i and cfg[7] == "y":  # 7
                functions.append(7)
            if lists[4] == i and lists[7] == i and cfg[1] == "y":  # 1
                functions.append(1)
            if lists[2] == i and lists[5] == i and cfg[8] == "y":  # 8
                functions.append(8)
            if lists[5] == i and lists[8] == i and cfg[2] == "y":  # 2
                functions.append(2)
            if lists[3] == i and lists[6] == i and cfg[9] == "y":  # 9
                functions.append(9)
            if lists[6] == i and lists[9] == i and cfg[3] == "y":  # 3
                functions.append(3)
            if lists[1] == i and lists[5] == i and cfg[9] == "y":  # 9
                functions.append(9)
            if lists[5] == i and lists[9] == i and cfg[1] == "y":  # 1
                functions.append(1)
            if lists[3] == i and lists[5] == i and cfg[7] == "y":  # 7
                functions.append(7)
            if lists[5] == i and lists[7] == i and cfg[3] == "y":  # 3
                functions.append(3)

            if lists[1] == i and lists[3] == i and cfg[2] == "y":  # 2 #
                functions.append(2)
            if lists[4] == i and lists[6] == i and cfg[5] == "y":  # 5 #
                functions.append(5)
            if lists[7] == i and lists[9] == i and cfg[8] == "y":  # 8 #
                functions.append(8)
            if lists[1] == i and lists[7] == i and cfg[4] == "y":  # 4 #
                functions.append(4)
            if lists[2] == i and lists[8] == i and cfg[5] == "y":  # 5 #
                functions.append(5)
            if lists[3] == i and lists[9] == i and cfg[6] == "y":  # 6 #
                functions.append(6)
            if lists[1] == i and lists[9] == i and cfg[5] == "y":  # 5 #
                functions.append(5)
            if lists[7] == i and lists[3] == i and cfg[5] == "y":  # 5 #
                functions.append(5)

    # Returning the positions
    return functions

# Function to draw a rectangle
def sharp(w, h):
    for s in range(2):
        fd(h)
        lt(90)
        fd(w)
        lt(90)

# Function for single-player mode (to select difficulty)
def starthard1():
    # Main settings for the turtle
    reset()
    ht()
    speed(0.1)
    setup(0, 0)
    # Making the variable global
    global hardwar
    # Getting input from the user
    try:
        hardwar = numinput('Set the difficulty level', '''Choose the difficulty level:
            Easy: 1
            Medium: 2
            Hard: 3''', 2, 1, 3)
    except TypeError:
        exit()
    # Restoring the screen with the golden ratio
    setup(400, 600)
    # Entering the main game screen drawing function
    game_lood1()

# Function to start the initial screen
def start():
    global Cls
    global hosh
    hosh = False
    # Allowing changes to the variables and making them global
    global cfg
    global index
    # Creating variables for AI (to remember which squares the user clicked to avoid re-clicking)
    cfg = ["933",
           "y", "y", "y",
           "y", "y", "y",
           "y", "y", "y"]
    # 933 in two variables to ignore the 0th index
    index = [993,
             0, 0, 0,
             0, 0, 0,
             0, 0, 0]
    # Asking the user for the number of players
    try:
        Cls = numinput("                      How many players?", """Single-player or two-player?
                Single-player: 1 
                Two-player: 2""", 1, 1, 2)
    except TypeError:
        exit()

    # Restoring the screen with the golden ratio
    setup(400, 600)
    # Function to determine if the user clicked on start or exit on the initial screen
    def ifelses(x, y):
        xt = int(x)
        yt = int(y)
        # Determining which button was pressed
        # For entering
        if (-120 < xt < 130) and (-170 < yt < -110):
            if Cls == 1:
                starthard1()
            if Cls == 2:
                game_lood1()
        # For exiting
        elif (-120 < xt < 130) and (-235 < yt < -175):
            exit()

    xd = [60, 60]
    yd = [250, 250]
    c = ["Yellow", "LawnGreen"]
    xg = [-120, -120]
    yg = [-235, -170]
    # Drawing the buttons
    for i in range(2):
        # Filling the button with color
        fillcolor(c[i])
        # Moving to the corner of the button
        goto(xg[i], yg[i])
        begin_fill()
        # Drawing the button (with dimensions based on the golden ratio = 1.618)
        sharp(xd[i], yd[i])
        end_fill()

    # Setting the color to black to write text on the buttons
    color("black")
    bgcolor("Aqua")
    goto(-80, -155)
    write("Start game", font=("Algerian", 18))
    fd(150)
    lt(-90)
    fd(3)
    lt(-90)
    write(" XO", font=("MISTRAL", 18))
    goto(-80, -220)
    write("Exit the Game", font=("Algerian", 18))
    goto(-110, -30)
    color("Fuchsia")
    # Writing the welcome message
    write("""
          
  welcome
     to
  Game 
     XO""", font=("MISTRAL", 50), )

    # Command to get a click on the user's laptop screen
    onscreenclick(ifelses)

    def start_game_with_key():
        if Cls == 1:
            starthard1()
        if Cls == 2:
            game_lood1()

    listen()
    onkeypress(start_game_with_key, 'p')
    onkeypress(start_game_with_key, 'Return')
    onkeypress(exit, 'e')
    onkeypress(exit, 'Escape')

# Function to draw the 3x3 grid of the game
def game_lood1():
    # Restoring the screen
    setup(0.5, 0.9)
    # Main settings for speed, color, and lifting the pen
    reset()
    color("BlueViolet")
    up()
    home()
    ht()
    speed(0.1)
    bgcolor("Fuchsia")
    # Moving to the corner of the grid and drawing the main square (border)
    goto(320, 280)
    setheading(270)
    down()
    pensize(20)
    fd(550)
    setheading(180)
    fd(650)
    setheading(90)
    fd(550)
    setheading(0)
    fd(650)
    # Drawing the inner squares
    up()
    goto(100, 100)
    down()
    sharp(180, 220)
    setheading(270)
    sharp(220, 185)
    setheading(270)
    fd(185)
    sharp(220, 185)
    setheading(180)
    fd(430)
    setheading(90)
    fd(185)
    setheading(0)
    fd(430)
    back(215)
    setheading(90)
    fd(180)
    back(550)
    # Restart button
    up()
    goto(-235, -335)
    down()
    pen(pensize=5)
    color("Yellow")
    begin_fill()
    sharp(97, 45)
    end_fill()
    up()
    setheading(0)
    color("red")
    goto(-328, -327)
    write("RESTART", ("Algerian", 16))
    # Executing the function to get clicks and return output to the user
    onclic()

# Variable for player turns
nobat = 0
# Variable for AI to not work if there is a winner or loser
hosh = True
# Another function for user clicks during the game (almost the entire game is summarized here)
def onclic():
    # Making the variable global
    global hosh
    # Bringing the variable for AI
    global index
    # Bringing the variable for turns and game difficulty taken from the user in the two-player section
    global nobat
    global hardwar
    global Cls
    # Commands to determine turns based on whether the game is single-player or two-player
    if Cls == 1:
        # If the user selects difficulty 1 or 2, it doesn't matter
        # But if the difficulty is 3, the bot goes first
        if hardwar == 1 or hardwar == 2:
            nobat = 0
    # But if the game is two-player
    if Cls == 2:
        # The turn doesn't matter, so it's the first player's turn
        nobat = 0

    # Drawing the turn
    goto(-300, 300)
    down()
    color("Fuchsia")
    fillcolor('Fuchsia')
    begin_fill()
    sharp(30, 110)
    end_fill()
    up()
    color('white')
    if nobat == 0:
        write("nobat  X", ("Algerian", 18))
    elif nobat == 1:
        write("nobat  O", ("Algerian", 18))
    # Variable for AI to not work if there is a winner or loser
    hosh = True
    # Function to
    # Draw X or O based on the turn
    # And calculate the user or bot's win or loss or a draw
    def draw_XO(x, y, nom):
        # Making the variable global
        global hosh
        # Bringing the variable for turns in a local function
        global nobat
        # Allowing changes to the text and numerical variables for filled or empty squares
        global cfg
        global index
        # Lifting the pen to avoid drawing while moving
        up()
        # Moving to the coordinates of the clicked square
        goto(x, y)
        # Calculating the turn
        # To draw X or O in the game
        if nobat == 0:
            color("black")
            write("X", font=("BLACKADDER ITC", 90))
            # Changing the empty square to X to calculate win or loss
            cfg[nom] = "X"
            # Changing the turn
            nobat += 1

        elif nobat == 1:
            color("white")
            write("O", font=("BLACKADDER ITC", 90))
            # Changing the empty square to O to calculate win or loss
            cfg[nom] = "O"
            # Changing the turn
            nobat -= 1
        # Drawing the turn
        goto(-300, 300)
        down()
        color("Fuchsia")
        fillcolor('Fuchsia')
        begin_fill()
        sharp(30, 110)
        end_fill()
        up()
        color('white')
        if nobat == 0 :
            write("nobat  X",("Algerian",18))
        elif nobat == 1 :
            write("nobat  O",("Algerian",18))
        """
            The code you see below
            is to declare the game over if 3 squares are filled and those three squares are in horizontal, vertical and diagonal
            positions
            Show the winner's name
            The user name is either X or O
        """
        # Below is a loop to try both X and O states
        n = ["X","O"]
        for i in range(2):
            if(((cfg[1] == n[i] and cfg[2] == n[i] and cfg[3] == n[i]) or
                (cfg[4] == n[i] and cfg[5] == n[i] and cfg[6] == n[i]) or
                (cfg[7] == n[i] and cfg[8] == n[i] and cfg[9] == n[i]))or
                (cfg[1] == n[i] and cfg[4] == n[i] and cfg[7] == n[i]) or
                (cfg[2] == n[i] and cfg[5] == n[i] and cfg[8] == n[i]) or
                (cfg[3] == n[i] and cfg[6] == n[i] and cfg[9] == n[i]) or
                ((cfg[1] == n[i] and cfg[5] == n[i] and cfg[9] == n[i]) or
                (cfg[7] == n[i] and cfg[5] == n[i] and cfg[3] == n[i]))):
                # Change the variable to make the robot not work
                hosh = False
                # Go to the coordinates of the victory write and draw a square around it
                # Delete the turn
                goto(-300,300)
                down()
                color("PaleGreen")
                fillcolor('PaleGreen')
                begin_fill()
                sharp(30,110)
                end_fill()
                up()
                # Draw the winner's name
                bgcolor("PaleGreen")
                color("red")
                goto(-80,-350)
                write(str(n[i])+" win",font=("BLACKADDER ITC",40))
                heading()
                down()
                pen(pensize=2)
                setheading(0)
                goto(-87,-337)
                sharp(55,140)
                up()
                # A function to clear the page and start over
                def mt(x,y):
                    reset()
                    speed(0.1)
                    ht()
                    up()
                    # Go to the game home page
                    game_lood1()

                # Clears the screen and initial properties or states
                # Same as speed, hiding and picking up the pen
                onscreenclick(mt)
                # Clears variables for AI (remembering which cells the user clicked so that they don't click again)
                cfg = ["933",
                "y","y","y",
                "y","y","y",
                "y","y","y"]
                # The number 933 is placed in two variables to avoid counting the zeroth place.
                index = [993,
                0, 0, 0,
                0, 0, 0,
                0, 0, 0]

        # Now we want to see if the game is a draw?
        # If the index variable contains 0, it means that there is still an empty square.
        if index.count(0) == 0 :
            # Change the variable to stop the robot from working
            hosh = False
            # # Delete turn
            goto(-300,300)
            down()
            color("Gray")
            fillcolor('Gray')
            begin_fill()
            sharp(30,110)
            end_fill()
            up()
            # If all cells are numbers other than 0, this command is entered
            # Goes to the coordinates of the victory writing and draws a square around it
            goto(-87,-337)
            heading()
            down()
            color("red")
            pen(pensize=2)
            setheading(0)
            # Draw a square with the golden ratio
            sharp(55,140)
            up()
            goto(-85,-345)
            # and writes the game as a draw
            bgcolor("Gray")
            write("X = O",font=("",40))
            # A function to clear the page and start over
            def mt(x,y):
                reset()
                speed(0.1)
                ht()
                up()
                # Go to the game's home screen
                game_lood1()

            # Clears the screen and returns to the initial settings
            # Same as speed, hiding, and picking up the pen
            onscreenclick(mt)
            # Clears variables for the AI ​​(remembering which cells the user clicked so that they don't click again)
            cfg = ["933",
            "y","y","y",
            "y","y","y",
            "y","y","y"]
            # 933 in two variables for not counting the zeroth place
            index = [993,
            0, 0, 0,
            0, 0, 0,
            0, 0, 0]


    # If it was a solo player and the user had chosen hard mode, it would issue the following commands
    if Cls == 1 and  hardwar == 3 and hosh == True:
        # This command is to prevent the user from clicking
        onscreenclick(None)
        # First and last of all squares
        gx = [993,-260,-50,170,-260,-50,170,-260,-50,170]
        gy = [993,120,120,120,-60,-60,-60,-240,-240,-240]
        # Fill in the square number clicked by the robot
        # This is done for the game's AI so that the code can understand that the square is full
        index[5] = 1
        # Draw that square based on the turn
        # Go to a coordinate and draw X or O
        draw_XO(gx[5],gy[5],5)


    """
    Below you see a function
    which is supposed to receive the x,y coordinates of the user's mouse click
    and check it
    so that the program's AI can understand
    which square the user clicked
    and get the number of that square from
    the index variable and if it is empty
    using the above function
    in that field
    based on the turn X or O clicked on the square
    """
    # Function for when the user clicks on the page
    def cloc (x,y):
        # Make the variable whether the squares are empty or not public
        global index
        global hosh
        global hardwar

        up()

        hosh = False
        # Above each command, the number of that square is written in the index variable.

        # index 1
        if -320 < x < -125  and 110  < y < 280 :
            # If the user clicks the first square and it is empty
            if index[1] != 1 :
                # In the index variable, the number of square 1 is set to 1 so that the code's 
                # artificial intelligence knows that the square is empty
                index[1] = 1
                hosh = True
                # And using the draw function, it draws the user's name based on the turn
                draw_XO(-260,120,1)

        # index 2
        elif -105 < x < 90 and 115 < y < 270 :
            if index[2] != 1 :
                index[2] = 1
                hosh = True
                draw_XO(-50,120,2)

        # index 3
        elif 110 < x < 305 and 115 < y < 270 :
            if index[3] != 1 :
                index[3] = 1
                hosh = True
                draw_XO(170,120,3)

        # index 4
        elif -320 < x < -125 and -75 < y < 90 :
            if index[4] != 1 :
                index[4] = 1
                hosh = True
                draw_XO(-260,-60,4)

        # index 5
        elif -105 < x < 90 and -75 < y < 90 :
            if index[5] != 1 :
                index[5] = 1
                hosh = True
                draw_XO(-50,-60,5)

        # index 6
        elif 110 < x < 305 and -75 < y < 90 :
            if index[6] != 1 :
                index[6] = 1
                hosh = True
                draw_XO(170,-60,6)

        # index 7
        elif -320 < x < -125 and -270 < y < -95 :
            if index[7] != 1 :
                index[7] = 1
                hosh = True
                draw_XO(-260,-240,7)

        # index 8
        elif -105 < x < 90 and -260 < y < -95 :
            if index[8] != 1 :
                index[8] = 1
                hosh = True
                draw_XO(-50,-240,8)

        # index 9
        elif 110 < x < 305 and -260 < y < -95 :
            if index[9] != 1 :
                index[9] = 1
                hosh = True
                draw_XO(170,-240,9)

        # If the user clicks on the option again
        elif -335 < x < -235 and -335 < y < -290 :
        # Clean up variables for the AI ​​(remembering which cells the user clicked so that they don't click again)
            cfg = ["933",
            "y","y","y",
            "y","y","y",
            "y","y","y"]
            #933 in two variables for not counting the zeroth place
            index = [993,
            0, 0, 0,
            0, 0, 0,
            0, 0, 0]
            reset()
            speed(0.1)
            ht()
            up()
            # Go to the game home page
            game_lood1()

        # In this short we say that if it was the robot's turn, the robot should choose the best mode and click
        # This part is for hard and medium
        if Cls == 1 and hosh == True and hardwar != 1 :
            def cloc_boot():
                global cfg
                global index
                # Finding empty houses
                dnd = []
                for i in range(len(index)):
                    if index[i] == 0 :
                        dnd.append(i)
                # First and last coordinates of all squares
                gx = [993,-260,-50,170,-260,-50,170,-260,-50,170]
                gy = [993,120,120,120,-60,-60,-60,-240,-240,-240]
                # This is to prevent the user from clicking
                onscreenclick(None)
                # Choose the best home
                botwin = Help_Bot(cfg,"X","D")
                botlos = Help_Bot(cfg,"X","S")
                if botwin == [0] :
                    if botlos == [0] :
                        while True :
                            m = (dnd[randint(0,(len(dnd)-1))])
                            if index[m] == 0 :
                                # Change the square number to 1 to know that the square is filled
                                index[m] = 1
                                # Draw that square in turn
                                draw_XO(gx[m],gy[m],m)
                                break

                    elif len(botlos) == 1 and botlos != [0] :
                        # Change the square number to 1 to know that the square is filled
                        index[botlos[0]] = 1
                        # Draw that square in turn
                        draw_XO(gx[botlos[0]],gy[botlos[0]],botlos[0])
                    elif len(botlos) > 1 :
                        a = dnd
                        b = (botlos[randint(0,(len(botlos)-1))])
                        if a.count(b) <= 1 :
                            if index[b] == 0 :
                                # Change the square number to 1 to know that the square is filled
                                index[b] = 1
                                # Draw that square in turn
                                draw_XO(gx[b],gy[b],b)
                            elif index[b+1] == 0 :
                                # Change the square number to 1 to know that the square is filled
                                index[b] = 1
                                # Draw that square in turn
                                draw_XO(gx[b],gy[b],b)
                        elif index[b] == 0 :
                            # Change the square number to 1 to know that the square is filled
                            index[b] = 1
                            # Draw that square in turn
                            draw_XO(gx[b],gy[b],b)
                elif len(botwin) == 1 and botwin != [0] :
                    # Change the square number to 1 to know that the square is filled
                    index[botwin[0]] = 1
                    # Draw that square in turn
                    draw_XO(gx[botwin[0]],gy[botwin[0]],botwin[0])
                elif len(botwin) > 1 :
                    a = dnd
                    b = (botwin[randint(0,(len(botwin)-1))])
                    if a.count(b) <= 1 :
                        if index[b] == 0 :
                            # Change the square number to 1 to know that the square is filled
                            index[b] = 1
                            # Draw that square in turn
                            draw_XO(gx[b],gy[b],b)
                        elif index[b+1] == 0 :
                            # Change the square number to 1 to know that the square is filled
                            index[b] = 1
                            # Draw that square in turn
                            draw_XO(gx[b],gy[b],b)
                    elif index[b] == 0 :
                            # Change the square number to 1 to know that the square is filled
                            index[b] = 1
                            ## Draw that square in turn
                            draw_XO(gx[b],gy[b],b)
                # The following command is the command that will go to the cloc function when the user clicks on the screen
                onscreenclick(cloc)
            cloc_boot()

        elif Cls == 1 and hosh == True and hardwar == 1 :
            # Finding empty houses
                dnd = []
                for i in range(len(index)):
                    if index[i] == 0 :
                        dnd.append(i)
                # First and last coordinates of all squares
                gx = [993,-260,-50,170,-260,-50,170,-260,-50,170]
                gy = [993,120,120,120,-60,-60,-60,-240,-240,-240]
                # This command is to prevent the user from clicking
                onscreenclick(None)
                b = [dnd[randint(0,(len(dnd)-1))]]
                # Change the square number to 1 to know that the square is filled
                index[b[0]] = 1
                # Draw that square in turn
                draw_XO(gx[b[0]],gy[b[0]],b[0])
                # The following command is the command that will go to the cloc function when the user clicks on the screen
                onscreenclick(cloc)


    # The following command is the command that will go to the cloc function when the user clicks on the screen
    onscreenclick(cloc)

# This is the command to start the game
start()
# It receives an input This input is to keep the page open
mainloop()
# End
