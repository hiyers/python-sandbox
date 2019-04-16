E='E'
C='C'
S='S'


start_stable=[C,C,C,C,E,S,S,S,S]
goal_stable=[S,S,S,S,E,C,C,C,C]

def successors(stable):
    #find empty spot
    empty=stable.index(E)
    #generate list of unfiltered candidate positions
    candidates = [empty-2,empty-1,empty+1,empty+2]
    #keep only those which are inside the stable
    candidates = [c for c in candidates if c>=0 and c< len(stable)]

    #cow can always move right, sheep always left and from 2 fields
    #apart, they have to jump over an animal
    candidates = [c for c in candidates if
                  stable[c:c+2] ==  [C,E] or #when cow can move right
                  stable[c-1:c+1] == [E,S] or #sheep can move left
                  stable[c:c+3] == [C,S,E] or #cow jumps to right over sheep
                  stable[c-2:c+1]==[E,C,S]] #sheep jumps over cow towards left
    #make sure all these entries are occupied
    #not necessary for operation just for better style
    assert not [c for c in candidates if stable[c] == E]

    for c in candidates:
        new_stable=stable[:]  # make a copy
        #move the candidate to empty pos
        new_stable[c],new_stable[empty]=new_stable[empty],new_stable[c]
        yield new_stable # remember where we were
        
def solution(stable):
    if stable==goal_stable:
        return [stable]

    #else depth first search
    for new_stable in successors(stable):
        #print new stable
        sol = solution(new_stable)
        if sol:
            return [stable]+sol

        
for s in solution(start_stable):
    print(s)
    
