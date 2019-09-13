#Week 2B ( 6.9.2019 )
#Pass Statement

def fib(n):    
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


 fib(400)

 #Returns A List of the number (Fibonacci)

 def fib2(n):
 	result = []
 	a , b = 0 , 1
 	while a < n:
 		result.append(a)
 		a, b = b, a + b
 		result result

 f100 = fib2(100)		

#Default Argument Values¶

 i = 5

def f(arg=i):
    print(arg)

i = 6
f()


####

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))