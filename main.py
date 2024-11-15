# Turtle only works with GIF image format.
import turtle
import pandas

screen = turtle.Screen()
screen.title("Australian States Game")
# Load a image as the turtle shape
## variable that holds the path to the image.
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(height=716, width=796)
turtle.shape(image)

# >>> THIS FUNCTION WILL GIVE US THE X AND Y COORDINATES WHEN CLICKING ON THE SCREEN <<<

## We use this to locate the states 

# def get_mouse_click_coor(x, y):
#     print(int(x), int(y))
    
# turtle.onscreenclick(get_mouse_click_coor)
# '''this will keep our screen open even after the code finish runing 
#     avoiding the flash and deseaper of the screen.
#     It works in a similar way to screen.exitonclick() '''
# turtle.mainloop()

data = pandas.read_csv("Australian_States.csv")
# here we are selecting the column 'state' of the csv file
all_states = data.state.to_list()
guessed_states = []

## Keep count of guessed states 
while len(guessed_states) < 7:
    # Window setup
    ''' We use the length of guessed_states varaible to keep the count of the guessed sates  '''
    ''' Avoid getting the wrong answer when the first letter of the state is not uppercase:
        .title() will capitalize the words of the string '''
    answer_state = screen.textinput(title=f"{len(guessed_states)}/7 States Correct", prompt="What's another state name?").title()
    print(answer_state)

    # EXIT THE GAME
    ''' We will exit the game with a secret word
        REMEMBER, the .title() will capitalize the answer'''
    if answer_state == "Exit":
        # CREATE A FILE TO SAVE THE ANSWERS AND COMPARE WITH THE RIGHT ANSWERS
        ## This will give us a list of the missing states 
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        # print(missing_states)
        ''' Save the list of the missing states in a column in a CSV file'''
        new_data = pandas.DataFrame(missing_states)
        ''' This is saving the data in a new file '''
        new_data.to_csv("states_to_learn.csv")
        break
    #If ansewer_state is one of the states in all the states in the 50_states.csv 
    ''' We can use the 'in' word only if we convert the state into a list <-- data.state.to_list() '''
    if answer_state in all_states:
        # every time the user guesses a state correctly, then we're going to add this answer_state to the guessed state.
        guessed_states.append(answer_state)
        #If we got it right:
        ## We Create a turtle to write the name of the state at the state's x and y coordinates
        pointer = turtle.Turtle()
        pointer.hideturtle()
        pointer.penup()
        #This is going to pull out the row where the state is equal to the answer_state.
        state_data = data[data.state == answer_state]
        #Here we are sending the pointer to the x and y coordinates of the typed state
        ''' In state_data.x and state_data.y the x and y are the names of the columns in the csv file. '''
        pointer.goto(state_data.x.item(), state_data.y.item())
        pointer.write(answer_state, font=("arial", 12, "normal"))



screen.exitonclick()