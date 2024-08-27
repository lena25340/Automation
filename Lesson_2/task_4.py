def fizz_buzz(x):
    for i in range(1, x+1):
        if i % 3 == 0  and i %5 == 0:
            print("fizz_buzzz")
        elif  i % 3 == 0  and i %5!= 0:
            print("fizz")
        elif i % 5 == 0  and i %3!=0:
            print("buzz")
        else:
            print(i)
        
x = input( "Введите  число: ")
x = int(x)
print( fizz_buzz(x))
