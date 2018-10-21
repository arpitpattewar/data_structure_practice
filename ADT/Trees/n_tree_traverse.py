'''
Created on Sep 30, 2018

@author: aavinash
'''


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
                
    def preorder(self, root):
        if root:
            l=[]
            l.append(root.val)
            for  i in root.children:
                if i.children:
                    l=l+self.preorder(i)
                else:
                    l.append(i.val)
            return l
        else:
            return []           
        
    def preorder_1(self, root):
        if root:
            l=[]
            l.append(root.val)
            for  i in root.children:
                if i.children:
                    while True:
                        
                else:
                    l.append(i.val)
            return l
        else:
            return []  


if __name__ == '__main__':
    
    
    b=Node(2,[])
    
    d=Node(4,[])
    
    f=Node(6,[])
    g=Node(7,[])
    
    e=Node(5,[d,g,f])
    c=Node(3,[e])
    a=Node(1,[ b,c])
    
    

    obj = Solution()
    print obj.preorder_1(a)
    
    
    