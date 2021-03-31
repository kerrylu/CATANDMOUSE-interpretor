stack = []

def LRParseRoutine()
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
        else if entry.action == reduce: 
            do 2∗size rhs times {pop()} pop entry.rule.rhs and states
            state := top-of-stack() do not pop!
            push(entry.rule.lhs)
            state = T[state,entry.rule.lhs]
            push(state)
        else if entry.action == blank then
            error
        entry = T[state, symbol]
    if symbol != '$': 
        error