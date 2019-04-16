def depth_first_search(problem,node):
    if problem.goal(node): return [node]
    # base case

    for n_succ in problem.succ(node):
        sol = depth_first_search(problem,n_succ)
        if sol: # its not empty
            # first path is returned
            return [node] + sol
