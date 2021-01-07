
def sol(input_text):
    turn = 0
    n_to_turn = {}
    last_spoken = None
    
    for n in input_text.split(","):
        if last_spoken != None:
            n_to_turn[last_spoken] = turn
        last_spoken = int(n)
        turn += 1
        
    for i in range(2020 - turn):
        if last_spoken not in n_to_turn:
            new = 0
        else:
            new = turn - n_to_turn[last_spoken]
        
        n_to_turn[last_spoken] = turn
        last_spoken = new
        turn += 1

    return last_spoken
        
    
test_input = """3,1,2"""

input_text = """0,1,4,13,15,12,16"""


print(sol(input_text))
