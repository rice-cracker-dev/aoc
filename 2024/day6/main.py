import math


type Grid = list[list[bool]]
type Move = tuple[int, int, int, int]


def readInputs() -> tuple[Grid, int, int]:
    grid: Grid = []
    pX, pY = 0, 0

    with open("./inputs.txt") as f:
        for yi, yv in enumerate(f):
            line: list[bool] = []
            for xi, xv in enumerate(yv):
                line.append(xv == "#")
                if xv == "^":
                    pX, pY = xi, yi
            grid.append(line)

    return grid, pX, pY


def rotatePoint(x: int, y: int, degree: float) -> tuple[int, int]:
    rX = (x * math.cos(degree)) - (y * math.sin(degree))
    rY = (y * math.cos(degree)) + (x * math.sin(degree))

    return round(rX), round(rY)


def getNext(x: int, y: int, dX: int, dY: int) -> tuple[int, int]:
    return x + dX, y + dY


def isPointOutOfBound(grid: Grid, x: int, y: int) -> bool:
    if y < 0 or y >= len(grid): return True
    if x < 0 or x >= len(grid[y]): return True

    return False


def printGrid(grid: Grid, pX: int, pY: int, oX: int | None = None, oY: int | None = None, pathGrid: Grid | None = None):
    for yi, y in enumerate(grid):
        line = ""
        for xi, x in enumerate(y):
            if pX == xi and pY == yi:
                line += "@"
            elif pathGrid and pathGrid[yi][xi]:
                line += "$"
            elif oX == xi and oY == yi:
                line += "O"
            else:
                line += "#" if x else "."
        print(line)


def moveNext(grid: Grid, pX: int, pY: int, dX: int, dY: int) -> Move | None:
    nextX, nextY = getNext(pX, pY, dX, dY)
    if isPointOutOfBound(grid, nextX, nextY):
        return None

    if grid[nextY][nextX]:
        dX, dY = rotatePoint(dX, dY, math.radians(90))
    else:
        pX, pY = nextX, nextY

    return pX, pY, dX, dY


def getMoveList(grid: Grid, pX: int, pY: int) -> tuple[int, list[Move]]:
    dX, dY = 0, -1
    moves = 0
    gridClaimed: Grid = [[False for _ in range(len(grid[y]))] for y in range(len(grid))]
    moveList: list[Move] = []
    while not isPointOutOfBound(grid, pX, pY):
        if not gridClaimed[pY][pX]:
            gridClaimed[pY][pX] = True
            moves += 1

        moveList.append((pX, pY, dX, dY))

        next = moveNext(grid, pX, pY, dX, dY)
        if not next:
            break

        pX, pY, dX, dY = next

    return moves, moveList


def isRepeatingPattern(grid: Grid, pX: int, pY: int, dX: int, dY: int) -> bool:
    moveList: list[Move] = []

    while not isPointOutOfBound(grid, pX, pY):
        moveList.append((pX, pY, dX, dY))

        nextMove = moveNext(grid, pX, pY, dX, dY)
        if not nextMove:
            return False
        
        if nextMove in moveList:
            return True

        pX, pY, dX, dY = nextMove
    
    return False
        

# 💀💀💀
def part2(grid: list[list[bool]], moveList: list[Move], startX: int, startY: int):
    obstacles: list[tuple[int, int]] = []
    count = 0

    for pX, pY, dX, dY in moveList:
        count += 1
        nextX, nextY = getNext(pX, pY, dX, dY)
        if isPointOutOfBound(grid, nextX, nextY) or grid[nextY][nextX] or (nextX, nextY) == (startX, startY) or (nextX, nextY) in obstacles:
            continue
    
        grid[nextY][nextX] = True
        #printGrid(grid, startY, startX, nextX, nextY)
        #print()
        #print(nextX, nextY)
        repeating = isRepeatingPattern(grid, startX, startY, 0, -1)
        if repeating:
            obstacles.append((nextX, nextY))
            print(f"{count} / {len(moveList)}")

        grid[nextY][nextX] = False


    print(len(obstacles))


def main():
    grid, pX, pY = readInputs()
    moves, moveList = getMoveList(grid, pX, pY)
    print(moves)
    part2(grid, moveList, pX, pY)

if __name__ == "__main__":
    main()
