'''
Created on Sep 26, 2018

@author: aavinash

link:  https://leetcode.com/problems/symmetric-tree/description/

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        print "left = {}".format(self.preorder(root.left))
        print self.rtpreorder(root.right)
        return self.preorder(root.left) == self.rtpreorder(root.right) if root else False
        
        
        
    def preorder(self, nd):
        l=[nd.val if nd else None] 
        
        if nd:
            l=l+self.preorder(nd.left)
            l=l+self.preorder(nd.right)
        return l
        
        
    def rtpreorder(self,nd): 
        l=[nd.val if nd else None] 
        
        if nd: 
            l=l+self.rtpreorder(nd.right)
            l=l+self.rtpreorder(nd.left)
        return l
        
        

        
        
        
        
        
if __name__ == '__main__':
    
    a1 = TreeNode(2)
    a1_lt = TreeNode(3)
    a1_rt = TreeNode(3)
    
    a1.right = a1_rt
    a1.left =a1_lt  
    
    c = TreeNode(4)
    d = TreeNode(5)
    
    e = TreeNode(5)
    f= TreeNode(4)
    
    a1.left.left = c
    a1.left.right = d
    
    
    a1.right.left = e
    a1.right.right = f
    
    g=TreeNode(8)
    h=TreeNode(9)
    i=TreeNode(8)
    j=TreeNode(9)
    
    a1.left.right.left=g
    a1.left.right.right=h
    
    a1.right.left.left = j
    a1.right.left.right = i
    
    

    #a1_lt.right=TreeNode(None)
    
    
      
    
    t1=[1,2,2,3,4,4,3]
    t2=[1,2,2,None,3,None,3]
    t3=[2,3,3,4,5,5,4,None,None,8,9,9,8]
    
    
#     r = TreeNode(t3[0])
#     for i in len(0,range(t3)/2):
#         if i
        
        
    
    obj = Solution()
    print obj.isSymmetric(a1)
    
    
            