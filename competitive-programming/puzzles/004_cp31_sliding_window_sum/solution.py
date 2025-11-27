import sys

def solve():
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    s = int(data[1])
    nums = list(map(int, data[2:n+2]))

    max_len = 0
    window_sum = 0
    l = 0
    for r in range(n):
        window_sum += nums[r]
        
        while window_sum > s:
            window_sum -= nums[l]
            l += 1
        
        max_len = max(max_len, r - l + 1)
    
    print(max_len)

if __name__ == "__main__":
    solve()
