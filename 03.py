'''
无重复字符的最长子串

给定一个字符串，找出不含有重复字符的最长子串的长度。

示例：

给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。

给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。

给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。

'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        D = {}
        max_len = 0
        start = 0
        
        for idx, item in enumerate(s):
            if item in D and start <= D[item]:
                start = D[item]+1
            else:
                 max_len = max(idx-start+1, max_len)
            
            D[item] = idx
        return max_len
