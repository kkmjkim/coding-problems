# BOJ 5032: 탄산음료
# https://www.acmicpc.net/problem/5032

e, f, c = map(int, input().split())

bottles = e + f
count = 0
while bottles >= c:
    new = bottles // c
    bottles -= (c-1) * new
    count += new

print(count)
