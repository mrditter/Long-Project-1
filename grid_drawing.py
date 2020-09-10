import sys

def init(wid, hei):
    "Initializes the grid to specific width and height values"
    grid = []
    a, b = 0, 0
    while a < hei :
        cur_row = []
        while b < wid :
            cur_row.append(0)
            b += 1
        grid.append(cur_row)
        a += 1
        b = 0
    return grid

def print_grid(grid):
    a, b = 0, 0
    while a < len(grid) :
        while b < len(grid[0]) :
            print(grid[a][b], end="")
            b += 1
        b = 0
        a += 1
        print()

def one_point(grid, color, x, y):
    a, b = (len(grid) - 1), 0
    a = a - y
    b = b + x
    grid[a][b] = int(color)
    return grid


#def horiz_line():


#def vert_line():


#def filled_rect(): 


#def hollow_rect():


def main():
    a = 1
    # read user input
    for line in sys.stdin:
        com = line.strip()
        com = line.split()
        # do some brief validity checks
        if line[0] == '#':
            continue
        if len(com) == 0:
            print('Input error: no command was given.')
            continue
        if a == 1:
            if com[0] != 'init' :
                print('Input error: init was not the first command.')
                break
        a += 1
        
        # use commands, but first check validity
        # init command
        if com[0] == 'init':    
            try:
                grid = init(int(com[1]), int(com[2]))
            except:
                print("Input error: 'init' was not used properly. (init <wid> <hei>)")
                break
        # print commands
        elif com[0] == 'print' or com[0] == 'print_raw':
            try:
                if com[0] == 'print' :
                    print_grid(grid)
                elif com[0] == 'print_raw' :
                    print(grid)
            except :
                print("Input error: error printing, no parameters should be present")
                continue
        elif com[0] == 'set':
            try:
                if int(com[1]) >= 0 and int(com[1]) <= 9 and int(com[2]) >= 0 and int(com[3]) >= 0 \
                and int(com[2]) < len(grid[0]) and int(com[3]) < len(grid) :
                    grid = one_point(grid, int(com[1]), int(com[2]), int(com[3]))
                else :
                    print("Input error: Boundary issue")
                    continue
            except:
                print("Input error: Issue with set command. (set <color> <x> <y>)")
                continue
        else :
            print("Input error: Invalid command.")

if __name__ == "__main__":
    main()