'''
idea: 스택으로 괄호 쌍을 찾아냄
      1 ~ 괄호 쌍의 개수 - 1 까지 반복(삭제할 괄호 쌍의 개수)
      위 반복문에서 i개 괄호쌍의 조합들을 만들어내 삭제
      ((1))+2 처럼 중복이 나올 수 있으므로 (1)+2
      결과를 담는 공간을 set사용해서 같은 결과를 여러번 출력하는 상황 방지
'''
import sys
from itertools import combinations


math_ex = sys.stdin.readline().rstrip()
paren = []
result = set()
stk = []

for i, c in enumerate(math_ex):
    if c == '(':
        stk.append(i)

    elif c == ')':
        paren.append((stk.pop(), i))

for i in range(1, len(paren)):
    for c in combinations(paren, i):
        temp = math_ex
        sub_paren = []

        for p_idx in c:
            sub_paren.extend(p_idx)
        sub_paren.sort(reverse=True)

        for p in sub_paren:
            temp = temp[:p] + temp[p + 1:]

        result.add(temp)

result.add(math_ex.replace('(', '').replace(')', ''))
result = sorted(result)

for r in result:
    print(r)
