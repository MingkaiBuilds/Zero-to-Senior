import sys

def solve():
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    nums = list(map(int, data[1:n+1]))

    seen = set()

    for num in nums:
        if num in seen:
            print("YES")
            return
        seen.add(num)
    

    print("NO")
    return

if __name__ == "__main__":
    solve()