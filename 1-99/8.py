'''
 字符串转整数 (atoi)

'''
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        ls = list(str.strip())
        if len(ls)==0: 
            return 0
        sign = -1 if ls[0]== '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        
        ret,i = 0,0
        
        while i < len(ls) and ls[i].isdigit():
            ret = ret*10 + int(ls[i])
            
            i += 1
        return max(-2**31, min(sign*ret, 2**31-1))
