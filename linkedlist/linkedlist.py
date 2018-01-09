#python2
#
#link  :  http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
#
#link  :  https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/
#


import sys


class node:
   def __init__(self, data=None):
    self.data=data
    self.next=None


class linkedlist:
    
     def __init__(self,data=None):
       self.head=node(data)
       self.head.next=None
       
     def addnode(self, data):
       if self.isempty() : self.head=node(data)   
       else: 
           head = self.head
           while head:
               if head.next : head = head.next
               else :
                   print "adding {}".format(data) 
                   head.next=node(data)
                   break
         
     def display(self):
       head = self.head
       if  not self.isempty():
           while head :
               print head.data
               if  head.next : head = head.next
               else: break
       else: print "Empty linkedlist"
                   
         
     def addnext(self,source_data,new_data):
       head=self.head
       while head:
          flag=0
          if head.data == source_data :
              old_next=head.next
              head.next=node(new_data)
              new_next=head.next
              new_next.next=old_next
              flag=1
              break
          else: head=head.next    
       if flag==0 : print "Element %s is not part of the linkedlist"%(source_data)
       
     def addbefore(self,source_data,):  
         pass
     
     def isempty(self):
         return  self.head == None

     
     def pop(self):
        head = self.head
        prev=None
        while head:
            #prev=head
            if head.next:
                prev=head
                head=head.next   
            else : 
                if prev : prev.next=None
                else: self.head=None
                return head.data 
                break
            
            
     
     def reverse(self):

         cur= self.head
         prev=None
         next_node=cur.next
         while cur.next:
             '''
             print "Cur is  {}".format(cur.data)
             try:
                 print "Prev is  {}".format(prev.data)
             except: pass
             '''    
             cur.next = prev
             prev=cur            
             cur = next_node
             next_node = cur.next
         cur.next = prev
         self.head=cur
         
             
         

             
                      
                   

  

if __name__ == '__main__':
    
    l1=linkedlist(1)
    l1.addnode(2)
    l1.display()
    #l1.addnode(3)
    #l1.addnode(4)
    #l1.addnode(5)
    #l1.display()
    #l1.addnext(2,2.5)       
    #l1.display() 
    '''
    print " poping"
    l1.pop();
    l1.display();
    l1.pop()
    
    print "list after pop" 
    l1.display()
    '''
    
    print "Reversing the linkedlist"
    l1.reverse()
    print "List shall get reverse"
    l1.display()
    l1.addnode(0)
    l1.display()
    l1.reverse()
    l1.display()

    
    
    round_l="("
    round_r=")"
    square_r="]"
    square_l="[" 
    curly_l="{"
    curly_r="}"
    
    '''
    input=sys.argv[1]

    parse_control=linkedlist()
    for i in range(len(input)):
        parse_control.display()
        #parse_control.addnode(input[i])
        #parse_control.display()
        if input[i] in ["{","[","("] : parse_control.addnode(input[i])
        if input[i] in ["}","]",")"]:
            last=parse_control.pop()
            #print last
            
            if (last== "["  and input[i] !="]"  ) : 
                print i+1
                break    
            if (last == "(" and  input[i]!=")" ):
                print i+1
                break
            if (last == "{" and input[i]!="}"):
                print i+1
                break
    if parse_control.isempty() : print "Success"
    #else: print i+1        
    '''             
             
    
              



