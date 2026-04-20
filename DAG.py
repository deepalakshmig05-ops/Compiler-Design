class Node:
    def __init__(self, op, left=None, right=None):
        self.op = op
        self.left = left
        self.right = right


# Store already computed expressions
dag = {}

def get_node(op, left, right):
    key = (op, left, right)
    
    if key in dag:
        return dag[key]
    
    node = Node(op, left, right)
    dag[key] = node
    return node


def build_dag(expressions):
    results = {}

    for exp in expressions:
        left, right_expr = exp.split("=")
        left = left.strip()
        right_expr = right_expr.strip()

        # Assume format: a = b + c
        if '+' in right_expr:
            op = '+'
        elif '-' in right_expr:
            op = '-'
        elif '*' in right_expr:
            op = '*'
        elif '/' in right_expr:
            op = '/'

        operands = right_expr.split(op)
        op1 = operands[0].strip()
        op2 = operands[1].strip()

        node = get_node(op, op1, op2)
        results[left] = node

    return results


def print_dag():
    print("\nDAG Nodes (Unique Computations):")
    for key in dag:
        print(key)


# Input
n = int(input("Enter number of expressions: "))
expressions = []

for _ in range(n):
    expressions.append(input())

build_dag(expressions)
print_dag()