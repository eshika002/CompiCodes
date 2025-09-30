d = int(input())
results = []
for i in range(d):
    a, b = map(int, input().split())
    moves = (b - a % b) % b
    results.append(moves)
for r in results:
    print(r)
