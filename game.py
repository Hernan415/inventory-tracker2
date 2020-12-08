import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
#Asks for what type of graphic they would like
shape = turtle.textinput("What shape would you like done?",
                         "Circle spiral or name spiral").lower()
#If circle spiral is coded this will be ran
if (shape == 'circle spiral'):
#Asks if the user would like to input colors
    work = turtle.textinput("Colors",
                            "Would you like to choose the colors? yes or no").lower()
#if choosen yes, then the user will input 6 colors of their choice
    if (work == 'yes'):
        t.penup()
        #input colors
        colorOne = turtle.textinput("Type a color" , "Type a color")
        colorTwo = turtle.textinput("Type a color" , "Type a color")
        colorThree = turtle.textinput("Type a color" , "Type a color")
        colorFour = turtle.textinput("Type a color" , "Type a color")
        colorFive = turtle.textinput("Type a color" , "Type a color")
        colorSix = turtle.textinput("Type a color" , "Type a color")
        sides = int(turtle.numinput("Number of sides",
            "How many sides in your spiral of spirals?(1-6)",3,1,6))
        colors = [ colorOne , colorTwo , colorThree , colorFour , colorFive,colorSix]
        #spiral loop
        for m in range(100):
            t.penup()
            t.forward(m*8)
            position = t.position()
            heading = t.heading()
             #rosette loop
            for n in range(6):
                t.pendown()
                t.pencolor(colors[n%sides])
                t.circle(m*3/5)
                t.left(360/6)
                t.width(m*6/91)
        #move to position
            t.setx(position[0])
            t.sety(position[1])
            t.setheading(heading)
            t.left(360/sides +2)
#If the user decided they did not want to input colors the code will be ran automatically excpet it would ask the user for how many rosettes they would like.
    elif (work=='no'):
        t.penup()
        #input variables
        sides = int(turtle.numinput("Number of sides",
            "How many sides in your spiral of spirals?(1-6)",3,1,6))
        colors = ["red" , "orange" , "yellow" , "green" , "blue" , "purple"]
        #spiral loop
        for m in range(100):
            t.penup()
            t.forward(m*8)
            position = t.position()
            heading = t.heading()
        #rosette loop
            for n in range(6):
                t.pendown()
                t.pencolor(colors[n%sides])
                t.circle(m*3/5)
                t.left(360/6)
                t.width(m*6/91)
        #move to position
            t.setx(position[0])
            t.sety(position[1])
            t.setheading(heading)
            t.left(360/sides +2)
#If the user chose name spiral this code will be ran
elif (shape == "name spiral"):
     worko = turtle.textinput("Colors" , "Would you like to choose the colors? yes or no").lower()
#if choosen yes, then the user will input 6 colors of their choice
     if (worko== 'yes'):
         t.penup()
         turtle.bgcolor("black")
         #input variables
         colorOne = turtle.textinput("Type a color" , "Type a color")
         colorTwo = turtle.textinput("Type a color" , "Type a color")
         colorThree = turtle.textinput("Type a color" , "Type a color")
         colorFour = turtle.textinput("Type a color" , "Type a color")
         colorFive = turtle.textinput("Type a color" , "Type a color")
         colorSix = turtle.textinput("Type a color" , "Type a color")
         colors = [ colorOne , colorTwo , colorThree , colorFour , colorFive,colorSix]
         family = []
         name = turtle.textinput("My family", "Enter a name, or just hit [ENTER] to end:")
#Will draw the name spiral
         while name != "":
             family.append(name)
             name = turtle.textinput("My family", "Enter a name, or just hit [ENTER] to end:")
         for x in range(100):
            t.pencolor(colors[x%len(family)])
            t.penup()
            t.forward(x*4)
            t.pendown()
            t.write(family[x%len(family)], font = ("Arial", int((x+4)/4), "bold") )
            t.left(360/len(family) + 2)
#If the user decided they did not want to input colors the code will be ran automatically excpet it would ask the user for how many rosettes they would like.
     elif (worko == 'no'):
         colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "brown", "gray", "pink"]
         family = []
         name = turtle.textinput("My family", "Enter a name, or just hit [ENTER] to end:")
         while name != "":
             family.append(name)
             name = turtle.textinput("My family", "Enter a name, or just hit [ENTER] to end:")
         for x in range(100):
             t.pencolor(colors[x%len(family)])
             t.penup()
             t.forward(x*4)
             t.pendown()
             t.write(family[x%len(family)], font = ("Arial", int((x+4)/4), "bold") )
             t.left(360/len(family) + 2)
