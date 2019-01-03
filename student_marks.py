n = int(input())
dict= {}
for lehsun in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    dict[name] = scores
    query_name = input()
print(dict)
