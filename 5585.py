n = int(input())

n = 1000-n

a = n//500
n -= a*500
b = n//100
n -= b*100
c = n//50
n -= c*50
d = n//10
n -= d*10
e = n//5
n -= e*5
f = n

print(a+b+c+d+e+f)
