n, m, d = [int(x) for x in input().split(' ')]
table = [[int(x) for x in input().split(' ')] for _ in range(n)]
ranges = [(-1, 0)]
archer = []

# 사정거리
for i in range(2, d+1):
    for j in range(1, i+1):
        ranges.append((0-j, -i+j))
    for j in range(1, 2*i-i):
        ranges.append((-i+j, 0+j))

# 궁수위치
for i in range(m-2):
    for j in range(1+i,m-1):
        for k in range(1+j,m):
            archer.append((i, j, k))

# 사격
def shoot(shootrange, turn, position, end, turntable, nexttable):
    for target in shootrange:
        if turn+target[0]>=0 and position+target[-1]>=0 and position+target[-1]<end:
            if turntable[turn+target[0]][position+target[-1]] > 0:
                if turntable[turn+target[0]][position+target[-1]] == 1:
                    turntable[turn+target[0]][position+target[-1]] = 2
                    nexttable[turn+target[0]][position+target[-1]] = 0
                    return 1
                return 0
    return 0

# 모든 위치 확인
cnt = [0 for _ in range(len(archer))]
for a in range(len(archer)):
    table3 = [list(t) for t in table]
    for i in reversed(range(n+1)):
        table2 = [list(t) for t in table3]
        for j in archer[a]:
            cnt[a] += shoot(ranges, i, j, m, table2, table3)

print(max(cnt))
