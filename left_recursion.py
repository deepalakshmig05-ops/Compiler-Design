def remove_left_recursion(A, alpha, beta):
    print(A,"->",beta+A+"'")
    print(A+"' ->",alpha+A+"' | ε")

A="E"
alpha="+T"
beta="T"

remove_left_recursion(A,alpha,beta)