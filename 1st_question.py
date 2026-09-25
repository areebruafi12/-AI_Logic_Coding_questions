import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    
    intervals = []
    for _ in range(n):
        start = int(data[idx]); idx += 1
        end = int(data[idx]); idx += 1
        intervals.append((start, end))
    
    intervals.sort()
    
    merged = []
    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    
    out = []
    for start, end in merged:
        out.append(f"{start} {end}")
    
    print("\n".join(out))

main()
