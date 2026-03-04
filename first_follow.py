grammar = {
"E":["TR"],
"R":["+TR","e"],
"T":["FY"],
"Y":["*FY","e"],
"F":["(E)","i"]
}

def first(symbol):
    if not symbol.isupper():
        return {symbol}

    result=set()

    for prod in grammar[symbol]:
        if prod=="e":
            result.add("e")
        else:
            result |= first(prod[0])

    return result

for non in grammar:
    print("FIRST(",non,") =",first(non))