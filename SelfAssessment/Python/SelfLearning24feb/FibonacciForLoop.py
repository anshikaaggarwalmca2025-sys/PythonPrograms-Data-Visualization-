#program to generate fibonacci series using for loop
n = int(input())

a = 0
b = 1

for i in range(n):
    print(a)
    a, b = b, a + b

   

#Output
n = 5

0
1
1
2
3
