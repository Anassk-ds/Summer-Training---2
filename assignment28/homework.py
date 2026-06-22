#problem8
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

window = sum(arr[:k])
ans = window

for i in range(k, n):
    window += arr[i] - arr[i-k]
    ans = max(ans, window)

print(ans)

#problem9
s = input()

seen = set()
left = 0
ans = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])
    ans = max(ans, right - left + 1)

print(ans)

#problem10
n = int(input())
arr = list(map(int, input().split()))

seen = set()

for x in arr:
    if x in seen:
        print(x)
        break
    seen.add(x)