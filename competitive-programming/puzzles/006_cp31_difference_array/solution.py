import sys

def solve():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    q = int(data[1])

    D = [0] * (n + 2)

    idx = 2
    for _ in range(q):
        l = int(data[idx])
        r = int(data[idx + 1])
        x = int(data[idx + 2])
        idx += 3

        D[l] += x
        if r + 1 <= n:
            D[r + 1] -= x
        
        result = []
        running = 0
    
    for i in range(1, n + 1):
        running += D[i]
        result.append(running)
    
    print(*result)

if __name__ == "__main__":
    solve()