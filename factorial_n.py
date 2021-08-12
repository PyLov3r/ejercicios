x = int(input('Valor de "x": '))
n = int(input('Valor de "n": '))

factorial = 1

e = 1 + x
e1= 0
for i in range(1,n+2):
    e = e + e1
    factorial *= i
    if i == 1:
        continue
    else:
        e1 = x**i/factorial
    
print(e)
       
        
