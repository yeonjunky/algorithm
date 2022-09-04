'''
idea: 기본적으로 CCW이용해서 해결
      v1[0] * v2[1] - v1[1] * v2[0], v3[0] * v4[1] - v3[1] * v4[0]
      둘 중 하나만 음수 == 한 쪽은 시계, 다른 한 쪽은 반시계
      v1[0] * v3[1] - v1[1] * v3[0], v2[0] * v4[1] - v2[1] * v4[0]
      또한 둘 중 하나만 음수
      
      위 두 조건 모두 충족해야만 교차,
      그렇지 않다면 교차하지 않으면서 한 직선의 수직방향으로 다른 직선이 존재할 가능성 있음

          \
           \
            \
             \

       -------------
      이런 식으로 위치할 가능성이 있음.
'''

import sys


x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))
x3, y3, x4, y4 = list(map(int, sys.stdin.readline().split()))

v1 = [x3 - x1, y3 - y1]
v2 = [x4 - x1, y4 - y1]
v3 = [x3 - x2, y3 - y2]
v4 = [x4 - x2, y4 - y2]

cp1 = v1[0] * v2[1] - v1[1] * v2[0]
cp2 = v3[0] * v4[1] - v3[1] * v4[0]
cp3 = v1[0] * v3[1] - v1[1] * v3[0]
cp4 = v2[0] * v4[1] - v2[1] * v4[0]

if (cp1 * cp2 < 0) and (cp3 * cp4 < 0):
    print(1)
else:
    print(0)
