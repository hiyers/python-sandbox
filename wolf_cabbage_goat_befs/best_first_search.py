import heapq
import path

# Candidates is a list of paths

def best_first_search(problem,candidates):
    if not candidates: return
    # make sure there is something in the candidates list
    
    #print('candidates',candidates)
    
    cand = heapq.heappop(candidates) # pop the best candidates path
    node = cand.current()
    
    if problem.goal(node): return cand 
    # base case
    
    for succ_node in problem.succ(node):
        heapq.heappush(candidates,cand.appended(succ_node))
        # 1 -step extension
     
    return best_first_search(problem,candidates)