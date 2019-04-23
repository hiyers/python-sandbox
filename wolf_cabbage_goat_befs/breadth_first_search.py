def breadth_first_search(problem,candidates):
    if not candidates: return
    # make sure there is something in the candndates list
    
    # i am modifying candidates list here 
    # why don't i need to copy?
    #print('candidates is',candidates)
    c = candidates.pop(0)  # pop from the front
    node = c[-1]           # must exist
    
    if problem.goal(node): return c
    # base case
    
    succ = [s for s in problem.succ(node)]
    
    for s in problem.succ(node):
        candidates.append(c+[s])
        # 1-step extension
        
    return breadth_first_search(problem,candidates)  