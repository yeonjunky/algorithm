def bt(n: int, m: int, nums: list[str]):
    if len(nums) == m:
        print(" ".join(nums))
        return 
    for i in range(1, n + 1):
        i = str(i)
        if i not in nums:
            nums.append(i)
            bt(n, m, nums)
            nums.pop()

n, m = map(int, input().split())
l = []
bt(n, m, l)