# BOJ 21924: 도시건설
# https://www.acmicpc.net/problem/21924

import sys
import heapq

edges = []
total_cost = 0
min_cost = 0


# find parent recursively
def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]


def union(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


# up to 500,000 lines -> sys.stdin.readline()
n, m = map(int, sys.stdin.readline().split())
parents = [i for i in range(n+1)]  # for convenience

for i in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    total_cost += cost
    heapq.heappush(edges, (cost, a, b))

for i in range(m):
    cost, a, b = heapq.heappop(edges)
    if find_parent(parents, a) != find_parent(parents, b):
        union(parents, a, b)
        min_cost += cost

# final union
for i in range(1, n+1):
    parents[i] = find_parent(parents, i)

if any(x > 1 for x in parents):
    print(-1)
else:
    print(total_cost - min_cost)
