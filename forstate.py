#Week 2A ( 9.5.2019 )
#for statement

fruit = ['Apple' , 'Banana', 'Orange']
for f in fruit:
	print(w,len(w)) 


animals = ['lion' ,'tiger' ,'leopard']	
for a in animals[:]:
	if len(a) > 6:
		animals.insert(0,a)  # >>> animails.insert(1,a)

print(animals)	

#answer : ['leopard','lion', 'tiger', 'leopard']	


#Range Funciton

for i in range(10):
	print(i)

#answer : 	0 ~ 9
			
range(5,10):
#answer : 5 ~ 9

 for i in range(10,100,10):
  print(i)

 #answer : 10, 20, -> 90 

 a = ['Mary', 'Had', 'A', 'Little', 'Boy']
>>> for i in range(len(a)):
...     print(i,a[i]):

# 0 Mary
# 1	Had
# 2	A
# 3	Little
# 4	Boy


##break and continue Statements, and else Clauses on Loops

#for if continue

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

#answer : 

#for if break else

 for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


   