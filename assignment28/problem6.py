#Logisticsc route consistency check 
n = int(input())
arr = list(map(int, input().split()))

if len(arr) == len(set(arr)):
    print("YES")
else:
    print("NO")