temp_count = 1

def get_temp():
    global temp_count
    temp = f"T{temp_count}"
    temp_count += 1
    return temp


def generate_intermediate(expr):
    operators = ['*', '/', '+', '-']
    quadruples = []
    triples = []
    indirect = []

    expr = expr.replace(" ", "")
    
    while any(op in expr for op in operators):
        for op in operators:
            if op in expr:
                idx = expr.find(op)
                
                left = expr[idx-1]
                right = expr[idx+1]
                temp = get_temp()
                
                # Quadruple: (op, arg1, arg2, result)
                quadruples.append((op, left, right, temp))
                
                # Triple: (op, arg1, arg2)
                triples.append((op, left, right))
                
                # Replace in expression
                expr = expr[:idx-1] + temp + expr[idx+2:]
                break

    # Indirect triple (just index reference)
    for i in range(len(triples)):
        indirect.append(i)

    return quadruples, triples, indirect


# Input
expression = input("Enter expression (e.g., a+b*c): ")

quad, triple, indirect = generate_intermediate(expression)

print("\nQuadruple:")
for q in quad:
    print(q)

print("\nTriple:")
for i, t in enumerate(triple):
    print(f"{i}: {t}")

print("\nIndirect Triple:")
for i in indirect:
    print(f"Pointer -> {i}")