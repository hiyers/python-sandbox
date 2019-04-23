##
## This is just an interface, do not use on its own
##
class Nodes:
    def succ(self,n):
        raise Exception("Successor undefined")
    def start(self):
        raise Exception("Start undefined")
    def goal(self,n):
        raise Exception("Goal undefined")
