

#Ignore this File. 




class Node: 
   
    def __init__(self,value) -> None:
        
        self.value = value
        self.childeren = []
        
        pass
        
    def addChild(self, child_node) -> None: 
        
        self.childeren.append(child_node)
        
        
        
        pass 
    
    
    def removeChild(self, child_node) -> None: 
        
        self.childeren = [i for i in self.childeren if i is not child_node]
        
        
    
    
    def traversal(self): 
        
        temp = [self]
        
        while(temp) > 0: 
            current = temp.pop()
            
        temp += current.childeren