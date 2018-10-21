'''
Created on Sep 20, 2018

@author: aavinash
'''

class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        

class dtree(object):
    '''
    classdocs
    '''


    def __init__(self, root=None):
        '''
        Constructor
        '''
        self.root = root
        self.counter = 0
        if self.root : self.counter+=1
        
            
    def insert(self, num): 
        if  self.counter < 1 : 
            self.root=num
            self.counter+=1
        else:    
            head = self.root
            while head:
                if num.data >= head.data : 
                    if head.right : head = head.right
                    else : 
                        head.right = num;
                        print """  
                                  {}
                                    \\
                                     {} """.format(head.data,head.right.data)                        
                        #print head.data,head.right.data
                        self.counter+=1
                        break
                else:
                    if head.left : head = head.left
                    else : 
                        head.left = num
                        print """  
                                  {}
                                 / 
                                {} """.format(head.data,head.left.data)
                        self.counter+=1
                        break 
                      
          
          
    ###########################
    #                         #   
    #   R E C U R S I V E     #
    #                         #   
    ###########################                      
                    
    def height(self, head=None ):
        if not head : head= self.root
        
        hl,hr=0,0
        #if not head.left and head.right : return -1
        if head.left : hl=hl +1 + self.height(head.left)
        if head.right : hr=hr+1 + self.height(head.right)
        return max(hr,hl)
    

        
    def display_leaves(self, head=None):
        l=[]
        
        if not head : head= self.root
        if head.left :  l=l+self.display_leaves(head.left)
        if head.right :  l=l+self.display_leaves(head.right)
        if not head.left and not head.right : l.append(head.data)
        return   l
    
    
    def countNodes(self, head=None):
        if not head : head= self.root
        a=self.display_leaves(head)
        print a
        return len(a) if head else None    
    
    
    def sort_tree(self,nd=None,max=0):
        if not nd : nd = self.root
        if nd.left : 
            if nd.data == nd.left.data: 
                max+=1
                self.sort_tree(nd.left,max)
            else:
                max=1
                self.sort_tree(nd.left, max)
            print max        
        else:
            print nd.data,max
            
        if nd.right : 
            self.sort_tree(nd.right)
    
    
    def sort_tree_rec(self, nd=None):
        """
        Inorder traversal
        Left-Root-Right
        """
        l=[]
        if not nd : nd = self.root
        
        if nd.left : l=l+self.sort_tree_rec(nd.left)
        l.append(nd.data)
        if nd.right : l=l+self.sort_tree_rec(nd.right)
        return l
    
        
    def preorder_traversal_rec(self, nd=None):
        """
        Pre-order traversal
        Root-Left-Right
        """
        l=[]
        if not nd : nd = self.root
        
        l.append(nd.data) 
        if nd.left :  l=l+self.preorder_traversal_rec(nd.left)
        if nd.right : l=l+self.preorder_traversal_rec(nd.right)
        return l
    
        
    def postorder_traversal_rec(self, nd=None):
        """
        Postorder traversal
        LtRtRoot
        """
        l=[]
        if not nd : nd = self.root
        
        if nd.left : l=l+self.postorder_traversal_rec(nd.left)
        if nd.right : l=l+self.postorder_traversal_rec(nd.right) 
        l.append(nd.data)
        return l               
          
          
    ###########################
    #                         #   
    #        ITERATIVE        #
    #                         #   
    ###########################          
    def sort_tree_while(self):
        """
        Inorder traversal
        """   
        
        stack=[self.root] 
        head = self.root
        
        while stack:
                #print [ i.data for i in stack]
                if head.left:    
                    head = head.left
                    stack.append(head)
                else:
                    last = stack.pop()
                    print last.data
                    if last.right: 
                        head = last.right
                        stack.append(last.right)
                        
    def bredth_first_traversal(self):
        stack = [] 
        head = self.root
        if head.left: stack.append(head.left)
        if head.right: stack.append(head.right)
        
        while stack:
            for i in stack:
                print i.val
                
            
            
        
        
            
                                    

      
                
    def compare_trees(self, t1, t2):
        return t1.sort_tree_rec( ) == t2.sort_tree_rec()            

        
        
    
 
if __name__ == '__main__':
     t1 = dtree()

     s=[12,3,4,32,2,56,31,0,-90,-8,-8,-5,122,-8]
     s=[-1,-1,-1]

     for i in s: t1.insert(node(i))
     #print t1.display_leaves()
     
     '''
     print "In-order traversal \n "
     print t1.sort_tree_rec()
     
     print "Pre-order traversal \n "
     print t1.preorder_traversal_rec()
     
     print "\n Post-order traversal"
     print t1.postorder_traversal_rec()                               
     '''
         
     #print t1.height() 
     #t1.sort_tree_while() 
     t1.sort_tree()
     print t1.display_leaves()
     print t1.countNodes()
     

     


                      
                        
                    
                        
            
      
        
        