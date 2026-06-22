#Cyber security login analysis
s = input()

count = 0

for ch in s:
    if ch == 'F':
        count += 1
        if count >= 3:
            print("ALERT")
            break
    else:
        count = 0
else:
    print("SAFE")