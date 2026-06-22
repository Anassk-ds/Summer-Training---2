#Warehouse shipment monitoring
n = int(input())

inside = set()

for _ in range(n):
    x = int(input())

    if x > 0:
        inside.add(x)
    else:
        inside.discard(-x)

print(len(inside))