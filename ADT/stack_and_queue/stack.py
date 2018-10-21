'''
Created on Aug 27, 2018

@author: aavinash
'''


class Stack:
     def __init__(self):
         self.new = []
         self.c= 0
         
         
     def push(self,data):
         self.new.append(data)
         self.c+=1
         
     def pop(self):  
         self.c-=1  
         return self.new.pop()
     
     def is_empty(self):
         if len(self.new) ==1 : return True
         else: False
         
     def display_stack(self): print self.new    
  
  
#
#Queue implementation using stack
#     
     
class Qqueue:
    def __init__(self):
        self.qs = Stack()
        self.c = 0
        
    def dqueue(self):
        s2 = Stack()
        for i in range(self.qs.c-1):
            s2.push(self.qs.pop())
            
        self.qs.pop()    
        
        for i in range(s2.c) :
            self.enqueue(s2.pop()) 
            
        print self.qs.c       
            
            
         
        
        
    def enqueue(self, data):  
        self.qs.push(data) 
          
    def is_empty(self):
        return self.qs.is_empty()  
    
    def display_queue(self): print self.qs.display_stack()   
    
       
     
             
if __name__ == '__main__':
    q1 = Qqueue()
    for i in range(10,100,10):
        q1.enqueue(i)
        
    q1.display_queue() 
    
    q1.dqueue()
    q1.display_queue() 
        
    
    q1.display_queue()       
    

        
        
        
        
        