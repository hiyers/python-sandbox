import wolf_cabbage_goat
import sys
from depth_first_search import *

sys.setrecursionlimit(10000)
wcg = wolf_cabbage_goat.Wolf_Cabbage_Goat()
print(depth_first_search(wcg,wcg.start()))
