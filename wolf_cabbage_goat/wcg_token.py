import wolf_cabbage_goat

class WCG_Token(wolf_cabbage_goat.Wolf_Cabbage_Goat):
    def token(self,node):
        #get the list of pairings of traveler and location
        # each of them e.g. ('goat','right')
        paris=list(node.items())

        #sort them arbitrarily but fixed, so that
        # the token does not depend on arbitrary dictionary order
        paris.sort()

        #make it immutable, turn it into tuple
        return tuple(paris)
