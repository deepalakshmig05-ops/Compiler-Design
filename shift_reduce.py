stack=[]
input_string="id+id"
grammar=["E->E+E","E->id"]

print("Input:",input_string)

for char in input_string:
    stack.append(char)
    print("Shift:",stack)

    if "".join(stack[-2:])=="id":
        stack[-2:] = ["E"]
        print("Reduce to E:",stack)

print("Final Stack:",stack)