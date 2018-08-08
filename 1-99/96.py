'''
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
'''
#1
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2,n+1):
            for j in range(0,i):
                dp[i] += dp[j]*dp[i-j-1]
        
        print(dp)
        return dp[n]
 
#2
