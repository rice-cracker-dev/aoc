S = {int(s): 1 for s in open("inputs.txt").read().split(" ")}
PR = lambda: print(sum(S.values()))

def A(d, s, c):
  d[s] = d.get(s, 0) + c

for n in range(75):
  if n == 25:
    PR()

  N = {}
  for s, c in S.items():
    if s == 0:
      A(N, 1, c)
    elif (n := len(dig := str(s))) % 2 == 0:
      A(N, int(dig[:n // 2]), c)
      A(N, int(dig[n // 2:]), c)
    else:
      A(N, s * 2024, c)
  S = N

PR()
