import sys

def solve():
    data = sys.stdin.read().strip().split()
    # data[0] = N
    # data[1:N+1] = numbers
    # data[N+1] = T
    
    n = int(data[0])
    nums = list(map(int, data[1:n+1]))
    t = int(data[n+1])

    seen = set()

    for num in nums:
        if t - num in seen:
            print("YES")
            return
        seen.add(num)
    
    print("NO")
    return

if __name__ == "__main__":
    solve()
