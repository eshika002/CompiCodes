t = int(input())
target = "codeforces"
for _ in range(t):
    c = input().strip()
    if c in target:
        print("YES")
    else:
        print("NO")
