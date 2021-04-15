# Project3.py

import scanner
import parser
class Node:
    def __init__(self, data = []): 
        self.data = data

class Project3:
    def createTree(structures):
        STstack = []
        for (x,y) in structures:
            if z == 3:      # two non-terminals in RHS
                pass
                # TODO: create node of type "seq" containing references to the two syntax trees
            if z == 0 or z == 2 or z == 4 or z == 5 or z == 10:     # one non-terminal in RHS
                pass
            else:
                y[0] = Node(y[1:])
                STstack.append(y[0])
                



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
        parser.printOutput(structures)