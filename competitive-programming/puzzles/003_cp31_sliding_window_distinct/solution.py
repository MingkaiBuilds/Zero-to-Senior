import sys

def solve():
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    nums = list(map(int, data[1:n+1]))
    max_len = 0

    seen = set()

    l = 0
    for r in range(n):
        while nums[r] in seen:
            seen.remove(nums[l])
            l += 1
        seen.add(nums[r])
        max_len = max(max_len, r - l + 1)
    
    print(max_len)

if __name__ == "__main__":
    solve()

    