# C(n, r) = C(n - 1, r - 1) * n/r
n = 990
r = 33
ans = n-r
for m,k in zip(range(n - r + 1, n+1), range(1, r+1)):
	ans = ans * m
	ans = ans / k
print(ans)