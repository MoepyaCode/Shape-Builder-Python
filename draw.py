import math

# Space and Asterisk (Drawing the shape) will be used to form the shapes.
# Space will also be used for additional spacing too.
asterisk = '*' 
space = ' '


# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():

    # Create shape varible and initialize as an empty string to force loop to start.
    # Create options array that will have the available shapes.
    shape = ''
    options = ['pyramid', 'triangle', 'square', 'diamond', 'rhombus', 'trapezium']

    # write a While loop that checks if the user input, 'shape', is in the options.
    # If not in the options it prompts the user again until condition is met.
    while shape not in options:
        shape = input('Shape?: ').lower()

    # Returns shape once While loop condition is false.
    return shape

# TODO: Step 1 - get height (it must be int!)
def get_height():
    
    # Create height varible and initialize as 0 to force loop to start since condition is true.
    height = 0

    # Use error handling to make program not break after entering foreign character.
    # Such as a letter. i.e 't'
    while height <= 1 or height > 80:
        try:
            height = int(input('Height?: '))
        except ValueError as msg:
            continue    # Tell the program to continue prompting the user.
        else:
            break   # Tells the program to stop the loop once condtion is False.
        
    return height


# TODO: Step 2
def draw_pyramid(height, outline):

    # The varibles below are used as counts for the asterisks and the space.
    # The pyramid varible is created outside the loop in order to not have a non-declaration error.
    asteriskCount = 1   
    spaceSolidCount = 1
    spaceOutlineCount = 0
    pyramid = ''

    # The IF/ELSE conditon checks if the user wants the outline or solid print of shape.
    if outline == False: 

        for i in range(height):

            # We have to use spaces that will automatically push asterisk to the right.
            # This will then for a pyramid shape.
            pyramid += ((space * (height - spaceSolidCount)) + (asterisk * asteriskCount))
            pyramid += asterisk * (asteriskCount - 1)

            # IF/ELSE statement include the escape until i == height.
            if i < (height - 1):
                pyramid += '\n'
            
            else:
                pyramid += ''

            # We increment the varibles that have been created above.
            spaceSolidCount = spaceSolidCount + 1
            asteriskCount = asteriskCount + 1
        
    elif outline == True:

        for i in range(height):
            
            pyramid += (space * (height - (spaceOutlineCount + 1)))
            pyramid += (asterisk)

            # Says that the spaces within the shape should start after the first loop.
            # And should end before the last loop.
            # Furthermore, says that asterisks should be printed at the end of each clustered space print.
            if spaceOutlineCount > 0 and spaceOutlineCount < (height - 1):

                pyramid += space * spaceOutlineCount
                pyramid += (space * (spaceOutlineCount - 1)) + asterisk

            else:
                # spaceOuline starts from 0
                pyramid += asterisk * spaceOutlineCount # Prints the left side of the Pyramid
                pyramid += (asterisk * spaceOutlineCount) # Prints the right bottom side of the Pyramid
            
            # i starts from 0 when counting.
            # The last loop number is height - 1, thus we say height - 2 in order to avoid the escape.
            if i <= (height - 2):
                pyramid += '\n'
            
            else:
                pyramid += ''

            # We increment the varibles that have been created above.
            asteriskCount = asteriskCount + 1
            spaceOutlineCount = spaceOutlineCount + 1
        
    print(pyramid)


# TODO: Step 3
def draw_square(height, outline):
    
    # We create a square varible that we'll build on to create a square.
    square = ''
    width = height # According to instructions.
    
    # The IF/ELSE conditon checks if the user wants the outline or solid print of shape.
    if outline == False:

        # This is the code for the solid square
        for i in range(height):
            square += asterisk * width

            if i == (height - 1):
                square += ''

            else:
                square += '\n' 
        
    elif outline == True:
        
        # This is the code for the outline square
        for i in range(1):

            for j in range(1):
                square += asterisk * width
                square += '\n'
                
            for k in range(1,height - 1):
                square += asterisk + (space * (height - 2)) + asterisk
                square += '\n'
                
            for f in range(1):
                square += asterisk * width  
        
    print(square)


# TODO: Step 4
def draw_triangle(height, outline):

    # The varibles below are used as counts for the asterisks and the space.
    # The triangle varible is created outside the loop in order to not have a non-declaration error.
    asteriskCount = 1
    spaceCount = 0
    triangle = ''

    if outline == False:

        for i in range(height):
            triangle += asterisk * asteriskCount
            
            # If i is in the last loop we then avoid the escape ('\n').
            if i == (height - 1):
                triangle += ''

            else:
                triangle += '\n'    
            
            asteriskCount = asteriskCount + 1

    else:

        for i in range(height):

            # i starts from 0 when counting.
            # The last loop number is height - 1, thus we say while its less than height - 1.
            if spaceCount < (height - 1):

                triangle += asterisk + (space * (spaceCount - 1))

                if spaceCount > 0:
                    triangle += asterisk

                triangle += '\n'
                spaceCount = spaceCount + 1
            
            else:
                triangle += asterisk * height   # This is to get the base line.

    print(triangle)


def draw_diamond(height, outline):

    # The varibles below are used as counts for the asterisks and the space.
    # The diamond varible is created outside the loop in order to not have a non-declaration error.
    # halfHeight allows us to work on the two parts of the diamond seperately.
    asteriskCount1 = 1
    asteriskCount2 = 1
    spaceCount1 = 1
    spaceCount2 = 1
    diamond = ''
    halfHeight = int(math.ceil(height/2))

    # The IF/ELSE conditon checks if the user wants the outline or solid print of shape.
    if outline == False:

        for i in range(1):

            # Builds top part of the solid diamond.
            for j in range(halfHeight):
                diamond += (space * (halfHeight - spaceCount1))
                diamond += (asterisk * asteriskCount1)
                diamond += (asterisk * (asteriskCount1 - 1)) # comment this out in order to get the logic behind it.
                diamond += '\n'
                spaceCount1 = spaceCount1 + 1
                asteriskCount1 = asteriskCount1 + 1

            # Builds bottom part of the solid diamond.
            for k in range(halfHeight - 1):
                diamond += (space *spaceCount2) + (asterisk * (halfHeight - asteriskCount2))
                diamond += asterisk * (halfHeight - (asteriskCount2 + 1))

                if k <= (halfHeight - 3):
                    diamond += '\n'
                
                else:
                    diamond += ''

                spaceCount2 = spaceCount2 + 1
                asteriskCount2 = asteriskCount2 + 1
            
    else:

        for i in range(1):
            
            # Builds top part of the outline diamond.
            for j in range(halfHeight):
                diamond += (space * (halfHeight - spaceCount1))
                diamond += (asterisk + (space * (spaceCount1 - 1)))
                
                if j >= 1:
                    diamond += (space * (spaceCount1 - 2) + asterisk) 

                diamond += '\n'
                spaceCount1 = spaceCount1 + 1
                asteriskCount1 = asteriskCount1 + 1

            # Builds bottom part of the outline diamond.
            for k in range(halfHeight - 1):
                
                if k != (halfHeight - 1):
                    diamond += (space *spaceCount2) + (asterisk)
                    diamond += (space * (halfHeight - (spaceCount2 + 1)))

                # Works on the bottom right of the diamond.
                # halfHeight - 2 is the second last loop for halfHeight.
                if k == (halfHeight - 2):
                    diamond += ''
                else:
                    diamond += (space * (halfHeight - (spaceCount2 + 2)))

                if k == (halfHeight - 2):
                    diamond += ''
                else:
                    diamond += asterisk

                if k < (halfHeight - 2):
                    diamond += '\n'
                else:
                    diamond += ''

                spaceCount2 = spaceCount2 + 1
                asteriskCount2 = asteriskCount2 + 1

    return print(diamond)


def draw_rhombus(height, outline):

    # The varibles below are used as counts for the asterisks and the space.
    # The rhombus varible is created outside the loop in order to not have a non-declaration error.
    # Rhombus is a square that is skewed, thus width is equal to height.
    asteriskCount = 1 
    spaceCount = 1
    rhombus = ''
    width = height
    
    # The IF/ELSE conditon checks if the user wants the outline or solid print of shape.
    if outline == False:
        
        for i in range(height):
            rhombus +=  (space * (spaceCount - 1)) + ((asterisk + space) * width)

            # i starts from 0 when counting.
            # The last loop number is height - 1, thus we say if i <= second last loop number (height - 2).
            if i <= (height - 2):
                rhombus += '\n'

            else:
                rhombus += ''
            
            spaceCount = spaceCount + 1
              
    else:
        
        # Loops once as inner loops print out the full shape.
        # Outer loop accomdates the inner loops.
        for i in range(1):
    
            for i in range(1):
                rhombus += ((asterisk + space) * width) 
                rhombus += '\n'

            for i in range(height - 2):
                rhombus += (space * spaceCount) + asterisk
                rhombus += (space * ((width * 2) - 3)) + asterisk
                rhombus += '\n'
                spaceCount = spaceCount + 1 
            
            for i in range(1):
                rhombus += space * (width - 1)
                rhombus += ((asterisk + space) * width) 
    
    return print(rhombus)


def draw_trapezium(height, outline): 

    # The varibles below are used as counts for the asterisks and the space.
    # The trapezium varible is created outside the loop in order to not have a non-declaration error.
    asteriskCount = 1 
    spaceCount = 1
    trapezium = ''

    # The IF/ELSE conditon checks if the user wants the outline or solid print of shape.
    if outline == False:
        
        for i in range(height):
            trapezium += (space * (height - spaceCount))
            trapezium += (asterisk * (height + asteriskCount))

            # i starts from 0 when counting.
            # The last loop number is height - 1, thus we say if i <= second last loop number (height - 2).
            if i <= (height - 2):
                trapezium += '\n'
            
            else:
                trapezium += ''
                
            asteriskCount = asteriskCount + 1
            spaceCount = spaceCount + 1
            
    else:
        
        for i in range(1):
            
            # The top part of the trapezium
            for j in range(1):
                trapezium += (space * (height - spaceCount))
                trapezium += (asterisk * ((height - 1) + asteriskCount))
                trapezium += '\n'
                asteriskCount = asteriskCount + 1
                spaceCount = spaceCount + 1

            # The middle part of the trapezium
            for k in range(height - 2):
                trapezium += (space * (height - spaceCount))
                trapezium += asterisk + (space * (height + (spaceCount - 3))) 
                trapezium += asterisk
                trapezium += '\n'
                asteriskCount = asteriskCount + 1
                spaceCount = spaceCount + 1

            # The bottom(base) part of the trapezium
            for f in range(1):
                trapezium += (space * (height - spaceCount))
                trapezium += (asterisk * ((height - 1) + asteriskCount))
                trapezium += ''
                asteriskCount = asteriskCount + 1
                spaceCount = spaceCount + 1

    return print(trapezium)


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):

    # conditonal staments that checks user input again each condition.
    # the first one that is met will be printed out by calling the draw_shape function.
    if shape == 'pyramid':
        draw_pyramid(height, outline)

    elif shape == 'square':
        draw_square(height, outline)

    elif shape == 'triangle':
        draw_triangle(height, outline)

    elif shape == 'diamond':
        draw_diamond(height, outline)

    elif shape == 'rhombus':
        draw_rhombus(height, outline)

    elif shape == 'trapezium':
        draw_trapezium(height, outline) 


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():

    # The outline varible is created outside the loop in order to not have a non-declaration error.
    outline = ''

    # While Loop checks if user input for outline is == True or False.
    # If True it returns the shapes outline.
    # If False it returns the solid shape.
    while outline != 'y' or outline != 'n' or outline != '':

        outline = input('Outline only?(y/N): ').lower()

        if outline == 'n' or outline == '':
            return False

        elif outline.lower() == 'y':
            return True
    
if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

