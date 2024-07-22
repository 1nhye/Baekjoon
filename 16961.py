n = int(input())
t_days = []
s_days = []
fifth = 0

for i in range(366):
    t_days.append(0)
    s_days.append(0)

for i in range(n):
    c, s, e = input().split()
    s = int(s)
    e = int(e)

    if c == 'T':
        for i in range(s-1, e):
            t_days[i] += 1
    else:
        for i in range(s-1, e):
            s_days[i] += 1

    if fifth < e-s+1:
        fifth = e-s+1

first = 0
for i in range(366):
    if t_days[i] + s_days[i] == 0:
        first += 1
first = 366-first

second = 0
for i in range(366):
    max = t_days[i] + s_days[i]

    if second < max:
        second = max

third = 0
for i in range(366):
    total = t_days[i]+s_days[i]
    if total != 0 and t_days[i] == s_days[i]:
        third += 1

fourth = 0
for i in range(366):
    max2 = t_days[i] + s_days[i]
    if t_days[i] == s_days[i]:
        if fourth < max2:
            fourth = max2

print(first, second, third, fourth, fifth, sep='\n')
