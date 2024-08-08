num = []
for i in range(5):
    num.append(int(input()))
    
mean = int(sum(num)/len(num))
num = sorted(num)

print(mean)
print(num[2])
