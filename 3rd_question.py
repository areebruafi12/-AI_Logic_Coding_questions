n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

i = 0
j = 0
Carry = 0
result = []

while i < n or j < m or Carry:
    x = a[i] if i < n else 0
    y = b[j] if j < m else 0

    total = x + y + Carry
    result.append(total % 10)
    Carry = total // 10

    i += 1
    j += 1

print(*result)
