def fib(n: int) -> int:
    dp = [0] * (n + 1)
    return rec(n, dp)

def rec(n , dp):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    elif dp[n - 1] == 0 :
        dp[n - 1] = rec(n - 1, dp) + rec(n - 2, dp)
        
    return dp[n - 1]
    