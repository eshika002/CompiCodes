n = int(input())
x_data = list(map(int, input().split()))
p = x_data[0]
x_levels = set(x_data[1:])
y_data = list(map(int, input().split()))
q = y_data[0]
y_levels = set(y_data[1:])
all_levels = x_levels | y_levels
if len(all_levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
