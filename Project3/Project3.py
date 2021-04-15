# Project3.py

import scanner
import parser
from collections import deque
import turtle

class Node:
    def __init__(self, data): 
        self.data = data

class Project3:
    def createTree(structures):
        STstack = []
        for (x,y,z) in structures:
            #print(x,y,z)
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
                node = Node(y[0:5] + [D])
                STstack.append(node)
            if z == 5:
                D = STstack.pop()
                node = Node(y[0:5] + [D])
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
                node = Node(['D'] + y)
                STstack.append(node)
            if z == 12:
                node = Node(['D'] + y)
                STstack.append(node)
            if z == 13:
                node = Node(['D'] + y)
                STstack.append(node)
            if z == 14:
                node = Node(['D'] + y)
                STstack.append(node)
        return STstack

    def traverseTree(tree):
        def createGrid(i,j):
            sc=turtle.Screen()
            trtl=turtle.Turtle()
            # method to draw y-axis lines
            def drawy(val):
                # line
                trtl.forward(j*10)
                # set position
                trtl.up()
                trtl.setpos(-300+val,-300)
                trtl.down()
            # method to draw y-axis lines
            def drawx(val):
                # line
                trtl.forward(i*10)
                # set position
                trtl.up()
                trtl.setpos(-300,-300+val)
                trtl.down()

            # Main Section
            # set screen
            sc.setup(800,800)    
            # set turtle features
            trtl.speed(100)
            trtl.up()
            trtl.setpos(-300,-300)
            trtl.down()
            trtl.left(90)  
            trtl.color('lightgreen')
            # y lines
            for y in range(i+1):
                drawy(10*(y+1))
            # set position for x lines
            trtl.right(90)
            trtl.up()
            trtl.setpos(-300,-300)
            trtl.down()
            # x lines
            for x in range(j+1):
                drawx(10*(x+1))
            turtle.Screen().exitonclick()
            
        def placeCat(cat,i,j):
            return 0
        def placeMouse(mouse,i,j):
            return 0
        def placeHole(i,j):
            return 0
        
        q = deque()
        q.append(tree[0])
        while q:
            node = q.popleft()
            nodeType = node.data[0]
            if nodeType == 'size':
                i = int(node.data[1])
                j = int(node.data[2])
                createGrid(i,j)
            if nodeType == 'cat':
                cat = node.data[1]
                i = int(node.data[2])
                j = int(node.data[3])
                #placeCat(cat,i,j)
            if nodeType == 'mouse':
                mouse = node.data[1]
                i = int(node.data[2])
                j = int(node.data[3])
                #placeMouse(mouse,i,j)
            if nodeType == 'hole':
                i = int(node.data[1])
                j = int(node.data[2])
                #placeHole(i,j)
            if nodeType == 'seq':
                pass
            if nodeType == 'move':
                pass
            if nodeType == 'clockwise':
                pass
            if nodeType == 'repeat':
                pass
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
        Project3.traverseTree(tree)

        