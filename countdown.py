def countdown(n):
    if n == 0:
        print('Shutdown')
    elif n < 0
        print('Please insert a numember greater than zero.')
    else:
        for i in range(len(n)):
            if i > 0:
                print(i)
                n = i - 1
            else:
                print('Shutdown')

n = input()
countdown(n)
