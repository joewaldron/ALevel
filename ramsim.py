def printgrid(grid):
    for eachRow in grid:
        pstr = ""
        for eachItem in eachRow:
            pstr += str(eachItem)
            #pstr += str(grid[eachRow][eachItem])
        print(pstr)

def initialise():
    grid = []
    for eachRow in range(8):
        grid.append([])
        for eachItem in range(8):
            grid[eachRow].append(0)
    return grid

def update(grid,address,byte):
    count = 0
    for eachbit in byte:
        grid[address][count] = eachbit
        count += 1
    return grid

def read(grid,address):
    byte = ""
    for eachbit in grid[address]:
        byte += eachbit
    return byte

def readandremove(grid,address):
    b = read(grid,address)
    update(grid,address,"00000000")
    return grid,b

g1 = initialise()
print(g1)
printgrid(g1)
print("")
g1 = update(g1,0,"10011111")
printgrid(g1)
g1,b = readandremove(g1,0)
print("")
print(b)
print("")
printgrid(g1)
