s = input()
start_idx = 0
result = 0
s_list = s.split('-')

result += sum(map(int, s_list[0].split('+')))
for i in s_list[1:]:
    result -= sum(map(int, i.split('+')))

print(result)