from utils import readInput

def main():
    distance = 0
    lInput, rInput = readInput();
    lInput.sort()
    rInput.sort()

    for left, right in zip(lInput, rInput):
        distance += abs(left - right)

    print(distance)

if __name__ == "__main__":
    main()
