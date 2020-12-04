input_str_ex = """..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->"""

input_str = """...........#..#.#.###....#.....
...#..#...........#.#...#......
#.....#..#........#...#..##....
..#...##.#.....#.............#.
#.#..#......#.....#....#.......
.....#......#..#....#.....#....
.......#.#..............#......
.....#...#..........##...#.....
...#....#.#...#.#........#...#.
..#.........###.......##...##..
.#....#...........#........#..#
..#.............##.............
..#.##.#....#................#.
.....##.#.......#....#...#.....
......#.#....##................
..#..........###..#..#.#..#....
....#..............#....##..#.#
.#.........#.#....#.#.#....#...
..#.....#......##.#....#.......
..#.#....#..#.#...##....###....
...#......##...#........#.#..#.
.##.#.......##....#............
...##..#.#............#...#.#..
.##...##.#..#..................
..#......##......#......##.....
.....##...#..#...#.........#...
.##.#.....#..#..#.##....##....#
..#.#......#.......##..........
......................#......##
##.#...#.................#.#.#.
......#.#..........#.....##.#..
#.#......#.....#...........#...
.....#...#.......#..#..#.#...#.
...........#......#.#...#......
....##...##...........#......#.
.........#.##..................
......#...#....#......##.##...#
......#...#.#########......#...
.......#.#...#.......#..#......
............#...#...#.###...##.
...........#..........#...#....
...#..#.#................#.#..#
..#....#.....#.............#.#.
....##......#........#....#....
........##...............#....#
........#..#...#..............#
...#....#.#...#..#...#....#.#.#
.........#.......#....##.......
#.##..............#.#........##
......................###......
.........#....##..##....#.#.#..
.#...##.#.#...#....##..#.....#.
....................#.#......#.
.#..#.......................#..
..#..#.............#..#....#...
...#...#..#...#...#.#..#.##....
........#....#...#....#........
.#.....#........#.........#...#
...#......#..#..#..####..#.....
#....#..............#.##.......
.#....#.............##...#.....
....#...#.##........##......#..
##....#...#.......#..#........#
....##........................#
..................#..#.........
..#....#........#..#.......#...
#...#..#....#...##...........#.
.........#..#..#.#.##..........
....#.#..#.....#..#.#.#.#..#.##
##................#.##.....#...
.#.....###..#..#..#.....#....##
...#...........#..........####.
.#.....#....#......#.##..#.#...
..#...##....#................#.
........#.......#......#.#.....
....#.#.#.#....#...#......#..#.
...........#......#..#.........
###...##......##.#..#....##....
##....##.........#..#....###...
#.#.....#....#......#...#..##..
#....##.#..............#.##....
.#........#.#.........#...#....
......................#......#.
........#..#..##.....#..#.#....
..#...###.................#..#.
...#...#............#..........
.##.......#..#.........#....#..
.#..............#....#....##...
...............##..#.#.......##
.#.....#....#...#..#.......#..#
#..#.............#....#......#.
.....#.#......#.........###..#.
.#...#.#...............#....#..
#......#.............#.........
.#.##.#.####...#..#.##..#.....#
.....#......#..#...#.......#...
#........###...#.....#..#.....#
....#.#.....#...#..........#...
...#.#.......#.#......#..#.##..
..#..........#.#..#.......#.#..
#...#.#..............#...###.#.
...#..#...#............###.....
..#..#...#.#............#..#...
.###.#.....................#..#
....#....#..#.....##.##........
#....#....#.#..#.........#.....
.#.....##....#............##..#
#....#.#...#...#..#.#......#...
#.....##.....##.....##.#...##..
...##...#..#..####.#........#..
.........#...#......##..##..#..
..#.....###.#..#..####.#.......
.......#......#...#..##....#...
.#.....#.#.#..#....#...#..##...
..........#.#...#...#.#..#.....
....#.....#........#.....##..#.
..#.#.##.........#...##.....##.
.........#.##....#............#
............##.....#.......#.#.
......#.....#...#..#..###......
##.....#.......#...##.#....#...
...........##......#..##...#.#.
..#.#.#.#...#.......#....#...#.
#.............#.....#.#...###..
##....#.......#.....#..##.#....
...#.......#....#.........##...
......#.......#......##.##.....
..#......#...#.#........#......
....#.#....#.#.##......#.....#.
#......#.........#..#....#.....
........#..#....##.....#.......
#......##....#.##....#......#..
..#.......#............##.....#
...........#...#...........#...
#.......#...#....#....#...#.#.#
..###..#........#........#.....
..#..###...........#.#......#..
.#...........#......#..........
.#.......#.....#.......#.......
..#......##.#............#....#
#..........#.....#.#..#........
.....#...##.##.......#......#..
..........#.....#........#.#.#.
....#......#.....#......#.#....
.........#.#.#..#...##....#...#
.........#.......#...##...#.#..
.##........#...............#...
.......#....#...........##.....
.........###......#.........#.#
......#.......#...#..........#.
...#.#..........##......#...#..
#.......#.#..........#.........
................#..#......#..##
.....#...#....#.#.....#........
#.....#....#...........#....#..
#....#.#..#...##....#...##.#...
...#.....#......#.#....#..#..#.
..#................#...#.#..##.
..........#..............#..#.#
.....##.....#..#.###...........
....#.#......#.#...........#...
.#....#.#.........##.#....#....
.#.#........#........###....#..
##.#................#...#..#...
.......#......##..#.....#..#.#.
...#............#......###...##
#.#...........#.........#......
.....#.#.#.................#...
....#..............#...#.#.....
...#.#.....##..#...............
.#..##...#....##.....###..#....
...............#...#...#.#.###.
.###....#.....#...#.#......#...
...#..#.....#.......#..##.#....
...........#..#....##..#...#...
...#...#..........#.......##.#.
............#.#.......#........
....#.........#.....#..........
...#.###.##..#...##..####..#..#
.#.#...#..#...................#
.....#..#.....##..#............
....#......#...##..#.##........
...#...............#..#.....##.
...#......#.........#.#..##....
.#....#.##.......#......#......
....#.......#....#..........#..
#.#.#....###.#.#.............#.
..##..###........#.#..#.#..#...
......#.#............##.#...###
.........#.#....#####.....##...
............##......#.#..#.....
...#.....#.....###....#........
##..........####.##.#.#........
....................##.....##.#
#.#............#........#......
....#...##.....#......#....#...
...###.#..##..................#
..###......#..............#.#.#
.#...#...........#....#........
....#............#..#..#.#.....
...#.........#.#.........#.####
..#...#...#...#...........#....
...............#.#......##..#..
#....#.#.......#.#..#......#..#
........#.#....#..#...#..#...#.
...#..#.......#...........#....
...........#.......#...........
.#......#................#.....
....#.#.#...#......#..#...#....
................#.#.#....#.....
.........................##..#.
.#...........#............##...
#...............#.....##.#.#..#
.........#.......###....#.....#
....##...#...#.....#..#........
........#.....#..#.#.#...#..#..
......#.......#.#.........#.#..
#......#............#...#....#.
#..##...#..#................#..
.##...#...#.....#.##.......#..#
.......#.##........##..##......
##.#..##...............#.....#.
......#....#..##...#......###.#
#........##..#....#.#......#...
.#......##.#...#.#...#.........
.#.#...#..#.............#......
.##..........#..........#......
.#.....#.....#..............#.#
..#.........#..#.#.....#.#....#
..#.##..............##...#..###
....................#..........
......###..#..#...........#....
..#..........#.......#...#.....
...#......#......#.............
....##..............#.#.....#..
........#.#......#..#........##
.............#...#.#.........##
...###...#..........##.......#.
.#..........#...##..#.#.....#..
##...#.........#...............
......#....#....#.....#.....#..
..........#....#...#...#..#...#
...##....#.#.#..#...##.........
#......#.#...##.###...#....#...
##.......##.#......##..#...#...
......#.............#.##.....##
#.......###....####.#...##....#
..#...#..#.......#..........#..
#.....#..#..#..#.##...###...#..
.....##.#..#..#..#.#....#...#..
..#...#..................##....
....#.#........##..............
#...#.......##...#...#.#.......
..#...#........##....#.#.......
..........###...###...#......#.
#.....#..###...##...##..#..#..#
..#.....##.....#.......##..#.#.
........#........#.........#...
.................#....#.......#
.......#...#.....#...#.#.......
....##...............#...##...#
.##...#................#...#...
.............#.................
.#..#....#....#.#....#.........
.#.#..#..........#.......#.....
.....##.....##...#..#..........
#...#.#.........#......#..#....
........#....#...#....#.#.##...
....#..#........#...#...#......
.#..#.....#.#...#.........#....
.#..#..#...........#..#....#...
....###.............#..#.......
#......#..#..##..........#.#...
#..#..#.##..#...#.#.#..........
....###......#.##.....#....#...
.##..#...#......##.#...........
..#..#.......#.....#.##....#.#.
.......#.#.#........#....##....
..##...#....#...............###
#..##..#...........#.#....##...
...##..#.....................#.
###......#....#....###..#...##.
.........##............#..#...#
..#..........#...#.#.#......#.#
.......#.....##..##......#.##..
#..........#.....##.#..........
#.......#.#...#...#....#.......
#...#.....##.......#.#..#.#.#..
.........#.#.#..#..#...#.###...
.................##...#....#...
###.......#..........##...#....
#.#..#.........#....##.#.......
......#.#.....#........#.......
.......#.#........#......#.#..#
..............#..#...##....#..#
#...........#...##.....#..#.#..
..#....#..#.#.#...#..#....#.#..
...##.#.....#..#...##..#.....#.
..#.#................#........#
......#...#.............#......
.##............#....#...#..#...
....#...#...........#.......#..
.###..#.......#.............#.#
.#.#....#.#...........#.#......
...#.........#.........#..#....
...#..........#.#.....#.#......
.....#........#....##......#...
..#.#.#......#..#.#......#....#
.#.#..#................#.#.....
.#.#.........##...#.......#.#.#
#..#.....#...#..#...........#..
..##......####......#..#....###
#.....###....#.#........#..#..#
..##.#...#.#..##..........#..#.
#.........#.#.............#...#
...#.#...#...#.#.#....##.......
##.##...#.....#...#...........#
....#........#.#.....#.........
.................##..#..##...##
.....##....#...#...#.....#..#..
....#...#........#............#
..#...........##....#...#...##.
.....#......#.........#..##.#.."""

def sol(input_str):
    lines = input_str.split("\n")
    
    cols = len(lines[0])
    rows = len(lines)
    
    cnt = 0
    
    for r in range(rows):
        c = r * 3
        
        if lines[r][c % cols] == '#':
            cnt += 1
            
    return cnt
    
print(sol(input_str))