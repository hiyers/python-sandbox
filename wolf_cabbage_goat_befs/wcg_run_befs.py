import wolf_cabbage_goat
from best_first_search import best_first_search

class Path:
    
    def __init__(self,path=[],length=0):
        # current path, current length(cost)
        self.path=path
        self.length=length
        
    def __le__(self,path2):
        # default comparison by cost
        return self.length <= path2.length
    
    def __len__(self): return self.length
    
    def cost(self,n_from,n_to): return 1 # default cost
    
    def current(self):
        # defautl : last node in path
        if not self.path:
            raise Exception('Path is empty')
        return self.path[-1]

    def appended(self,node):
        # return the path with appended node (and record new length)
        # this is so general that it can be in path 
        
        # careful to return an object of the original class by which 
        # we were called
        
        return self.__class__(path=self.path+[node], 
                            length=self.length+self.cost(self.current(),node))


class WCG_Path(Path):
    
    def graph(self,n):
        return " ".join(p for p in n if n[p] == 'left') + "----" +\
               " ".join(p for p in n if n[p] == 'right')
               
    def __repr__(self):
        return "\n".join(self.graph(n) for n in self.path)

wcg = wolf_cabbage_goat.Wolf_Cabbage_Goat()
start_path = WCG_Path(path=[wcg.start()], length=1)
print(best_first_search(wcg,[start_path]))


# careful how to specify thei initial candidates
# its not a node but a candidate list of paths
# i.e. list of lists