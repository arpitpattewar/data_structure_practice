'''
Created on Mar 22, 2018

@author: aavinash
'''

import sys
import Queue
#from  ADT.linkedlist import *
sys.path.append('/Users/aavinash/personal_github_repo/data_structure_practice/ADT/linkedlist')
import linkedlist


 


#sys.path.append('/Users/aavinash/personal_github_repo/data_structure_practice/ADT/linkedlist')


class node:
    def __init__(self, data=None):
        self.data = data
        self.leftnode = None
        self.rightnode = None
        self.next=None
        

class tree:
    def __init__(self, rootnode=None):
        self.rootnode = rootnode
        self.ht = 0
        self.size = 1
        
        
    def rec_insert(self, new_node, headnode=None): 
        if not self.rootnode: self.rootnode = new_node
        else:
            if not headnode : head = self.rootnode 
            else : head= headnode
            
            if new_node.data <= head.data : 
                if head.leftnode:
                    self.rec_insert(new_node, head.leftnode)
                else:
                    print """
                           {}
                         /
                        {} 
                         """.format(head.data,new_node.data)                    
                    head.leftnode = new_node
                    self.size+=1
            
            else:
                if head.rightnode:
                    self.rec_insert(new_node, head.rightnode)
                else:
                    print """
                     {}
                       \    
                        {} 
                         """.format(head.data,new_node.data)                      
                    head.rightnode = new_node
                    self.size+=1
                    
                        
    
    def insert(self, new_node):
        if not self.rootnode: self.rootnode = new_node
        else:  
            root = self.rootnode
            ht=0
            while True:
                if new_node.data < root.data:
                    ht+=1
                    if root.leftnode:
                        
                        root = root.leftnode
                    else:
                         root.leftnode = new_node  
                         
                         print "Adding to left of {} , new_node {} ".format(root.data,new_node.data) 
                         print """
                           {}
                         //
                        {} 
                         """.format(root.data,new_node.data)
                         self.size+=1
                         if ht >= self.ht : self.ht=ht 
                         break
                else:
                    ht+=1
                    if root.rightnode:
                        
                        root = root.rightnode
                    else:
                        root.rightnode = new_node
                        
                        print "Adding to right of {} , new_node {} ".format(root.data,new_node.data) 
                        print """
                           {}
                             \\
                               {}
                        """.format(root.data,new_node.data) 
                        #print self.size
                        self.size+=1
                        if ht >= self.ht : self.ht=ht 
                        break
                    
                    
    def search(self, data):
        if not self.rootnode: return "Not found"
        else:
            root = self.rootnode
            counter=0
            while True:
                counter+=1
                if data < root.data:
                    if root.leftnode: root = root.leftnode
                    else: print "Not found";break
                if data > root.data:    
                    if root.rightnode : root = root.rightnode
                    else: print "Not found";break
                if data == root.data:
                    print "Found"
                    print counter;break
                    
                    
    def rec_search(self, data, head=None):
        if not self.rootnode: return "Not found"
        if not head : head= self.rootnode
        print head.data
        if head.data == data:
            return "Found"
        if data > head.data:
            if head.rightnode:
                return self.rec_search(data, head.rightnode)
            else:
                return "Number not found"
        if data < head.data:
            if head.leftnode:
                return self.rec_search(data, head.leftnode)
            else:
                return "Number not found"            
                    
                
            
        
                            
                    
    def is_tree_empty(self):   return True if not self.rootnode else False           
                    
                    
    def remove(self, data):
        if self.is_tree_empty(): print "It is empty Tree"
        else:
            root = self.rootnode
            while True:

                if  root.data > data:
                    if root.leftnode: 
                        prev = root
                        root = root.leftnode
                    else: print "Not found";break
                if data > root.data:    
                    if root.rightnode :
                         prev = root
                         root = root.rightnode
                    else: print "Not found";break
                if data == root.data:
                    
                    if root.leftnode and root.rightnode:
                        pass
                    elif root.leftnode:
                        print "Found"
                        prev.leftnode = root.leftnode  ;break                      
                    else :
                        print "Found"
                        prev.rightnode = root.rightnode;break
                    #del root  
                    
                    
    
                    
                      
    #Inorder Recursive traversal
    def rec_traverse(self, root=None):
        if not root : root = self.rootnode

        if root.leftnode:
            self.rec_traverse(root.leftnode)
            print root.data
            if root.rightnode:
                self.rec_traverse(root.rightnode)
        else: 
            print  root.data    
            if root.rightnode:
                self.rec_traverse(root.rightnode)
                
                        
                
    def delete_node(self, data):
        if self.is_tree_empty(): print "It is empty Tree"
        else:
            root = self.rootnode
            counter=0
            while True:
                counter+=1
                if data < root.data:
                    if root.leftnode: root = root.leftnode
                    else: print "Not found";break
                if data > root.data:    
                    if root.rightnode : root = root.rightnode
                    else: print "Not found";break
                if data == root.data:
                    print "Found"
                    print 
     
    def find_special(self, nature, head =None):
        if not head : head = self.rootnode
        if self.is_tree_empty(): print "It is empty Tree"
        
        else:
            if nature == "min":
                while True:
                    if head.rightnode:
                        head = head.rightnode
                    else:
                        return  head.data  
                        break 
              
            else:
                while True:
                    if head.leftnode:
                        head =head.leftnode
                    else:
                        return head.data
                        break    
                        

                
    def get_leaf_nodes_rec(self, headnode=None):
        if not headnode and  self.is_tree_empty() : return None
        elif headnode: head  = headnode
        else:head = self.rootnode
        
        if head.leftnode or head.rightnode: 
            if head.leftnode:
                self.get_leaf_nodes_rec(head.leftnode)
                
            if head.rightnode:
                self.get_leaf_nodes_rec(head.rightnode)                 
        else:
            print head.data
            
            
            
                
    def get_leaf_nodes_count(self, headnode=None):
        if not headnode and  self.is_tree_empty() : return None
        elif headnode: head  = headnode
        else:head = self.rootnode
        
        c=0
        if head.leftnode or head.rightnode: 
            if head.leftnode:
                c= c + self.get_leaf_nodes_count(head.leftnode)
            if head.rightnode:
               c = c + self.get_leaf_nodes_count(head.rightnode)                 
        else:
            c+=1
        return c
    
    
    
    def get_height_of_tree(self):
        if self.is_tree_empty() : return None
        else: head = self.rootnode
        left = head.leftnode
        right = head.rightnode

        ht=0
        while left or right: 
            ht+=1
            if left:
                left = left.leftnode 
            if right:
                right = right.rightnode                 
        return ht 
    
    

        
    

    def bredth_first_traversal(self):
        if self.is_tree_empty(): print "Tree is empty"
        else:
            temp = self.rootnode
            pque = linkedlist.Linkedlist() 
        
            while temp:
                print temp.data
                if temp.leftnode:
                    pque.add_node(temp.leftnode)  
                if temp.rightnode:
                    pque.add_node(temp.rightnode)  
                temp= pque.dequeue()
                
                
    def get_given_level(self, root, level):
        if  not root: print "Tree is empty"
        if level == 1 : print  root.data
        else:
            if root.leftnode:
                self.get_given_level(root.leftnode, level-1)
            if root.rightnode:
                self.get_given_level(root.rightnode, level-1) 
            
                            
                
                
    def get_element_at_height(self, height):       
        if self.is_tree_empty(): print "Tree is empty"
        else:
            temp = self.rootnode
            pque = linkedlist.Linkedlist() 
            ht=0
            c=0
            while temp:
                
                print "{}:{}".format(ht,temp.data)
                if temp.leftnode:
                    pque.add_node(temp.leftnode)  
                    c+=1
                if temp.rightnode:
                    pque.add_node(temp.rightnode)  
                    c+=1
                print "We have found {} element at ht {}".format(c,ht)    
                temp= pque.dequeue()                                
                
                


            

if __name__ == '__main__':
  t1=tree()  
  w=range(20,400,4)
  import random
  t=random.shuffle(w)

  for i in [50,45,55,12,47,59,54,3,56,42,7,76,8,19]:
      t1.insert(node(i))

      #t1.insert(node(i))
      #print "height is {}".format(t1.ht)
  print "Size of the binary tree is :: {} ".format(t1.size)    
  data=50 

  #print "Result of number search {} is {}".format(data, t1.rec_search(data))    
      
  print "Result of tree traversal is \n\n "    
  t1.rec_traverse()
  
 # print "max is {}".format(t1.find_special("max"))
  #print "min is {}".format(t1.find_special("min"))

  
  '''
  print "\n\n print all leaf nodes"
  t1.get_leaf_nodes_rec()
  
  print "\n\ total number of leaf node"
  print t1.get_leaf_nodes_count()
  
  print "\nHeight of the tree is "
  print t1.get_height_of_tree()
  print t1.ht

    
  print "Bredth firdt traversal results "
  t1.bredth_first_traversal()  
  '''
  

  level =4
  for i in range(1,level+1):
      print "get element at level {}".format(i)
      t1.get_given_level(t1.rootnode, i)
  
  


  #t1.get_leaf_nodes()
  #print t1.find_special("max")
  

  
  
  
      
  