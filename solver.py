#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import Counter,namedtuple
import itertools
from itertools import compress,repeat,chain

node= namedtuple("node", ['index','neighbour']) #Each node has an index where its colour is found
def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])
    colours= [0]*node_count
    

    nodes = []
    edges=[]
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        node1= int(parts[0])
        node2= int(parts[1])
        edges.append((node1,node2))
    
        if any(x.index==node1 for x in nodes):
                filt=[getattr(a, 'index')==node1 for a in nodes]
                #item= compress([getattr(a, 'index')==node1 for a in nodes],nodes) 
                #item[0].neighbour.append(node2) 
                item= next((x for x in compress(nodes,filt)))
                item.neighbour.append(node2) 
        else:
            nodes.append(node(index=node1,neighbour=[node2]))
        if any(x.index==node2 for x in nodes):                            
                filt=[getattr(a, 'index')==node2 for a in nodes]
                item= next((x for x in compress(nodes,filt)))
                item.neighbour.append(node1)                 
        else:
        
            nodes.append(node(node2,[node1]))
    
    #Greedy-sort vertexes by degree
    edges=list(itertools.chain(*edges))
    edges_sorted=[]
    [edges_sorted.append(x) for x in list(chain.from_iterable(repeat(i, c) for i,c in Counter(edges).most_common())) if x not in edges_sorted]
    mapping={n.index:n for n in nodes}
    
    for n in edges_sorted:
        print(f'edge:{n}')
        item= mapping[n]
        if colours[item.index]==0:
          colours[item.index]=min(range(1,node_count+2))
        for x in item.neighbour:
          neighbour_item= mapping[x]
          neighbour_items2=[mapping[i] for i in neighbour_item.neighbour]
          #if colours[neighbour_item.index]==0:
          colours[neighbour_item.index]= min([i for i in range(1,node_count+2) if i not in [colours[y.index] for y in neighbour_items2]])
      
 
  
       

    # prepare the solution in the specified output format
    output_data = str(node_count) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, colours))

    return output_data
    
    
    


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')


