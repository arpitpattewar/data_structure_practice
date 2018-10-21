'''
Created on Dec 17, 2017

@author: aavinash
'''





class node():
    def __init__(self, data, nxt=None, prv=None):
        self.data = data
        self.nxt = nxt
        self.prv = prv
        
    def setnxt(self, data):
        self.nxt = node(data)
        
    def setprv(self, data):
        self.prv = node(data)
        
    def getnxt(self):
        return self.nxt
        
    def getprv(self):
        return self.prv
    
    def getdata(self):
        return self.data
                
                     
        

class NewDoublyLinkedList(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.head = None   
        self.counter = 0 
        
        
    def push(self, data):
        new_node = node(data)
        new_node.nxt = self.head
        if self.head :
            self.head.prv = new_node
        self.head = new_node    
        
    def append(self, data):  
        
        new_node = node(data)
        
        head = self.head
        
        if not head:
            self.head = new_node
            return 
        
        while head:
            if head.nxt : 
                head = head.nxt
            else:
                head.nxt = node(data)
                head.prv = new_node
                return
                
                

    def display(self):
        head = self.head  
        while head :
            print head.data  
            if head.getnxt() :
                head =  head.getnxt()
                self.counter += 1 
            else:
                return
            
    def insertafter(self, prev_node, data):
        head = self.head
        new_node = node(data)
                
        while head:
            #print "hi"
            print head.data
            if head.data == prev_node.data :
                tmp = head.nxt
                
                head.nxt = new_node
                new_node.prv = head
                
                new_node.nxt = tmp
                tmp.prv = new_node
                return
            else:
                if head.nxt : 
                    head = head.nxt  
                else: return    
                
    
    def isCyclic(self):
        head = self.head
        pt1=head
        pt2=head.nxt
                     
                     
                

            


if __name__ == '__main__':
    
    obj =  NewDoublyLinkedList()
    obj.append(1)
    obj.display()
    obj.append(2)
    obj.append(3)
    obj.append(4)
    obj.append(5)
    obj.push(11)
    obj.push(10)
    obj.append
    #obj.insetafter(None,45)
    print "obj.head.nxt.nxt.data is {}".format(obj.head.nxt.nxt.nxt.nxt.data)
    obj.insertafter(prev_node=obj.head.nxt.nxt.nxt, data=56)
    obj.display()
    
    
                
            
        