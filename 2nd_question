from collections import deque

n = int(input())
a = list(map(int, input().split()))
k = int(input())

max_dq = deque()
min_dq = deque()

left = 0
best_len = 0
best_start = 0

for right in range(n):
    while max_dq and a[max_dq[-1]] <= a[right]:
        max_dq.pop()
    max_dq.append(right)

    while min_dq and a[min_dq[-1]] >= a[right]:
        min_dq.pop()
    min_dq.append(right)

    while a[max_dq[0]] - a[min_dq[0]] > k:
        if max_dq[0] == left:
            max_dq.popleft()
        if min_dq[0] == left:
            min_dq.popleft()
        left += 1

    length = right - left + 1

    if length > best_len:
        best_len = length
        best_start = left + 1

print(best_len, best_start)
