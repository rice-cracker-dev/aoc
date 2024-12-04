WORD_TO_SEARCH_PART1 = "XMAS"
WORD_TO_SEARCH_PART2 = "MAS"


def readInputs() -> list[str]:
    with open("./inputs.txt") as f:
        return [line for line in f]


def check(s: list[str], lineIndex: int, charPos: int, dX: int, dY: int, wordSearch: str, wordSearchIndex: int = 0) -> bool:
    if lineIndex < 0 or lineIndex >= len(s):
        return False
    
    line = s[lineIndex]
    if charPos < 0 or charPos >= len(line):
        return False

    char = line[charPos]
    toMatch = wordSearch[wordSearchIndex]

    if char != toMatch: return False
    if char == toMatch and wordSearchIndex == len(wordSearch) - 1: return True

    return check(s, lineIndex + dY, charPos + dX, dX, dY, wordSearch, wordSearchIndex + 1)


def main():
    crossword = readInputs()
    total = 0
    masCount = 0

    for i in range(len(crossword)):
        for char in range(len(crossword[i])):
            # part 1
            if check(crossword, i, char, 0, 1, WORD_TO_SEARCH_PART1): total += 1 # bottom
            if check(crossword, i, char, 1, 1, WORD_TO_SEARCH_PART1): total += 1 # bottom right
            if check(crossword, i, char, 1, 0, WORD_TO_SEARCH_PART1): total += 1 # right
            if check(crossword, i, char, 1, -1, WORD_TO_SEARCH_PART1): total += 1 # top right
            if check(crossword, i, char, 0, -1, WORD_TO_SEARCH_PART1): total += 1 # top
            if check(crossword, i, char, -1, -1, WORD_TO_SEARCH_PART1): total += 1 # top left
            if check(crossword, i, char, -1, 0, WORD_TO_SEARCH_PART1): total += 1 # left
            if check(crossword, i, char, -1, 1, WORD_TO_SEARCH_PART1): total += 1 # bottom left
            
            # part2
            topLeftToBottomRight = check(crossword, i - 1, char - 1, 1, 1, WORD_TO_SEARCH_PART2)
            bottomRightToTopLeft = check(crossword, i + 1, char + 1, -1, -1, WORD_TO_SEARCH_PART2)
            topRightToBottomLeft = check(crossword, i - 1, char + 1, -1, 1, WORD_TO_SEARCH_PART2)
            bottomLeftToTopRight = check(crossword, i + 1, char - 1, 1, -1, WORD_TO_SEARCH_PART2)

            if not topLeftToBottomRight and not bottomRightToTopLeft: continue
            if not topRightToBottomLeft and not bottomLeftToTopRight: continue

            masCount += 1

    print(f"part1: {total}")
    print(f"part2: {masCount}")


if __name__ == "__main__":
    main()
