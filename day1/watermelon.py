n=int(input())
possible=False
for i in range(2,n,2):
    remaining= n-i
    if remaining%2==0:
        print("YES")
        possible=True
        break
if not possible:
        print("NO")
        
