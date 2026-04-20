temp_count = 1

def get_temp():
    global temp_count
    t = f"T{temp_count}"
    temp_count += 1
    return t


def generate_code(expr):
    expr = expr.replace(" ", "")
    operators = ['*', '/', '+', '-']
    code = []

    while any(op in expr for op in operators):
        for op in operators:
            if op in expr:
                i = expr.find(op)
                
                left = expr[i-1]
                right = expr[i+1]
                temp = get_temp()

                # Generate assembly-like code
                code.append(f"LOAD {left}")
                
                if op == '+':
                    code.append(f"ADD {right}")
                elif op == '-':
                    code.append(f"SUB {right}")
                elif op == '*':
                    code.append(f"MUL {right}")
                elif op == '/':
                    code.append(f"DIV {right}")
                
                code.append(f"STORE {temp}")

                # Replace expression
                expr = expr[:i-1] + temp + expr[i+2:]
                break

    return code


# Input
expression = input("Enter expression (e.g., a+b*c): ")

instructions = generate_code(expression)

print("\nGenerated Code:")
for line in instructions:
    print(line)