chars = {}
word = input().upper()

for i in word:
    if not i in chars:
        chars[i] = 1
    else:
        chars[i] += 1

nums = list(chars.values())
copy = nums.copy()
nums.sort()

if len(nums) == 1 or (nums[-1] > nums[-2]):
    print(list(chars.keys())[copy.index(nums[-1])])
else:
    print("?")
