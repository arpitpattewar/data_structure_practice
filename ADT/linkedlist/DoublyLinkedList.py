'''
Created on Dec 3, 2017

@author: aavinash
'''


class node:
    def __init__(self, data, nxt=None, prv=None):

        self.data = data
        self.nxt = nxt
        self.prv = prv
        
        
        

class DoublyLinkedList(object):
    '''
    classdocs
    '''


    def __init__(self, data, nxt=None, prv=None):
        '''
        Constructor
        '''
        self.head = node(data) 

        
    def addnode(self, data):
        head = self.head
        while True:
            if head.nxt:
                head = head.nxt
            else:
                head.nxt = node(data, prv=head)   
                print "datanode {} Successfullt added".format(data)
                break
                
    def display(self):
        head = self.head
        while True:
            if head.nxt:
                if head.prv : print "Current node {}, prev node {}, next node {}".format(head.data, head.prv.data, head.nxt.data)
                if not  head.prv : print "head node {}  next node {}".format(head.data,  head.nxt.data)
                head = head.nxt
            else:
                print "Lastnode {} prev node {}".format(head.data, head.prv.data)
                break 
            
            
            
            
if __name__ == '__main__':
    
    dl1 = DoublyLinkedList(12)
    dl1.addnode(13)
    dl1.addnode(15)
    dl1.addnode(17)
    dl1.addnode(19)
    dl1.display()
    
                        
                     
                    
        
        