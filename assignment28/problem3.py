#Digital payment fraud detector
n = int(input())

balance = 0
flag = False

for _ in range(n):
    balance += int(input())
    if balance < 0:
        flag = True

if flag:
    print("YES")
else:
    print("NO")
