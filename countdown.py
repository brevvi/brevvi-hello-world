import time

def countdown(n):
    for i in range(0,n):
        if n == 0:
            print('Shutdown!')
        elif n < 0:
            print('Please insert a numember greater than zero.')
        else:
            time.sleep(1)
            print(n-1)
        n = n - 1
    print('System shutdown!')

print('Contagem regressiva:')
n = int(input())
countdown(n)
