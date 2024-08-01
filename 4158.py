# 4158
def binary_search(target, data):
    start = 0
    end = len(data)-1

    while start <= end:
        mid = (start+end)//2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid-1
        else:
            start = mid + 1
    return -1

while(True):
    n, m = map(int, input().split())
    if n==0 and m==0:
        break

    nlist = []
    mlist = []

    for i in range(n):
        nlist.append(int(input()))
    for i in range(m):
        mlist.append(int(input()))

    cnt = 0

    for i in range(n):
        target = nlist[i]
        answer = binary_search(target, mlist)
        if answer != -1:
            cnt += 1

    print(cnt)

'''
문제를 제대로 읽자,,
입력은 여러 개의 테스트 케이스로 이루어져 있다.
라는 말은 종료 조건에 도달하지 않으면 계속 코드가 돌아간다는 말이나 마찬가지 이다!!!!!
종료 조건 처리를 제대로 하자
'''
