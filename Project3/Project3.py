# Project3.py

import scanner
import parser
from collections import deque
import tkinter
from tkinter import messagebox
import turtle

# This code is to hide the main tkinter window
root = tkinter.Tk()
root.withdraw()

class Node:
    def __init__(self, data): 
        self.data = data

class Project3:
    def createTree(structures):     # create syntax tree from the productions given from the parser
        STstack = []
        for (x,y,z) in structures:
            # x is the LHS of the grammar rule
            # y is the RHS of the grammar rule
            # z is the grammar rule number
            if z == 0:
                pass
            if z == 1:
                L = STstack.pop()
                node = Node(y[0:4] + [L] + [y[-1]])
                STstack.append(node)
            if z == 2:
                pass    # do nothing
            if z == 3:      # join two nodes into a seq node
                S = STstack.pop()
                L = STstack.pop()
                node = Node(['seq'] + [L] + [S])
                STstack.append(node)
            if z == 4:
                D = STstack.pop()
                node = Node(y[0:4] + [D])
                STstack.append(node)
            if z == 5:
                D = STstack.pop()
                node = Node(y[0:4] + [D])
                STstack.append(node)
            if z == 6:
                node = Node(y)
                STstack.append(node)
            if z == 7:
                node = Node(y + ['1'])
                STstack.append(node)
            if z == 8:
                node = Node(y)
                STstack.append(node)
            if z == 9:
                node = Node(y)
                STstack.append(node)
            if z == 10:
                L = STstack.pop()
                node = Node(y[0:2] + [L] + [y[-1]])
                STstack.append(node)
            # direction rules
            if z == 11:
                STstack.append(y[0])
            if z == 12:
                STstack.append(y[0])
            if z == 13:
                STstack.append(y[0])
            if z == 14:
                STstack.append(y[0])
        return STstack

    def traverseTree(tree):     # run through the syntax tree
        turtleQueue = []
        def executeCommands(turtleQueue):       # animate the mc program
            dq = deque(turtleQueue)
            while dq:
                command = dq.popleft()
                if command[0] == 'createGrid':
                    i = command[1]
                    j = command[2]
                    sc=turtle.Screen()
                    trtl=turtle.Turtle()
                    # method to draw y-axis lines
                    def drawy(val):
                        # line
                        trtl.backward(j*7)
                        # set position
                        trtl.up()
                        trtl.setpos(-300+val,300)
                        trtl.down()
                    # method to draw y-axis lines
                    def drawx(val):
                        # line
                        trtl.forward(i*7)
                        # set position
                        trtl.up()
                        trtl.setpos(-300,300-val)
                        trtl.down()

                    # Main Section
                    # set screen
                    sc.setup(1200,1200)    
                    # set turtle features
                    trtl.speed(100)
                    trtl.up()
                    trtl.setpos(-300,300)
                    trtl.down()
                    trtl.left(90)  
                    trtl.color('lightgreen')
                    # y lines
                    for y in range(i+1):
                        drawy(7*(y+1))
                    # set position for x lines
                    trtl.right(90)
                    trtl.up()
                    trtl.setpos(-300,300)
                    trtl.down()
                    # x lines
                    for x in range(j+1):
                        drawx(7*(x+1))
                elif command[0] == 'placeCat':
                    i = command[1]
                    j = command[2]
                    trtl.up()
                    trtl.setpos(-300+(i*7), 300-(j*7))
                    trtl.down()
                    trtl.color('red')
                    trtl.circle(2)
                elif command[0] == 'placeMouse':
                    i = command[1]
                    j = command[2]
                    trtl.up()
                    trtl.setpos(-300+(i*7), 300-(j*7))
                    trtl.down()
                    trtl.color('blue')
                    trtl.circle(2)
                elif command[0] == 'placeHole':
                    i = command[1]
                    j = command[2]
                    error = command[3]
                    trtl.up()
                    trtl.setpos(-300+(i*7), 300-(j*7))
                    trtl.down()
                    trtl.color('black')
                    trtl.circle(2)
                    if error:
                        messagebox.showerror("Error", "Hole out of bounds")
                elif command[0] == 'moveCat':
                    i = command[1]
                    j = command[2]
                    d = command[3]
                    dist = command[4]
                    error = command[5]
                    trtl.up()
                    trtl.setpos(-300+(i*7), 300-(j*7))
                    trtl.down()
                    trtl.color('red')
                    if d == 'east':
                        trtl.setheading(0)
                    if d == 'north':
                        trtl.setheading(90)
                    if d == 'west':
                        trtl.setheading(180)
                    if d == 'south':
                        trtl.setheading(270)
                    trtl.forward(7*int(dist))
                    trtl.circle(2)
                    if error:
                        messagebox.showerror("Error", "Cat out of bounds")
                elif command[0] == 'moveMouse':
                    i = command[1]
                    j = command[2]
                    d = command[3]
                    dist = command[4]
                    inHole = command[5]
                    error = command[6]
                    trtl.up()
                    trtl.setpos(-300+(i*7), 300-(j*7))
                    trtl.down()
                    trtl.color('blue')
                    if d == 'east':
                        trtl.setheading(0)
                    if d == 'north':
                        trtl.setheading(90)
                    if d == 'west':
                        trtl.setheading(180)
                    if d == 'south':
                        trtl.setheading(270)
                    trtl.forward(7*int(dist))
                    if inHole:      # don't draw mouse if it's hiding in a hole
                        pass 
                    else:
                        trtl.circle(2)
                    if error:
                        messagebox.showerror("Error", "Mouse out of bounds")
            trtl.hideturtle()
            turtle.Screen().exitonclick()
            
        positions = {}      # keep track of positions of all objects
        positions['hole'] = set()       # holes don't move so we can keep track of all of them in a single set
        q = deque()
        q.append(tree[0])       # add root node of syntax tree to queue
        x = 0       # track grid columns
        y = 0       # track grid rows
        isDead = set()      # track dead objects

        while q:        # traverse nodes in the syntax tree
            error = False       # error handling
            node = q.popleft()
            nodeType = node.data[0]
            if nodeType == 'size':
                i = int(node.data[1])
                j = int(node.data[2])
                x = i       # grid size is static
                y = j
                turtleQueue.append(('createGrid',i,j))
                q.appendleft(node.data[4])
            if nodeType == 'cat':
                cat = node.data[1]
                i = int(node.data[2])
                j = int(node.data[3])
                d = node.data[4]
                positions[cat] = ['cat', i, j, d]
                turtleQueue.append(('placeCat',i,j))
                # traverse through objects to see if there are any already on this square
                for obj in positions:
                    if obj != 'hole' and obj != cat:    # sets are unsubscriptable and objects do not kill themselves
                        # kill mice on the square unless there is a hole
                        if positions[obj][0] == 'mouse' and positions[cat][1] == positions[obj][1] and positions[cat][2] == positions[obj][2] and (i,j) not in positions['hole']:
                            isDead.add(obj)
                        # cat dies due to cat collision
                        if positions[obj][0] == 'cat' and positions[cat][1] == positions[obj][1] and positions[cat][2] == positions[obj][2]:
                            isDead.add(cat)
            if nodeType == 'mouse':
                mouse = node.data[1]
                i = int(node.data[2])
                j = int(node.data[3])
                d = node.data[4]
                positions[mouse] = ['mouse', i, j, d]
                turtleQueue.append(('placeMouse',i,j))
                # traverse through objects to see if there are any already on this square
                for obj in positions:
                    if obj != 'hole' and obj != mouse:  # sets are unsubscriptable and objects do not kill themselves
                        # mouse dies to mouse collision unless there is a hole
                        if positions[obj][0] == 'mouse' and positions[mouse][1] == positions[obj][1] and positions[mouse][2] == positions[obj][2] and (i,j) not in positions['hole']:
                            isDead.add(mouse)
                        # mouse dies to cat unless there is a hole
                        if positions[obj][0] == 'cat' and positions[mouse][1] == positions[obj][1] and positions[mouse][2] == positions[obj][2] and (i,j) not in positions['hole']:
                            isDead.add(mouse)
            if nodeType == 'hole':
                i = int(node.data[1])
                j = int(node.data[2])
                # bounds check
                if i > x or i < 0 or j > y or j < 0:
                    error = True
                turtleQueue.append(('placeHole', i,j, error))
                positions['hole'].add((i,j))
            if nodeType == 'seq':
                L = node.data[1]
                S = node.data[2]
                q.appendleft(S)
                q.appendleft(L)
            if nodeType == 'move':
                var = node.data[1]
                distance = node.data[2]
                change = 0
                # dead objects don't move
                if var in isDead:
                    pass
                else:
                    # bounds check
                    if positions[var][3] == 'north':
                        change = positions[var][2] - int(distance)
                        if change > y or change < 0 or positions[var][1] > x or positions[var][1] < 0:
                            error = True
                    if positions[var][3] == 'west':
                        change = positions[var][1] - int(distance)
                        if change > x or change < 0 or positions[var][2] > x or positions[var][2] < 0:
                            error = True
                    if positions[var][3] == 'south':
                        change = positions[var][2] + int(distance)
                        if change > y or change < 0 or positions[var][1] > x or positions[var][1] < 0:
                            error = True
                    if positions[var][3] == 'east':
                        change = positions[var][1] + int(distance)
                        if change > x or change < 0 or positions[var][2] > x or positions[var][2] < 0:
                            error = True

                    if positions[var][0] == 'mouse':
                        # hole check
                        if positions[var][3] == 'north':
                            if (positions[var][1], change) in positions['hole']:     # mouse moves to hole
                                turtleQueue.append(('moveMouse', positions[var][1], positions[var][2], positions[var][3], distance, True, error))
                            else:
                                turtleQueue.append(('moveMouse', positions[var][1], positions[var][2], positions[var][3], distance, False, error))
                        if positions[var][3] == 'west':
                            if (change, positions[var][2]) in positions['hole']:     # mouse moves to hole
                                turtleQueue.append(('moveMouse', positions[var][1], positions[var][2], positions[var][3], distance, True, error))
                            else:
                                turtleQueue.append(('moveMouse', positions[var][1], positions[var][2], positions[var][3], distance, False, error))
                        if positions[var][3] == 'south':
                            if (positions[var][1], change) in positions['hole']:     # mouse moves to hole
                                turtleQueue.append(('moveMouse', positions[var][1], positions[var][2], positions[var][3], distance, True, error))
                            else:
                                turtleQueue.append(('moveMouse', positions[var][1], positions[var][2], positions[var][3], distance, False, error))
                        if positions[var][3] == 'east':
                            if (change, positions[var][2]) in positions['hole']:     # mouse moves to hole
                                turtleQueue.append(('moveMouse', positions[var][1], positions[var][2], positions[var][3], distance, True, error))
                            else:
                                turtleQueue.append(('moveMouse', positions[var][1], positions[var][2], positions[var][3], distance, False, error))
                        # check if move will kill the mouse
                        for obj in positions:
                            if obj != 'hole' and obj != var:       # sets are not subscriptable and objects do not kill themselves
                                if positions[var][3] == 'north':
                                    if positions[obj][0] == 'mouse' and positions[var][1] == positions[obj][1] and change == positions[obj][2] and (positions[var][1], change) not in positions['hole']:     # cat kills mouse
                                        isDead.add(var)
                                    if positions[obj][0] == 'cat' and positions[var][1] == positions[obj][1] and change == positions[obj][2]:     # cat dies upon collision with another cat
                                        isDead.add(var)  
                                if positions[var][3] == 'west':
                                    if positions[obj][0] == 'mouse' and change == positions[obj][1] and positions[var][2] == positions[obj][2] and (change, positions[var][2]) not in positions['hole']:     # cat kills mouse
                                        isDead.add(var)
                                    if positions[obj][0] == 'cat' and change == positions[obj][1] and positions[var][2] == positions[obj][2]:     # cat dies upon collision with another cat
                                        isDead.add(var)
                                if positions[var][3] == 'south':
                                    if positions[obj][0] == 'mouse' and positions[var][1] == positions[obj][1] and change == positions[obj][2] and (positions[var][1], change) not in positions['hole']:     # cat kills mouse
                                        isDead.add(var)
                                    if positions[obj][0] == 'cat' and positions[var][1] == positions[obj][1] and change == positions[obj][2]:     # cat dies upon collision with another cat
                                        isDead.add(var)
                                if positions[var][3] == 'east':
                                    if positions[obj][0] == 'mouse' and change == positions[obj][1] and positions[var][2] == positions[obj][2] and (change, positions[var][2]) not in positions['hole']:     # cat kills mouse
                                        isDead.add(var)
                                    if positions[obj][0] == 'cat' and change == positions[obj][1] and positions[var][2] == positions[obj][2]:     # cat dies upon collision with another cat
                                        isDead.add(var)
                                    
                    if positions[var][0] == 'cat':
                        turtleQueue.append(('moveCat', positions[var][1], positions[var][2], positions[var][3], distance, error))
                        # check if move will kill the cat
                        for obj in positions:
                            if obj != 'hole' and obj != var:
                                if positions[var][3] == 'north':
                                    if positions[obj][0] == 'mouse' and positions[var][1] == positions[obj][1] and change == positions[obj][2] and (positions[var][1], change) not in positions['hole']:     # cat kills mouse
                                        isDead.add(obj)
                                    if positions[obj][0] == 'cat' and positions[var][1] == positions[obj][1] and change == positions[obj][2]:     # cat dies upon collision with another cat
                                        isDead.add(var)  
                                if positions[var][3] == 'west':
                                    if positions[obj][0] == 'mouse' and change == positions[obj][1] and positions[var][2] == positions[obj][2] and (change, positions[var][2]) not in positions['hole']:     # cat kills mouse
                                        isDead.add(obj)
                                    if positions[obj][0] == 'cat' and change == positions[obj][1] and positions[var][2] == positions[obj][2]:     # cat dies upon collision with another cat
                                        isDead.add(var)
                                if positions[var][3] == 'south':
                                    if positions[obj][0] == 'mouse' and positions[var][1] == positions[obj][1] and change == positions[obj][2] and (positions[var][1], change) not in positions['hole']:     # cat kills mouse
                                        isDead.add(obj)
                                    if positions[obj][0] == 'cat' and positions[var][1] == positions[obj][1] and change == positions[obj][2]:     # cat dies upon collision with another cat
                                        isDead.add(var)
                                if positions[var][3] == 'east':
                                    if positions[obj][0] == 'mouse' and change == positions[obj][1] and positions[var][2] == positions[obj][2] and (change, positions[var][2]) not in positions['hole']:     # cat kills mouse
                                        isDead.add(obj)
                                    if positions[obj][0] == 'cat' and change == positions[obj][1] and positions[var][2] == positions[obj][2]:     # cat dies upon collision with another cat
                                        isDead.add(var)
                    # update position
                    if positions[var][3] == 'north':
                        positions[var][2] = change
                    if positions[var][3] == 'west':
                        positions[var][1] = change
                    if positions[var][3] == 'south':
                        positions[var][2] = change
                    if positions[var][3] == 'east':
                        positions[var][1] = change
            # update direction
            if nodeType == 'clockwise':
                var = node.data[1]
                if positions[var][3] == 'north':
                    positions[var][3] = 'east'
                elif positions[var][3] == 'west':
                    positions[var][3] = 'north'
                elif positions[var][3] == 'south':
                    positions[var][3] = 'west'
                elif positions[var][3] == 'east':
                    positions[var][3] = 'south'

            if nodeType == 'repeat':
                i = node.data[1]
                for _ in range(int(i)):
                    q.appendleft(node.data[2])
        # all moves are added to a turtleQueue which is then animated with python turtle
        executeCommands(turtleQueue)
        return 

if __name__ == "__main__":
    # create table
    file = open('./parsedata.txt', 'r')
    table = parser.readTable(file)
    file.close()

    # get tokens
    file = open('./' + input('Enter file name: '), 'r')
    tokenTypes = scanner.scan(file)
    file.close()

    # parser
    structures = parser.LRParseRoutine(tokenTypes+['$'], table)   # None if error, otherwise should be an array of productions
    if structures == None:
        print('CATANDMOUSE program is not syntactically correct')
    # animate
    else:
        tree = Project3.createTree(structures)
        Project3.traverseTree(tree)
        