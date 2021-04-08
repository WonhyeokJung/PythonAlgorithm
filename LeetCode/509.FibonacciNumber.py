# 1. Brute Force Algorithm / 816ms
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)

# 1-1. Brute Force Algorithm / Runtime Error
class Solution:
    def fib(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)

# 2. memoization / 32ms
import collections
class Solution:
    a = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if self.a[n]:
            return self.a[n]

        self.a[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.a[n]  # 함수 실행한 곳에 Return 값

# 2-1. memoization using List / 32ms
class Solution:
    a = [0] * 100001  # 충분히 큰 List 선언

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if self.a[n]:
            return self.a[n]

        self.a[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.a[n]


# 3.Tabulation / 28ms
class Solution:
    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        self.dp[1] = 1

        for i in range(2, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[n]


# 4. Saving memory storage / just 2 variables are used! / 32ms
class Solution:

    def fib(self, n: int) -> int:
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x + y

        return x