#Smart server memory allocation
n = int(input())
arr = list(map(int, input().split()))
limit = int(input())

left = 0
total = 0
ans = 0

for right in range(n):
    total += arr[right]

    while total > limit:
        total -= arr[left]
        left += 1

    ans = max(ans, right - left + 1)

print(ans)