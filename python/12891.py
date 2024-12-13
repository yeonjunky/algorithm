s, p = map(int, input().split())
dna = input()
n = list(map(int, input().split()))
cnt = 0
dna_cnt = {"A": 0, "C": 0, "G": 0, "T": 0}

for i in range(p - 1):
    dna_cnt[dna[i]] += 1

for i in range(p - 1, s):
    dna_cnt[dna[i]] += 1
    cnt += dna_cnt["A"] >= n[0] and dna_cnt["C"] >= n[1] and \
        dna_cnt["G"] >= n[2] and dna_cnt["T"] >= n[3]
    dna_cnt[dna[i - p + 1]] -= 1

print(cnt)