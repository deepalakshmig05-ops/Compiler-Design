grammar={
"E":"E+T|T",
"T":"T*F|F",
"F":"(E)|i"
}

leading={}
trailing={}

for nt,prod in grammar.items():
    leading[nt]=set()
    trailing[nt]=set()

    for p in prod.split("|"):
        if p[0].islower() or p[0] in "+*()":
            leading[nt].add(p[0])

        if p[-1].islower() or p[-1] in "+*()":
            trailing[nt].add(p[-1])

print("Leading:",leading)
print("Trailing:",trailing)