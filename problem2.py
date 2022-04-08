


class Solution:
    def get_create_copy_node(self, d, n):
        if n not in d:
            copy_n = Node( n.val )
            d[n] = copy_n
        return d[n]
        
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        # hashmap to store the node and its copy
        d = {}
        queue = []
        queue.append(node)
        #to store the all the nodes which have been visited
        visited = set()
        visited.add(node)
        
        while len(queue) != 0:
            #print([ node.val for node in queue])
            #pop the node out of the queue
            n = queue.pop(0)
            #print(n.val)
            
            #if the node is not in the dictionary, name the new copy node
                
            copy_n = self.get_create_copy_node(d, n)
                
            #loop through all the neighbour nodes
            for neighbour in n.neighbors:
                #print(neighbour.val)
                
                #if the neighbour node not in hashmap
                copy_neighbour = self.get_create_copy_node(d, neighbour)
                
                copy_n.neighbors.append( copy_neighbour )
                
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    
        # for k, v in d.items():
        #     print(k.val, v.val)
        #print(d[node].val)
        return d[node]
