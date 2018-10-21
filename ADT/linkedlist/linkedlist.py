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


class Linkedlist:
    
     def __init__(self, data=None):
       if data:
         self.head=node(data)
       else:
        self.head=None   
                
       #self.head.next=None
       if not data : self.counter=0
       else: self.counter =1
       
       
     def is_empty_linkedlist(self):
         if  self.head : return True
         else : return False 
       
     def addnode(self, data):
       if self.isempty() :
           print "Adding head node {}".format(data) 
           self.head=node(data)   
       else: 
           head = self.head
           while head:
               if head.next : head = head.next
               else :
                   print "adding {}".format(data) 
                   head.next=node(data)
                   self.counter+=1
                   break


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
                   
         
     def display(self):
       head = self.head
       if  not self.isempty() and self.isLoopExistUsingCounter():
           while head :
               print head.data
               if  head.next : head = head.next
               else: break
       else: print "Empty linkedlist or loop exists"
                   
         
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
                if prev : 
                    prev.next=None
                else: 
                    self.head=None
                break
        return head.data if head else None   
            
     
     def reverse(self):
         cur= self.head
         prev=None
         next_node=cur.next
         while cur.next:
             cur.next = prev
             prev=cur            
             cur = next_node
             next_node = cur.next
         cur.next = prev
         self.head=cur
         
         
         
     def rec_reverse(self, cur=None):
         if not cur : cur =self.head
         prev=None
         next_node=cur.next
         if  cur.next:
             print cur.data
             cur.next = prev
             prev=cur            
             cur = next_node
             #next_node = cur.next
             
             self.rec_reverse(cur).next = self.rec_reverse(cur)
         else:    
             #cur.next = prev
             self.head=cur
             return  self.head
         
         
         
     def getMiddleElement_conter(self):
        head = self.head
        if self.counter%2 == 0 :
            print "even"
            middle_index = self.counter/2
        else:
            print "odd"
            middle_index = self.counter/2 + 1
        c=1 
        while  c != middle_index and head.next:
                c+=1
                head = head.next   
        return head.data        
    
    
     def getMiddleElement_next(self):
         start=self.head
         greedy=self.head
         while greedy.next and start :
             greedy = greedy.next.next
             if not greedy : break
             start=start.next
         return  start.data  
     
            
             
     def removeDuplicatesUnsorted2Loops(self):
         #In progress
         head=self.head
         prev=self.head
         while head:
            inner_head=self.head
            while inner_head:
                if inner_head != head and inner_head.data == head.data:
                    new_current = inner_head.next
                    prev.next = new_current
                    inner_head = new_current
                else:
                    prev = inner_head
                    if inner_head.next :
                        inner_head=inner_head.next
                    else:   
                        break
            if head.next: head=head.next
            else:break 
            
            
            
     def mergeSortedLinkedList(self,l2):
         tmp_list = linkedlist()
         tmp_list.head=None

         while True:
             #tmp_list.display()
             if  tmp_list.head:
                if self.head and  l2.head:
                    if self.head.data >= l2.head.data:
                        tmp_list.add_node(l2.dequeue())
                    else:
                        tmp_list.add_node(self.dequeue())
                            
                elif   self.head:
                    c=self.head
                    head_tmp=tmp_list.head
                    while head_tmp:
                        if head_tmp.next:
                            head_tmp=head_tmp.next
                        else:
                              head_tmp.next=c
                              self.head=None
                              break
                              #tmp_list.display()
                              
                                
                elif   l2.head:
                    c=l2.head
                    head_tmp=tmp_list.l2.head
                    while head_tmp:
                        if head_tmp.next:
                            head_tmp=head_tmp.next
                        else:
                              head_tmp.next=c
                              l2.head=None  
                              break
                              #tmp_list.display()
                              
                else :
                    print "break" 
                    break          
                              
             else:    
                 if self.head.data > l2.head.data :
                     tmp_list.head = l2.dequeue()
                     

                 else:
                     tmp_list.head = self.dequeue() 
                     
         return  tmp_list              

                 
             
             

             
             
             
     def dequeue(self):
         head = self.head
         if head:
             if head.next:
                 current = self.head
                 self.head = head.next
                 current.next=None
                 return current
             else:
                 self.head=None
                 return head    
             
             
     def ifPalimdrom(self):
         first= self.dequeue() 
         last=self.pop()
         while  first and last:
             print first, last
             if first == last :
                 first= self.dequeue() 
                 last=self.pop()
                 continue
             else:
                 return False
                 
         return True 
     
     
     
     def rotateLinkedList(self, num):
         '''
         in progress
         '''
         old_head=self.head
         head = self.head
         new_head=None
         c=0
         while head:
             cur=head
             if head.next : 
                 head = head.next
                 c+=1

             if c==num:
                 new_head = head
                 cur.next=None
                 
                 
     def formLoop(self):
         head=self.head
         while True:
             if head.next : head= head.next
             else:
                 print "loop is formed, be careful now"
                 break
         head.next = self.head  
         
         
     def isLoopExistUsingCounter(self):
         head=self.head
         c=1
         while c <= self.counter:
             #print c
             if head.next:
                 head =head.next
                 c+=1
             else:
                 break  
         if c > self.counter : return  "loop exists"
         else: return "No loop"  
         
      
     def isLoopExistsUsing2Pointers(self):
         first=self.head
         second=self.head.next
         while True:
             
             if  first.next:
                 first=  first.next
             else:
                 print "No loop"
                 break
             if second.next.next  :
                 second=second.next.next    
             else:
                 print "No loop"
                 break
             #print 'first={}, second={}'.format(first.data,second.data)
             if first == second:
                 print "loop exists"
                 break    
                 
                 
     def removeLoop(self):
         if self.isLoopExistUsingCounter() == 'loop exists':
             head=self.head
             c=1
             while True :
                head=head.next
                print head.data,c
                c+=1
                if  c == self.counter:
                    
                    head.next = None
                    print "Loop successfully removed"
                    break
         else: print "There is no loop in linked list"       
                     
     def flattenLinkedList(self):   
         pass   
                     
                  
             
                     
                       
     
               
                              
  

if __name__ == '__main__':
    
    l1=linkedlist(1)
    l1.addnode(5)
    
    l1.addnode(9)
    l1.addnode(14)
    l1.addnode(25)

    
    l2= linkedlist(6)
    l2.addnode(9)
    l2.addnode(21) 
    
    l1.display()
    print "\n\n"
    l2.display()
    
    a=l1.mergeSortedLinkedList(l2)
    a.display()
    
    '''
    l1.formLoop()
    l1.isLoopExistUsingCounter()
    l1.isLoopExistsUsing2Pointers()
    
    l1.removeLoop()
    
    l1.display()
    
 
    l1.addnode(2)
    l1.addnode(1)
    l1.addnode(2)
    l1.addnode(4)
    l1.addnode(2)
    l1.addnode(1)
    l1.addnode(3)
    l1.addnode(1)
    '''



    
    
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
             
    
    
    #####
    ## 
    #1.Merge two sorted linkedlist in progress
    #2.Implementation of merge sort in progress
              



