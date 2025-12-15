import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    window_sum = sum(arr[:k])
    best_sum = window_sum
    best_L = 0   

    for L in range(1, n - k + 1):
        window_sum += arr[L + k - 1]   
        window_sum -= arr[L - 1]       

        if window_sum < best_sum:
            best_sum = window_sum
            best_L = L

    print(best_L + 1)
