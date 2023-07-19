import pandas
import turtle

data = pandas.read_csv("50_states.csv")
turtle.Screen().title("District guessing game")
bg_image = "image.gif"
turtle.Screen().addshape(bg_image)
turtle.shape(bg_image)


states = data["state"].tolist()
score = 0
guessed = []
game_repeat = True
while game_repeat:

    user_data = turtle.Screen().textinput(title=f"Score:{score}/50", prompt="Enter a district name: ").title()

    if user_data in states:

        if user_data not in guessed:
            score += 1
        guessed.append(user_data)
        myturtle = turtle.Turtle()
        myturtle.hideturtle()
        myturtle.penup()

        current_district = data[data.state == user_data]
        myturtle.goto(int(current_district.x), int(current_district.y))
        myturtle.write(user_data)

    if score == 50:
        game_repeat = False


turtle.Screen() .exitonclick()


