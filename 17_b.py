from collections import defaultdict

def render(grid):
    minx, miny, minz, maxx, maxy, maxz = boundaries(grid)
    
    for z in range(minz, maxz+1):
        print("z = ",z)
        
        for r in range(minx, maxx+1):
            row = []
            
            for c in range(miny, maxy+1):
                if grid[(r, c, z)]:
                    row.append("#")
                else:
                    row.append(".")
                
            print("".join(row))
        print()

def boundaries(grid):
    minx, miny, minz, minw, maxx, maxy, maxz, maxw = 0, 0, 0, 0, 0, 0, 0, 0
    
    for (x, y, z, w) in grid:
        if x < minx:
            minx = x
        if y < miny:
            miny = y
        if z < minz:
            minz = z
        if w < minw:
            minw = w
        if x > maxx:
            maxx = x
        if y > maxy:
            maxy = y
        if z > maxz:
            maxz = z
        if w > maxw:
            maxw = w
            
    return minx, miny, minz, minw, maxx, maxy, maxz, maxw
        
def neighbors(coord):
    x, y, z, w = coord
    
    ret = []
    
    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            for k in [z-1, z, z+1]:
                for l in [w-1, w, w+1]:
                    neigh = (i, j, k, l)
                    if neigh != coord:
                        ret.append(neigh)
    return ret

def activeNeighborCount(grid, coord):
    cnt = 0
    for n in neighbors(coord):
        if grid[n]:
            cnt += 1
            
    return cnt

def evolve(grid):
    newGrid = defaultdict(bool)
    
    minx, miny, minz, minw, maxx, maxy, maxz, maxw = boundaries(grid)
    
    for w in range(minw-1, maxw+2):
        for z in range(minz-1, maxz+2):
            for r in range(minx-1, maxx+2):
                for c in range(miny-1, maxy+2):
                    coord = (r, c, z, w)
                    active = grid[coord]

                    if active and 2 <= activeNeighborCount(grid, coord) <= 3:
                        newGrid[coord] = True
                    if not active and 3 == activeNeighborCount(grid, coord):
                        newGrid[coord] = True
    return newGrid

def sol(input_text):
    grid = defaultdict(bool)
    
    for r, line in enumerate(input_text.split("\n")):
        for c in range(len(line)):
            ch = line[c]
            
            if (ch == "#"):
                grid[(r, c, 0, 0)] = True
            
#     render(grid)
    
    for i in range(1, 7):
        grid = evolve(grid)
        
#         print("After", i, "cycles")
#         render(grid)
    
    cnt = 0
    
    for _, v in enumerate(grid):
        if v:
            cnt += 1
            
    return cnt
    
    
    
test_input = """.#.
..#
###"""

input_text = """######.#
#.###.#.
###.....
#.####..
##.#.###
.######.
###.####
######.#"""


print(sol(input_text))
