import sys


meetings = []
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    meeting = tuple(map(int, sys.stdin.readline().split()))
    meetings.append(meeting)

meetings.sort(key=lambda m: (m[1], m[0]))

end = meetings[-1][1]
times = [0] * end
last = meetings[0][1]
meetings_queue = [meetings[0]]

meetings = meetings[1:]

for m in meetings:
    if last <= m[0]:
        last = m[1]
        meetings_queue.append(m)

print(len(meetings_queue))
