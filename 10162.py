T = int(input())

a = 60*5
b = 60
c = 10

a_cnt = 0
b_cnt = 0
c_cnt = 0

a_cnt = T//a
T -= a*a_cnt

b_cnt = T//b
T -= b*b_cnt

c_cnt = T//c
T -= c*c_cnt

if T != 0:
    print(-1)
else:
    print(a_cnt)
    print(b_cnt)
    print(c_cnt)
