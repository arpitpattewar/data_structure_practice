'''
Created on Aug 28, 2018

@author: aavinash
'''


class Heap:
    def __init__(self):
        self.input = []
        
        
        
    def insert(self, num):
       """This is heap function, while forming heap
       """
       self.input.append(num)
       #print "Inserting {}".format(num)
       self.build_max_heap()  
                
            
    def max_heapify(self, idx):
        #print "I am in max_heapify {}".format(idx)
        left = 2*idx+1  
        right = 2*idx+2  
        
        largest = idx
        if  left < len(self.input) and self.input[idx] < self.input[left]  :  largest = left
        if right < len(self.input) and self.input[largest] < self.input[right] :  largest  = right
        if largest != idx :
            print "I am here"
            self.input[idx],self.input[largest] = self.input[largest],self.input[idx]
            self.max_heapify(largest)            
            
    def extract_max(self):
        """This is heap function 
        """
        self.build_max_heap()
        max = self.input[1]
        del self.input[1]
        return max
    
    def build_max_heap(self):
        middle = len(self.input)/2
        for i in range(middle,-1,-1):
            self.max_heapify(i)
            

    def heap_sort(self):
        heap_size = len(self.input)-1 
        
        while heap_size >= 0:
            #print self.input, heap_size
            self.build_max_heap()
            self.input[0], self.input[heap_size] = self.input[heap_size], self.input[0]
            print self.input[heap_size]
            del self.input[heap_size]
            heap_size = len(self.input)-1 
            

if __name__ == '__main__':
    input = [45, 78, 32, 65, 43, 79, 11, 8, 44, 12,-34,-56,12,34,5,6,4,45,345]
    
    
    input_1 =[12,45,32,78,65,43,79,55,8,44,96]
    input_2=[-23,-56,-78,-90,0,25]
    input_3=[-3,2,343,4,23,123,123,55,55,55,0]
    input_4 = [12,4,67,5,6,80,91]
    
    
    h1 = Heap()
    for i in input_4:
        h1.insert(i)
        
    h1.heap_sort()


    