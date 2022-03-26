import sys

chars = {}
word = sys.stdin.readline().replace('\n', '').upper()

for i in word:
    if not i in chars:
        chars[i] = 1
    
    else:
        chars[i] += 1

nums = list(chars.values())
copy = nums.copy()
nums.sort()

if len(word) != 1 and nums[-1] == nums[-2]:
    print("?")
else:
    print(list(chars.keys())[copy.index(nums[-1])])