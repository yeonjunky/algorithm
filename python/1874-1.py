n, *a = open(0)
n = int(n)
a = list(map(int, a))
cnt = 1
result = []
stack = []

for i in range(n):
    while cnt <= a[i]:
        stack.append(cnt)
        result.append("+")
        cnt += 1
    if a[i] == stack[-1]:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        break

if not len(stack):
    print("\n".join(result))