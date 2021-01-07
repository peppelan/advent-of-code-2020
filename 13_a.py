

def sol(input_text):
    me, busses = input_text.split("\n")
    me = int(me)
    
    minWait = me
    best = None
    
    for cadence in busses.split(","):
        if cadence == "x":
            continue
        
        cadence = int(cadence)
        
        if me % cadence == 0:
            return cadence
        
        lastPassBeforeMe = (me // cadence) * cadence
        nextPassAfterMe = lastPassBeforeMe + cadence
        
        wait = nextPassAfterMe - me
        
        # print(cadence, "passed at", lastPassBeforeMe, "and will come back at", nextPassAfterMe, "and I'll wait for it", wait)
        
        if wait < minWait:
            minWait = wait
            best = cadence
            # print("Waiting", wait, "for", cadence)
    
    return best * minWait
    
    
    

test_input = """939
7,13,x,x,59,x,31,19"""

input_text = """1000390
23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,383,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,503,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37"""

print(sol(input_text))
