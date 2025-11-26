import sys


def solve():
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])
    nums = list(map(int, data[1:n+1]))

    seen = set()

    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + nums[i - 1]
    
    for val in pref:
        if val in seen:
            print("YES")
            return
        seen.add(val)
    
    print("NO")
    return


if __name__ == "__main__":
    solve()
