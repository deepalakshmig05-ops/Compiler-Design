from collections import defaultdict

# Grammar representation
grammar = {
    "E": ["E+T", "T"],
    "T": ["T*F", "F"],
    "F": ["(E)", "id"]
}

# Add augmented grammar
start_symbol = "E"
augmented_start = "E'"
grammar[augmented_start] = [start_symbol]

# Function to compute closure
def closure(items):
    closure_set = set(items)
    
    while True:
        new_items = set(closure_set)
        
        for (lhs, rhs, dot_pos) in closure_set:
            # If dot is before a non-terminal
            if dot_pos < len(rhs):
                symbol = rhs[dot_pos]
                
                if symbol in grammar:
                    for production in grammar[symbol]:
                        new_items.add((symbol, production, 0))
        
        if new_items == closure_set:
            break
        
        closure_set = new_items
    
    return closure_set


# Function to compute GOTO
def goto(items, symbol):
    moved = set()
    
    for (lhs, rhs, dot_pos) in items:
        if dot_pos < len(rhs) and rhs[dot_pos] == symbol:
            moved.add((lhs, rhs, dot_pos + 1))
    
    return closure(moved)


# Function to generate LR(0) items
def lr0_items():
    C = []
    
    # Initial state
    I0 = closure([(augmented_start, grammar[augmented_start][0], 0)])
    C.append(I0)
    
    symbols = set()
    for lhs in grammar:
        symbols.add(lhs)
        for prod in grammar[lhs]:
            for ch in prod:
                symbols.add(ch)
    
    while True:
        new_states = []
        
        for I in C:
            for symbol in symbols:
                goto_state = goto(I, symbol)
                
                if goto_state and goto_state not in C and goto_state not in new_states:
                    new_states.append(goto_state)
        
        if not new_states:
            break
        
        C.extend(new_states)
    
    return C


# Display LR(0) items
def print_items(states):
    for i, state in enumerate(states):
        print(f"\nI{i}:")
        for (lhs, rhs, dot_pos) in state:
            item = rhs[:dot_pos] + "." + rhs[dot_pos:]
            print(f"{lhs} -> {item}")


# Run
states = lr0_items()
print_items(states)