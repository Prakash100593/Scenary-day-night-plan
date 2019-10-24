
"""
This program takes the no of trees and if house needed as input from user
and accordingly plans for day or Night.

"""
import turtle as t
import math
import random

t.setworldcoordinates(-1000, -1000, 1000, 1000)
def DrawTrunk(height,spacebetween):

    """
    Draws Trunk.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) 100 units from the end of the previous object.
     At Start, it will be at (100,0) 100 relative units from the star.
     However this is reused for drawing trunks for different type pf trees
     Hence the relative Post conditon will be 100 pixels far from the previous
     object's post condition.

     Directions - Heading (east), up
    :return: None
    """


    t.up()
    t.forward(spacebetween)
    t.down()
    t.left(90)
    t.forward(height)
    t.up()
    t.backward(height)
    t.right(90)
def DrawTopTriangle(height,Sides):
    """
    Draws Top portion on the trunk for Pine Tree.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) 100 units far from the previose object.
    from the s heading (east), up
    :return: None
    """

    t.left(90)
    t.forward(height)
    t.left(90)
    t.down()
    t.forward(Sides/2)
    t.right(135)
    t.forward(Sides/(math.sqrt(2)))
    t.right(90)
    t.forward(Sides/(math.sqrt(2)))
    t.right(135)
    t.forward(Sides/2)
    t.left(90)
    t.up()
    t.forward(height)
    t.left(90)
    t.forward(Sides/2)
def DrawTopCircle(height,radius):
    """
    Draws Top portion on the trunk for Mapple Tree.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) 100 units far from the previose object.
    from the s heading (east), up
    :return: None
    """


    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(radius)
    t.left(90)
    t.forward(radius)
    t.down()
    t.circle(radius)
    t.up()
    t.backward(radius)
    t.left(180)
    t.forward(height)
    t.left(90)
def DrawTopSqare(height,Sides):
    """
    Draws Top portion on the trunk for Own(that is user defined) Tree.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) 100 units far from the previose object.
    from the s heading (east), up
    :return: None
    """

    t.left(90)
    t.forward(height)
    t.left(90)
    t.down()
    t.forward(Sides/2)
    t.right(90)
    t.forward(Sides)
    t.right(90)
    t.forward(Sides)
    t.right(90)
    t.forward(Sides)
    t.right(90)
    t.forward(Sides/2)
    t.left(90)
    t.up()
    t.forward(height)
    t.left(90)
    t.forward(Sides / 2)
def DrawHouseTop(Sides):
    """
    Draws Top portion of the house.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) 100 units far from the previose object.
    from the s heading (east), up
    :return: None
    """


    t.up()
    t.left(90)
    t.forward(Sides)
    t.left(90)
    t.forward(Sides)
    t.down()
    t.right(135)
    t.forward(Sides/math.sqrt(2))
    t.right(90)
    t.forward(Sides/math.sqrt(2))
    t.right(45)
    t.up()
    t.forward(Sides)
    t.left(90)
def DrawPineTree(spacebetween):
    """
    Draws Pine Tree.
    Calls DrawTrunk and DrawTopTriangle
    :return: height of the trunk
    """
    # Height varianle to be selected randomly within range of 50 to 200
    height = float(random.uniform(50, 200))
    Sides = height
    DrawTrunk(height, spacebetween)
    DrawTopTriangle(height, 80)
    return height
def DrawMappleTree(spacebetween):
    """
    Draws Mapple Tree.
    Calls DrawTrunk and DrawTopCircle
    :return: height of the trunk
    """
    # Height varianle to be selected randomly within range of 50 to 150

    height = float(random.uniform(50, 150))
    radius = height/2
    DrawTrunk(height, spacebetween)
    DrawTopCircle(height, 40)
    return height

def DrawOwnTree(spacebetween):
    """
    Draws Own(user defined) Tree.
    Calls DrawTrunk and DrawTopSquare
    :return: height of the trunk
    """
    # Height varianle to be selected randomly within range of 50 to 200
    #height = random.randint(50, 200)
    height = float(random.uniform(50, 200))
    Sides = height
    DrawTrunk(height, spacebetween)
    DrawTopSqare(height, 80)
    return height
def DrawHouse(houseHeight,spacebetween):
    """
    Draws House for the Night and Day based on parameter HouseHeight.
    Parameter Spacebetqween is to maintain consistent space betweem trunks and House walls.
    Calls DrawTrunk and DrawTopSquare
    :return: 4* House Height = Walls of the wood availaible for refurnishing.
    """


    DrawTrunk(houseHeight, spacebetween)
    Housebase =houseHeight
    DrawTrunk(houseHeight, Housebase)
    DrawHouseTop(houseHeight)
    t.up()
    t.forward(40)
    return (4*houseHeight)
def DrawStar(height):
    """
        Draws Star based on the maximum height.
        pre condition - (0,0)
        Post Condition - (0,0)
        At start it will be at 0,0, once the max heighted tree is found, the cursor will move
        respective pixels forward and will end at 0,0 again
        It places star on the top of the max hieght tree
        :return: None.
        """
    pp=0
    #position = 2*height + 70
    position = height + 80 + 70
    t.left(90)
    t.forward(position)
    t.left(60)
    t.down()
    t.forward(60)
    t.backward(60)
    t.right(30)
    t.forward(60)
    t.backward(60)
    t.right(60)
    t.forward(60)
    t.backward(60)
    t.right(30)
    t.forward(60)
    t.backward(60)
    t.right(60)
    t.forward(60)
    t.backward(60)
    t.right(30)
    t.forward(60)
    t.backward(60)
    t.right(60)
    t.forward(60)
    t.backward(60)
    t.right(30)
    t.forward(60)
    t.backward(60)
    t.up()
    t.left(60)
    t.forward(position)
    t.left(90)

def DrawSun(Height,spacebetween):
    """
        Draws Sun in the morning.
        pre condition- relative(0,0) respective to the house constructed
        Post condition - (Height of the House + 28radius of the sun)
        :return: None.
    """
    t.up()
    t.forward(spacebetween)
    t.left(90)
    t.forward(2.5*Height)
    t.down()
    t.circle(Height/3)
    t.up()
    t.backward(2.5*Height)
    t.right(90)


def PlanNight(NoofTrees, NeedHouse, spacebetween):
    """
        Plans objects to be included as per user input.
        :return: Total Wodd available from all objects that are present in night to
            build a house for day
    """



    """
         Global vairables declared to compute max height and total wood availainle for house.
         
         - Two Lists height[],position[] defined to store the height and posoition of the tree
         - total initlaized to capture the quantity of lumber of woods availaible for house creation
            houseHeight - fixed to 100 pixels for the house to be drawn at night
    
    """
    houseHeight = 100
    total = 0;
    trunk = 0;
    counter=0
    difference=0
    maxHeight=0
    noofobjects=3
    height=[]
    position=[]
    index=0;
    initialposition=spacebetween
    indexcheck = 0
    finalposition = 0
    maximum = 0

    """
    if user does not include a House in night plan,
    the function will call randomly the trees to be included
    and will compute the hieght and Total wood availaible
    """

    if NeedHouse == 'n':
        noofobjects = 0
        for x in range(1, NoofTrees+1):
           noofobjects = noofobjects + 1
           trunk = random.choice([DrawMappleTree, DrawPineTree, DrawOwnTree])(spacebetween)
           height.insert(index, trunk)
           position.insert(index, initialposition)
           index = index + 1
           initialposition = initialposition + 100
           if x==1:
            maxHeight = trunk
           else:
               if trunk > maxHeight:
                maxHeight=trunk

           total = total + trunk
        t.setx(0)
        t.sety(0)
        for i, value in enumerate(height):
            if value > maximum:
                maximum = value
                indexcheck = i
        finalposition = position[indexcheck]
        finalheight= height[indexcheck]

        #print(finalposition)

        t.forward(finalposition)
        DrawStar(finalheight)
        t.setx(0)
        t.sety(0)

    else:
        """
        if user includes a House in night plan,
        the function will first include a tree at the start and end, as
        House needs to be in between at least two trees
        Secondly it will position house and the remaining trees as per random input
        
        It will return the total wood availaible for construction of House
        and will also store the height of each tree and its position in
        Height and Position lists
        """

        trunk = random.choice([DrawMappleTree, DrawPineTree, DrawOwnTree])(spacebetween)

        total = total + trunk
        maxHeight = trunk
        height.insert(index, trunk)
        position.insert(index, initialposition)
        index = index + 1
        initialposition = initialposition +100

        treeAtStart = random.randint(0, (NoofTrees-2))

        for x in range(1,treeAtStart):
            counter+1
            noofobjects=noofobjects+1
            #trunk = DrawPineTree(spacebetween)
            trunk = random.choice([DrawMappleTree, DrawPineTree, DrawOwnTree])(spacebetween)
            height.insert(index, trunk)
            position.insert(index, initialposition)
            index = index + 1
            initialposition = initialposition + 100

            if trunk > maxHeight:
               maxHeight = trunk
            total = total + trunk

        #print("Tree"+str(trunk))
           #print("Tree"+str(maxHeight))
        total = total + DrawHouse(houseHeight, spacebetween)
        if houseHeight > maxHeight:
            maxHeight = houseHeight
        initialposition = initialposition + 200

        if (counter < NoofTrees-2):
            difference = (NoofTrees-2)-counter

        for x in range(1,difference):
            #trunk = DrawPineTree(spacebetween)
            trunk = random.choice([DrawMappleTree, DrawPineTree, DrawOwnTree])(spacebetween)
            height.insert(index, trunk)
            position.insert(index, initialposition)
            index = index + 1
            initialposition = initialposition + 100

            if trunk > maxHeight:
                maxHeight = trunk
                total = total + trunk


        trunk = random.choice([DrawMappleTree, DrawPineTree, DrawOwnTree])(spacebetween)
        if trunk > maxHeight:
            maxHeight = trunk
        #print("Tree" + str(trunk))
        #print("Tree" + str(maxHeight))
        total = total + trunk
        height.insert(index,trunk)
        position.insert(index,initialposition)
        index = index + 1
        initialposition = initialposition + 100

        """
            The below lines will set the turtle cursor to 0,0.
            will search for the index of the maximum value 
            from list height(which stores the hieght of each tree constructed)
            it will fetch the position from the position list based on index
            obtained from above
            once it gets the position, it will compute the final position 
            for the star and will move the cursor accordingly to draw star
            
            After the star completion it will move turtle cursor back to 0,0
        """

        t.setx(0)
        t.sety(0)
        for i, value in enumerate(height):
            if value > maximum:
                maximum = value
                indexcheck = i
        finalposition = position[indexcheck]
        finalheight= height[indexcheck]


        t.forward(finalposition)
        DrawStar(finalheight)
        t.setx(0)
        t.sety(0)

        #print("Star" + str(maxHeight))
    return total


def main():
    """
    All the Top portion (i.e above the trunk) are kept to be 80 pixels
    Hence 40 pixels from the trunk

    Spacebetween is kept to 60, to meet the criteria of distance being
    100 between two trunks

    :return: None
    """
    spacebetween = 60
    Totalwood =0.00
    NoofTrees = int(input("How many tress in your forest ?"))

    # NoofTrees = int(getInput())
    if NoofTrees >= 1:
        NeedHouse=input("Is there a house in the forest (y/n) ?")
        Totalwood = Totalwood + float(PlanNight(NoofTrees, NeedHouse, spacebetween))
    else:
        input("Enter value greater than 0")

    input("Night is done, press enter for day")
    t.clear()

    t.setworldcoordinates(-1000, -1000, 1000, 1000)


    HouseSide = Totalwood/(2+math.sqrt(2))
    print()
    print("We have "+str(Totalwood)+" units of lumber for building")
    print("We have build a house with walls "+str(HouseSide)+" tall")


    """
    Below lines of code will draw the house using the same method of drawHouse
    that was used to create house at night.
    The parametert Houseside, will be calculated based on the Total wood availaible
    Respective to House, it will draw a sun (Which might touch the window borders
    in case of larger length)
    """
    t.reset()
    DrawHouse(HouseSide, spacebetween)
    DrawSun(HouseSide, spacebetween)
    print()

    input("Day is done, house is built, press enter to quit")

    t.mainloop()

if __name__ == '__main__':
        main()
