'''
Created on Sep 24, 2018

@author: aavinash

link:  https://leetcode.com/problems/same-tree/description/

Similar :   https://leetcode.com/problems/unique-binary-search-trees/description/

To do : To understand   https://leetcode.com/problems/same-tree/discuss/32894/Python-Recursive-solution-and-DFS-Iterative-solution-with-stack-and-BFS-Iterative-solution-with-queue


Possible Combinations ==>

[0,,] [0,,]
[1,2] [1]
[] []
[1,] [1,2,]
[1,,3][1,4,]
[4,5,6][4,5,6]

'''

#Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    
    def isSameTree_1(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree_1(p.left, q.left) and self.isSameTree_1(p.right, q.right)
        return p is q
    
    
        
    def isSameTree_2(self, p, q):
        def t(n):
            return n and (n.val, t(n.left), t(n.right))
        return t(p) == t(q)        
      
    def v(self, n):
            return n and [n.val, self.v(n.left), self.v(n.right)] 
        
               


if __name__ == '__main__':
    a1 = TreeNode(12)
    a1_lt = TreeNode(10)
    a1_rt = TreeNode(56)
    a1.right = a1_rt
    a1.left =a1_lt
    
    a2=TreeNode(12)
    
    a2_rt = TreeNode(56)
    a2_lt = TreeNode(10)
    a2.right = a2_rt
    a2.left = a2_lt
    
    obj = Solution()
    print obj.isSameTree_1(a1, a2)
    
    print obj.v(a1);print obj.v(a2)
    
    
    
        