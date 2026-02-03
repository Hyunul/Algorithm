import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(set(arr))

comp = {}
for i in range(len(sorted_arr)):
    comp[sorted_arr[i]] = i

result = []
for x in arr:
    result.append(str(comp[x]))
    
print(" ".join(result))