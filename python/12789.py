from collections import deque

n = int(input())
students = list(map(int, input().split()))
d = deque(students)
last = 0
stack = []

while d:
    if d[0] == last + 1:
        last = d.popleft()
    elif len(stack) and stack[-1] == last + 1:
        last = stack.pop()
    else:
        stack.append(d.popleft())

len = len(stack)
is_nice = True
for _ in range(len):
    num = stack.pop()
    if num != last + 1:
        is_nice = False
        break
    else:
        last = num

if is_nice:
    print("Nice")
else:
    print("Sad")
