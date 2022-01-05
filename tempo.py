import sys
import time
from fibonacci2 import fib1

start = time.time()
termofib = fib1(int)(sys.argv[1])
end = time.time()

print(termofib)
print('Tempo de execução' + (str)(end-str))