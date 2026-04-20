def infix_to_prefix(expression):
    expression = expression[::-1]
    
    # Swap brackets
    expression = list(expression)
    for i in range(len(expression)):
        if expression[i] == '(':
            expression[i] = ')'
        elif expression[i] == ')':
            expression[i] = '('
    expression = ''.join(expression)

    postfix = infix_to_postfix(expression)
    return postfix[::-1]


exp = input("Enter infix expression: ")
print("Prefix:", infix_to_prefix(exp))