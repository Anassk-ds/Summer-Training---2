#Retail sales performance analyzer
n = int(input())
arr = list(map(int, input().split()))

current = arr[0]
best = arr[0]

for i in range(1, n):
    current = max(arr[i], current + arr[i])
    best = max(best, current)

print(best)