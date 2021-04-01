import scanner

stack = []

grammar = {
    0: "P'->P",
    1: "P->z i i b L t",
    2: "L->S ;",
    3: "L->L S ;",
    4: "S->c v i i D", 
    5: "S->m v i i D",
    6: "S->h i i",
    7: "S->o v",
    8: "S->o v i",
    9: "S->l v",
    10: "S->r i L d",
    11: "D->n",
    12: "D->s",
    13: "D->e",
    14: "D->w"
}
def readTable(file):
    lines = file.readlines()
    m = len(lines)
    n = len(lines[0]) // 2
    table = [[''] * n for _ in range(m)]
    row = 0
    for line in lines:
        col = 0
        line = line.strip()
        string = ''
        for ch in line:
            if ch == '&':
                table[row][col] = string
                string = ''
                col += 1
            else:
                string += ch
        row += 1
    return table

def LRParseRoutine(tokenTypes, table):
    state = 0
    stack = []
    stack.append(state)
    
    symbol = tokenTypes.popleft() # obtain the lookahead symbol
    entry = table[state,symbol] # T is the LR parse table
    while entry != 'acc':
        if entry[0] == 's':
            stack.append(symbol)
            state = int(entry[1:])
            stack.append(state)
            symbol = tokenTypes.popleft()
        elif entry[0] == 'r': 
            n = grammar[int(entry[1:])]
            while n > 0:    # pop entry.rule.rhs and states
                stack.pop() 
                n -= 1
            state = stack[-1] # do not pop!
            stack.append(int(entry[1:]))
            state = table[state, int(entry[1:])]
            stack.append(state)
        elif entry.action == '':
            return  # error
        entry = table[state, symbol]
    if symbol != '$': 
        return  # error

def printOutput(output):
    # sets column width to the length of the longest string 
    col_width = max(len(str(word)) for row in output for word in row) + 2   # padding
    # print row by row
    for row in output:
        print ("".join(str(word).ljust(col_width) for word in row))
    return 0

if __name__ == "__main__":
    file = open('./' + input('Enter SLR(1) Parse Table data file: '), 'r')
    table = readTable(file)
    printOutput(table)
    file.close()

    '''
    file = open('./' + input('Enter file name: '), 'r')
    tokens = scanner.scan(file)
    file.close()
    for token in tokens:
        print(token[0])
    '''