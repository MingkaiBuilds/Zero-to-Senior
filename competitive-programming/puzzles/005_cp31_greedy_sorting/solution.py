import sys

def solve():
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    nums = list(map(int, data[1:n+1]))

    nums.sort()

    k = 0
    window_sum = 0

    for x in nums:
        if window_sum + x <= k + 1:
            window_sum += x
            k += 1
    
    print(k)

if __name__ == "__main__":
    solve()

