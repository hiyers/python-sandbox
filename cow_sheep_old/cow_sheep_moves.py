from gen_barn import barn


def move_cow_right(lst):
    if lst[0,1]==['C'] and lst[1:]==['E']:
        lst[0,1]='E'
        lst[1:]='C'

        
def run_process():
    #lst=barn()
    lst=['C','E']
    print("before:",lst)
    move_cow_right(lst)
    print("after:",lst)
