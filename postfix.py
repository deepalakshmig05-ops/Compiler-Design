def infix_to_postfix(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack = []
    output = ""

    for char in expression:
        if char.isalnum():
            output += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and 
                   precedence[char] <= precedence.get(stack[-1], 0)):
                output += stack.pop()
            stack.append(char)

    while stack:
        output += stack.pop()

    return output


exp = input("Enter infix expression: ")
print("Postfix:", infix_to_postfix(exp))