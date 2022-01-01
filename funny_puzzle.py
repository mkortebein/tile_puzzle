import heapq

goal_state = [1,2,3,4,5,6,7,8,0]
coords = [(0,2),(1,2),(2,2),
          (0,1),(1,1),(2,1),
          (0,0),(1,0),(2,0)]

def manhattan(state):
    total = 0
    for i in range(9):
        if goal_state[i] == state[i]:
            continue
        
        
        if state[i] != 0:
            x1 = state.index(state[i])
            x2 = goal_state.index(state[i])
            total += abs(coords[x2][0] - coords[x1][0]) + abs(coords[x2][1] - coords[x1][1])
        
        
    
    return total

def replace_tiles(zero_tile, new_tile, state):
    temp_state = state[:]
    temp_num = state[new_tile]
    temp_state[new_tile] = 0
    temp_state[zero_tile] = temp_num
    return temp_state

def get_succ(state):
    lists = []
    h_list = []
    
    if state[0] == 0:
        lists.append(replace_tiles(0,1,state))
        lists.append(replace_tiles(0,3,state))
    
    if state[1] == 0:
        lists.append(replace_tiles(1,0,state))
        lists.append(replace_tiles(1,2,state))
        lists.append(replace_tiles(1,4,state))
        
    if state[2] == 0:
        lists.append(replace_tiles(2,1,state))
        lists.append(replace_tiles(2,5,state))
            
    if state[3] == 0:
        lists.append(replace_tiles(3,0,state))
        lists.append(replace_tiles(3,4,state))
        lists.append(replace_tiles(3,6,state))
    
    if state[4] == 0:
        lists.append(replace_tiles(4,1,state))
        lists.append(replace_tiles(4,3,state))
        lists.append(replace_tiles(4,5,state))
        lists.append(replace_tiles(4,7,state))
        
    if state[5] == 0:
        lists.append(replace_tiles(5,2,state))
        lists.append(replace_tiles(5,4,state))
        lists.append(replace_tiles(5,8,state))
        
    if state[6] == 0:
        lists.append(replace_tiles(6,3,state))
        lists.append(replace_tiles(6,7,state))
    
    if state[7] == 0:
        lists.append(replace_tiles(7,4,state))
        lists.append(replace_tiles(7,6,state))
        lists.append(replace_tiles(7,8,state))
        
    if state[8] == 0:
        lists.append(replace_tiles(8,5,state))
        lists.append(replace_tiles(8,7,state))
           

    return sorted(lists)

def print_succ(state):
    ans = get_succ(state)
    for l in ans:
        print(f'{l} h={manhattan(l)}')

        
def solve(state):
    # Priority Queue
    OPEN = []
    CLOSE = []
    final = []
    # Moves
    g = 0
    # Parent Index
    parent = -1
    # Initial node on prioity queue
    heapq.heappush(OPEN, (manhattan(state), state, (g, manhattan(state), parent)))
        
    # While there are items in OPEN
    while OPEN:
        # Remove item from OPEN with lowest heuristic and place on CLOSE
        curr = heapq.heappop(OPEN)
        CLOSE.append(curr)
        
        parent = CLOSE.index(curr)
        # If currect node is goal node then stop loop
        if curr[1] == goal_state:
            break
        
        # Next move
        # Parent node is index of current node on CLOSE
        #parent = CLOSE.index(curr)
        # For successor in list of successors
        for succ in get_succ(curr[1]):
            # Checking if successor is on OPEN
            newList = [sl[1] for sl in CLOSE]
            if succ in newList:
                continue
            
            for node in OPEN:
                if node[1] == succ:
                    if node[2][0] > g+1:
                        node = (manhattan(node[1]), node[1], (g+1, manhattan(node[1]), parent))
            

            else:
                h = manhattan(succ)
                g = curr[2][0] + 1
                heapq.heappush(OPEN, (h+g, succ, (g, h, parent)))
            
    
    while curr[2][2] != -1:
        final.append(curr)
        curr = CLOSE[curr[2][2]]
    
    final.append(CLOSE[0])
    
    final.reverse()
    move = 0
    for i in final:
        print(f'{i[1]} h={i[2][1]} moves: {move}')
        move+=1
        
