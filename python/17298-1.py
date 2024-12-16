n, a = open(0)
n = int(n)
a = list(map(int, a.split()))
stack = []
result = [-1] * n

for i, v in enumerate(a):
    if not stack:
        stack.append(i)

    else:
        while stack and v > a[stack[-1]]:
            result[stack.pop()] = v
        stack.append(i)

print(" ".join(map(str, result)))