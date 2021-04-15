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
    def createTree(structures):
        STstack = []
        for (x,y,z) in structures:
            if z == 0:
                pass
            if z == 1:
                L = STstack.pop()
                node = Node(y[0:4] + [L] + [y[-1]])
                STstack.append(node)
            if z == 2:
                pass    # do nothing
            if z == 3:
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
            if z == 11:
                STstack.append(y[0])
            if z == 12:
                STstack.append(y[0])
            if z == 13:
                STstack.append(y[0])
            if z == 14:
                STstack.append(y[0])
        return STstack

    def traverseTree(tree):
        turtleQueue = []
        def executeCommands(turtleQueue):
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
                        trtl.backward(j*10)
                        # set position
                        trtl.up()
                        trtl.setpos(-300+val,300)
                        trtl.down()
                    # method to draw y-axis lines
                    def drawx(val):
                        # line
                        trtl.forward(i*10)
                        # set position
                        trtl.up()
                        trtl.setpos(-300,300-val)
                        trtl.down()

                    # Main Section
                    # set screen
                    sc.setup(800,800)    
                    # set turtle features
                    trtl.speed(100)
                    trtl.up()
                    trtl.setpos(-300,300)
                    trtl.down()
                    trtl.left(90)  
                    trtl.color('lightgreen')
                    # y lines
                    for y in range(i+1):
                        drawy(10*(y+1))
                    # set position for x lines
                    trtl.right(90)
                    trtl.up()
                    trtl.setpos(-300,300)
                    trtl.down()
                    # x lines
                    for x in range(j+1):
                        drawx(10*(x+1))
                elif command[0] == 'placeCat':
                    i = command[1]
                    j = command[2]
                    trtl.up()
                    trtl.setpos(-300+(i*10), 300-(j*10))
                    trtl.down()
                    trtl.color('red')
                    trtl.circle(2)
                elif command[0] == 'placeMouse':
                    i = command[1]
                    j = command[2]
                    trtl.up()
                    trtl.setpos(-300+(i*10), 300-(j*10))
                    trtl.down()
                    trtl.color('blue')
                    trtl.circle(2)
                elif command[0] == 'placeHole':
                    i = command[1]
                    j = command[2]
                    error = command[3]
                    trtl.up()
                    trtl.setpos(-300+(i*10), 300-(j*10))
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
                    trtl.setpos(-300+(i*10), 300-(j*10))
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
                    trtl.forward(10*int(dist))
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
                    trtl.setpos(-300+(i*10), 300-(j*10))
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
                    trtl.forward(10*int(dist))
                    if inHole:      # don't draw mouse if it's hiding in a hole
                        pass 
                    else:
                        trtl.circle(2)
                    if error:
                        messagebox.showerror("Error", "Mouse out of bounds")
            trtl.hideturtle()
            turtle.Screen().exitonclick()
            
        positions = {}
        positions['hole'] = set()
        q = deque()
        q.append(tree[0])
        x = 0
        y = 0
        isDead = set()

        while q:
            error = False
            node = q.popleft()
            nodeType = node.data[0]
            if nodeType == 'size':
                i = int(node.data[1])
                j = int(node.data[2])
                x = i
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
            if nodeType == 'mouse':
                mouse = node.data[1]
                i = int(node.data[2])
                j = int(node.data[3])
                d = node.data[4]
                positions[mouse] = ['mouse', i, j, d]
                turtleQueue.append(('placeMouse',i,j))
            if nodeType == 'hole':
                i = int(node.data[1])
                j = int(node.data[2])
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
                if positions[var][3] == 'north':
                    change = positions[var][2] - int(distance)
                    if change > y or change < 0:
                        error = True
                if positions[var][3] == 'west':
                    change = positions[var][1] - int(distance)
                    if change > x or change < 0:
                        error = True
                if positions[var][3] == 'south':
                    change = positions[var][2] + int(distance)
                    if change > y or change < 0:
                        error = True
                if positions[var][3] == 'east':
                    change = positions[var][1] + int(distance)
                    if change > x or change < 0:
                        error = True
                if positions[var][0] == 'mouse':
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
                if positions[var][0] == 'cat':
                    turtleQueue.append(('moveCat', positions[var][1], positions[var][2], positions[var][3], distance, error))
                if positions[var][3] == 'north':
                    positions[var][2] = change
                if positions[var][3] == 'west':
                    positions[var][1] = change
                if positions[var][3] == 'south':
                    positions[var][2] = change
                if positions[var][3] == 'east':
                    positions[var][1] = change
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
        executeCommands(turtleQueue)
        return

if __name__ == "__main__":
    # create table
    file = open('./parsedata.txt', 'r')
    table = parser.readTable(file)
    #printOutput(table)
    file.close()

    # get tokens
    file = open('./' + input('Enter file name: '), 'r')
    tokenTypes = scanner.scan(file)
    #print(scanner.symbolTable)
    file.close()

    # parser
    structures = parser.LRParseRoutine(tokenTypes+['$'], table)   # None if error, otherwise should be an array of productions
    if structures == None:
        print('CATANDMOUSE program is not syntactically correct')
    else:
        tree = Project3.createTree(structures)
        q = deque()
        q.append(tree[0])
        while q:
            item = q.popleft()
            if type(item) != Node:
                print(item)
            else:  
                for x in reversed(item.data):
                    q.appendleft(x)
        Project3.traverseTree(tree)
                

        