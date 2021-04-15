# parser.py

import numpy as np
from collections import deque

# grammar rules
grammar = {
    0: ("P'", "P"),
    1: ("P", "ziibLt"),
    2: ("L", "S;"),
    3: ("L", "LS;"),
    4: ("S", "cviiD"), 
    5: ("S", "mviiD"),
    6: ("S", "hii"),
    7: ("S", "ov"),
    8: ("S", "ovi"),
    9: ("S", "lv"),
    10: ("S", "riLd"),
    11: ("D", "n"),
    12: ("D", "s"),
    13: ("D", "e"),
    14: ("D", "w")
}
# indexes for the table
symbolIndexes = {
    'z': 1,
    'i': 2,
    'b': 3,
    't': 4,
    ';': 5,
    'c': 6,
    'v': 7,
    'm': 8,
    'h': 9,
    'o': 10,
    'l': 11,
    'r': 12,
    'd': 13,
    'n': 14,
    's': 15,
    'e': 16,
    'w': 17,
    '$': 18,
    'P': 19,
    'L': 20,
    'S': 21,
    'D': 22
}

# creates table from parsedata.txt
def readTable(file):
    lines = file.readlines()
    m = len(lines) // 2
    n = (len(lines[0].strip()) // 2) + 1

    # there are two tables in parsedata.txt, so we create them separately and them combine them
    table = [[''] * n for _ in range(m)]
    specialTable = [[''] * 4 for _ in range(m)]

    row = 0
    for line in lines:
        line = line.strip()
        col = 0
        if row >= 39:   # if 2nd table
            col = -1
        string = ''
        for x in range(len(line)):
            if line[x] == '&' or x == len(line)-1:
                if x == len(line)-1 and line[x] != '&':
                    string += line[x]
                if row >= 39:   # 2nd table
                    if col == -1:
                        pass
                    else:
                        specialTable[row-39][col] = string
                else:
                    table[row][col] = string
                string = ''
                col += 1
            else:
                string += line[x] 
        row += 1

    table = np.hstack((table, specialTable))    # combine both tables into one
    return table

# LR(1) Parser
def LRParseRoutine(tokenTypes, table):
    state = 0
    stack = []
    stack.append(state)
    productions = []
    tokenTypes = deque(tokenTypes)
    tup = tokenTypes.popleft() # obtain the lookahead symbol
    symbol = tup[0]
    entry = table[state+1][symbolIndexes[symbol]] # table is the LR parse table

    while entry != 'acc':
        if entry == '':     # error
            return None
        if entry[0] == 's':     # shift
            stack.append(tup)
            state = int(entry[1:])
            stack.append(state)
            tup = tokenTypes.popleft()
            symbol = tup[0]
        elif entry[0].isnumeric():  # also shift
            stack.append(tup)
            state = int(entry)
            stack.append(state)
            tup = tokenTypes.popleft()
            symbol = tup[0]
        elif entry[0] == 'r':       # reduce
            lhs = grammar[int(entry[1:])][0]
            rhs = grammar[int(entry[1:])][1]
            n = 2*len(rhs)
            toAppend = []
            while n > 0:    # pop entry.rule.rhs and states
                toCheck = stack.pop() 
                if type(toCheck) == tuple:
                    toAppend.append(toCheck[1])
                elif type(toCheck) == str:
                    toAppend.append(toCheck)
                n -= 1
            toAppend.reverse()
            state = stack[-1] # do not pop!
            stack.append(lhs)
            productions.append((lhs,toAppend,int(entry[1:])))
            state = table[int(state)+1][symbolIndexes[lhs]]
            stack.append(state) 
        entry = table[int(state)+1][symbolIndexes[symbol]]
    if symbol != '$':   # error
        return None
    return productions

# debug
def printOutput(output):
    # sets column width to the length of the longest string 
    col_width = max(len(str(word)) for row in output for word in row) + 2   # padding
    # print row by row
    for row in output:
        print ("".join(str(word).ljust(col_width) for word in row))
    return 0

    