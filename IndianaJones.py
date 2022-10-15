#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
#import numpy as np, itertools

from queue import LifoQueue 
Item = namedtuple("Item", ['index', 'value', 'weight'])


def solve_it(input_data):
 lines = input_data.split('\n')

 firstLine = lines[0].split()
 item_count = int(firstLine[0])
 capacity = int(firstLine[1])

 items = []
 for i in range(1, item_count+1):
      line = lines[i]
      parts = line.split()
      items.append(Item(i-1, int(parts[0]), int(parts[1]))) 
 

 def branch_bound_depthfirst(input_data):
     lines = input_data.split('\n')

     firstLine = lines[0].split()
     item_count = int(firstLine[0])
     capacity = int(firstLine[1])

     items = []

     for i in range(1, item_count+1):
       line = lines[i]
       parts = line.split()
       items.append(Item(i-1, int(parts[0]), int(parts[1])))         
     
        
     taken = [0]*len(items)       
        
     class Node:
        def __init__(self,level,val,wgt,bound,contains,total,right_child=None,left_child=None):
         self.level=level
         self.val=val
         self.wgt=wgt
         self.bound=bound
         self.contains=contains
         self.total=total
         self.left_child=left_child
         self.right_child=right_child
        
        def __str__(self):
            print(self.level, self.val, self.wgt, self.contains)
         
     

     items= sorted(items, key=lambda x:x.value/x.weight)
     

     '''def optimistic_estimate(level,remaining_cap):
         if level==len(items) or remaining_cap==0:
             oe=0
         else:
             while level<len(items):
                 if items[level].weight+weight<remaining_cap:
                     weight+=items[depth].weight
                     oe+=items[depth].value
                     remaining_cap-=items[depth].weight
                 else:
                     oe+=items[depth].density*remaining_cap
                     
         return oe'''          
                             
         
     def optimistic_estimate(modified_items=items):
         bb={item:0 for item in modified_items}
         w=0
         valuee=0
         for k,v in bb.items():
            if k.weight+w<=capacity:
              w+=k.weight
              valuee+=k.value
              bb[k]=1 
            
         if 0 in bb.values():
             remaining= next((k for k,v in bb.items() if v==0))
             frac= (capacity-w)/remaining.weight * remaining.value
             valuee+=frac
            
         return valuee
        
          
     
     #q=LifoQueue()
     q=[]
     root= Node(-1,0,0,0.0,[],items)
     root.bound= optimistic_estimate(items)
     q.append(root)
     best_val=0
     best_val,weight=0,0
    
     while q:
               # c=q.pop() #c=parent node
                c=q[-1]
                #print(f' bestval={best_val}, level:{c.level}, weight: {c.wgt}, value: {c.val},contains {c.contains},oe:{c.bound}')
                if c.level==len(items)-1:  #for termninal nodes
                   if c.val>best_val and c.wgt<capacity:
                    best=c.contains
                    best_val=c.val
                    weight= c.wgt
                   q.pop()
                    
                elif c.level<len(items)-1:
                  
                  
                  if c.left_child==None:
                    level= c.level+1
                    left_contains= list(c.contains)
                    left_contains.append(items[level])
                    left_wgt,left_val=0,0
                    for x in left_contains:
                        left_wgt+=x.weight
                        left_val+=x.value
                    left= Node(level,left_val,left_wgt,c.bound,left_contains,c.total)
                    c.left_child=left
                    if left_wgt<=capacity:
                     q.append(left)
                     continue
                  elif c.right_child==None:
                      level=c.level+1
                      right_total = list(c.total)
                      right_total.remove(items[level])
                      right= Node(level=level, val=c.val,wgt= c.wgt, bound=optimistic_estimate(c.total),contains=c.contains,total=right_total)
                      c.right_child=right
                      if right.bound>best_val and c.wgt<=capacity:
                       q.append(right)
                  else:
                     q.pop()
                  
                  #if c.val>best_val and c.wgt<capacity:
                    #best=set(c.contains)
                    #best_val=c.val
                    #weight= c.wgt
                    #q.get()
                    
                
                
    
     for item in best:
               taken[item.index]=1
    
     weight2=0
     value2=0
     for item in best:
         weight2+=item.weight
         value2+=item.value
               
                
          #prepare the solution in the specified output format
     output_data = str(best_val) + ' ' + str(0) + '\n'
     output_data += ' '.join(map(str, taken))
     return output_data
 return branch_bound_depthfirst(input_data)

 
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
        
       
        
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')


          
            
    

            
