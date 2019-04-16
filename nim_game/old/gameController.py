from nim import nim
from nimRandom import nimRandom

def gameController():
    totalSticks=20
    remainingSticks=totalSticks
    
    print 'Total Sticks ',totalSticks
    while (totalSticks>=0):
        print 'nimRandom player plays'
        player='nimRand'
        remainingSticks=remainingSticks-nimRandom(totalSticks)
        print 'Remaining Sticks', remainingSticks
        print 'nimOptimal player plays'
        player='nimOptimal'
        remainingSticks=remainingSticks-nim(totalSticks)        
        print 'Remaining Sticks', remainingSticks
        
    print 'Game Over',player,' wins.;
