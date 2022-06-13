import sys


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    applicants = []
    result = 0

    for i in range(n):
        applicant = tuple(map(int, sys.stdin.readline().split()))
        applicants.append(applicant)

    applicants.sort(key=lambda a: a[0])

    meeting_rank = applicants[0][1]

    for a in applicants:
        if meeting_rank >= a[1]:
            meeting_rank = a[1]
            result += 1

    print(result)
