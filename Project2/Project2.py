import scanner

stack = []

'''
def LRParseRoutine():
    state = 0
    stack.append(state)
    read(symbol) # obtain the lookahead symbol
    entry = T[state,symbol] # T is the LR parse table
    while entry.action != accept:
        if entry.action == shift:
            stack.append(symbol)
            state = entry.state
            stack.append(state)
            read(symbol)
        elif entry.action == reduce: 
            do 2∗size rhs times {pop()} pop entry.rule.rhs and states
            state := top-of-stack() do not pop!
            push(entry.rule.lhs)
            state = T[state,entry.rule.lhs]
            push(state)
        elif entry.action == blank then
            error
        entry = T[state, symbol]
    if symbol != '$': 
        error
'''

if __name__ == "__main__":
    file = open('./' + input('Enter file name: '), 'r')
    tokens = scanner.scan(file)
    file.close()
    for token in tokens:
        print(token[0])