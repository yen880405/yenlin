class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or len(s) == 0 or s[0] == '0':
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[0], dp[1] = 1, 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp[i + 1] += dp[i - 1]
                else:
                    return 0
            else:
                dp[i + 1] += dp[i]
                if 10 < int(s[i - 1 : i + 1]) <= 26:
                    dp[i + 1] += dp[i - 1]
        return dp[-1]
