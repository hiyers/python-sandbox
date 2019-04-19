#
# wolf_cabbage_goat.py
#
import search    # get the interface

def other_side(left_right):
    if left_right == 'left':
        #print('move right')
        return 'right'
    elif left_right == 'right':
        #print('move left')
        return 'left'

    
def safe(node):
    # The side without the farmer needs check
    # the other side is safe
    side_without_farmer=other_side(node['farmer'])
    lone_travelers = set(traveler for traveler in node if node[traveler] == side_without_farmer)
    # dangerous animals
    unsafe = set(['wolf','goat']).issubset(lone_travelers) or set(['goat','cabbage']).issubset(lone_travelers)
    return not unsafe

class Wolf_Cabbage_Goat(search.Nodes):
                 # define start node, everyone is on the left
                 def start(self):
                 # farmer, wolf, cabbage, goat on one side
                     return {'farmer':'left',
                          'wolf':'left',
                         'goat':'left',
                         'cabbage':'left'}

                 # define goal node, everyone is on right
                 def goal(self,node):
                     #true if all moved to right
                     return set(node[i] for i in node) == set(['right'])

                 # define successor    
                 def succ(self,node):
                     #for all possible travelers including none
                     #print('trying to find successor',node)
                     for traveler in list(node.keys()) + ['']:
                         if traveler == 'farmer':
                             continue
                         # ignore we will deal separately with farmer
                         new_node = node.copy()
                         # create as safety copy
                         # if somebody wants to travel and farmer is on same side, do it
                         #print('traveler',traveler)
                         #print('new_node[travler]',new_node[traveler])
                         if traveler and new_node[traveler] == new_node['farmer']:
                             #print(traveler,' will move to other side')
                             new_node[traveler] = other_side(new_node[traveler])
                             #print('after move new_node[travler]',new_node[traveler])

                         # the farmer always travels
                         new_node['farmer'] = other_side(new_node['farmer'])
                         #print('farmer travels',new_node)
    
                         #after a trip, the new state is ok if no one gets eaten
                         if safe(new_node):
                             #print('this one is safe',new_node)
                             yield new_node
