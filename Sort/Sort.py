n = int(input("Enter quantity of strings: "))
i = 0
j = 0
s = []
for i in range(0, n):
    s.append(input())
print()
print("Sorting on alphabed:")
s.sort()
for i in range(0, n):
    print(s[i])
print()
print("Sorting on quantity:")
for i in range(0, n):
    for j in range(0, n):       
        if len(s[i]) < len(s[j]):
            s[i], s[j] = s[j], s[i]
print()

for i in range(0, n):
    print(s[i])
print()
print("ok")

"""
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    for i in range(n):
        print(a[i])
"""

