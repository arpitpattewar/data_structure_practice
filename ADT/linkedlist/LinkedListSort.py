'''
Created on Mar 15, 2018

@author: aavinash
'''


class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
        

class LinkedList(object):
    '''
    classdocs
    '''


    def __init__(self,head=None):
        '''
        Constructor
        '''
        self.head=head
        
    def add_node(self, node):
        head =self.head
        if self.head :
            while True:
                if head.next:
                    head = head.next
                else:
                    head.next = node 
                    break   
        else:
            self.head = node
            
            
            
                    
        