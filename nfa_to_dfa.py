nfa = {
    0: {'a':[0,1], 'b':[0]},
    1: {'b':[2]},
    2: {}
}

def nfa_to_dfa(nfa,start):
    unmarked=[{start}]
    dfa=[]

    while unmarked:
        state=unmarked.pop()
        dfa.append(state)

        for symbol in ['a','b']:
            next_state=set()
            for s in state:
                if symbol in nfa[s]:
                    next_state.update(nfa[s][symbol])

            if next_state and next_state not in dfa:
                unmarked.append(next_state)

    print("DFA States:",dfa)

nfa_to_dfa(nfa,0)