
## Problem1 Remove Invalid Parentheses

# (https://leetcode.com/problems/remove-invalid-parentheses/)



class Solution:
    def find_minimum_brackets_to_remove(self, s):
        stack = []
        count = 0
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                if len(stack) == 0:
                    count += 1
                elif stack[-1] == "(":
                    stack.pop()
                elif stack[-1] == ")":
                    count += 2
                    
        return count + len(stack)
    
    def isValid(self, s):
        return self.find_minimum_brackets_to_remove(s) == 0
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        min_invalid_paran = self.find_minimum_brackets_to_remove(s)
        
        def para_recur(s, n, idx, to_leave, curr, output):
            if idx >= n and to_leave == 0:
                if self.isValid( "".join(curr) ):
                    output.append( "".join(curr) )
                return
            elif idx >= n:
                return
            
            if s[idx] == "(" or s[idx] == ")":
                
                para_recur(s, n, idx + 1, to_leave - 1, curr, output)
                
                curr.append( s[idx] )
                para_recur(s, n, idx + 1, to_leave, curr, output)
                curr.pop()
            else:
                curr.append( s[idx] )
                para_recur(s, n, idx + 1, to_leave, curr, output)
                curr.pop()
        output = []
        para_recur(s, n, 0, min_invalid_paran, [], output)
        
        d = {}
        for string in output:
            if string not in d:
                d[string] = 1
        return [ k  for k in d.keys() ]
