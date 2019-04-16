from nim_optimal import nim_optimal
from nim_random import nim_random
from nim_human import nim_human

def game_controller(sticks,players):
    i=0
    print(players)
    print ('Total Sticks ',sticks)
    while (sticks>0): # or simply while(sticks)
       sticks -= players[i](sticks)
       print (players[i]," left ",sticks," sticks")
       i=(i+1)%len(players)
       
    print ('Game Over! Player',players[(i-1)%len(players)],' wins.')    

