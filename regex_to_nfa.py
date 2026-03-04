def regex_to_nfa(regex):
    print("Simulating simple NFA transitions\n")

    state = 0
    for char in regex:
        if char.isalpha():
            print(f"q{state} --{char}--> q{state+1}")
            state += 1
        elif char == '*':
            print(f"Loop on q{state}")
        elif char == '|':
            print("Branching state")

regex = input("Enter regular expression: ")
regex_to_nfa(regex)