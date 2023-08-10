import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}

for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        if word in dic.keys():
            dic[word] += 1
        else:
            dic[word] = 1
            
for item in sorted(dic.items(), key = lambda x: (-x[1], -len(x[0]), x[0])):
    print(item[0])
