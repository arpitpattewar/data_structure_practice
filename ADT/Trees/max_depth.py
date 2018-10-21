'''
Created on Sep 29, 2018

@author: aavinash
link : https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #print root.val
        if root:
            if not root.left and not root.right : return 1
            else: return max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right))
        else: return 0
        
        
        
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            if not root.left and not root.right : return 1
            return min(map( lambda x : x>1, [1+self.minDepth(root.left), 1+self.minDepth(root.right)]) )
        else: return 0  
        
        

        
                
        
       


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
    '''
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
    '''
    obj = Solution()
    #print obj.maxDepth(a1)
    

    print obj.minDepth(None)
    print obj.maxDepth(None) 
    