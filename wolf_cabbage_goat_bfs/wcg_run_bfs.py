import wolf_cabbage_goat
from breadth_first_search import *

wcg = wolf_cabbage_goat.Wolf_Cabbage_Goat()

for s in breadth_first_search(wcg,[[wcg.start()]]):
    print(s)

# careful how to specify thei initial candidates
# its not a node but a candidate list of paths
# i.e. list of lists