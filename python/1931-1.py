import sys


n = int(sys.stdin.readline())
m = []
for _ in range(n):
    m.append(list(map(int, sys.stdin.readline().split())))

m.sort(key=lambda x: (x[1], x[0]))

end = m[-1][1]
time = [0] * end
last_time = m[0][1]
m_queue = [m[0]]

for meeting in m[1:]:
    if last_time <= meeting[0]:
        last_time = meeting[1]
        m_queue.append(meeting)

print(len(m_queue))