#insert para o modo de inserção 
#para salvar: SHIFT + : + "wq"

import sys #pra executar no cmd: python + nome do arquivo.py + parametro sys na linha 12

def fib(n):
    if(n==1):
        return 0
    if (n==2):
        return 1
    return fib(n-1) + fib(n-2)



