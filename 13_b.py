def sol(input_text):
    me, busses = input_text.split("\n")
    me = int(me)
    
    minWait = me
    best = None
    
    busses = [(int(cadence), offset) for offset, cadence in enumerate(busses.split(",")) if cadence != "x"]
        
    busses.sort(reverse=True)

    me = 0
    increment = 1
    
    for i in range(len(busses)):
        cadence, delta = busses[i]
        cnt = 0
        
        # print(cadence)
 
        while True:
            if ((me + delta) % cadence) != 0:
                me += increment
            else:
                break

        increment *= cadence       
        
    return me

test_input = """939
1789,37,47,1889"""

input_text = """1000390
23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,383,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,503,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37"""

print(sol(input_text))

