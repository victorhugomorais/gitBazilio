def fib1(n):
    return fib_aux(n,0,1)

def fib_aux(n, corrente, proximo):
    if(n==1):
        return corrente
    return fib_aux(n-1, proximo,corrente+proximo)


