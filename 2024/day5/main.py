def readInputs() -> tuple[dict[int, list[int]], list[list[int]]]:
    with open("./inputs.txt") as f:
        orders: dict[int, list[int]] = dict()
        sequences: list[list[int]] = []

        isSequence = False
        for line in f:
            if line == "\n":
                isSequence = True
                continue

            if isSequence:
                sequences.append([int(x) for x in line.split(',')])
            else:
                nums = [int(x) for x in line.split('|')]
                if not nums[0] in orders.keys():
                    orders[nums[0]] = list()
                if not nums[1] in orders.keys():
                    orders[nums[1]] = list()
                orders[nums[0]].append(nums[1])

        return orders, sequences


def isValid(orders: dict[int, list[int]], update: list[int]):
    for num in update:
        for greater in orders[num]:
            if not greater in update: continue
            if update.index(num) > update.index(greater): return False

    return True


def sort(orders: dict[int, list[int]], update: list[int]):
    for i in range(len(update)):
        for j in range(len(update)):
            if not update[j] in orders[update[i]]: continue
            if i < j: continue

            update[i], update[j] = update[j], update[i]


def main():
    orders, updates = readInputs()
    sumMiddle = 0
    sumCorrected = 0

    for update in updates:
        if isValid(orders, update):
            sumMiddle += update[len(update) // 2]
        else:
            sort(orders, update)
            sumCorrected += update[len(update) // 2]

    print(f"part1: {sumMiddle}")
    print(f"part2: {sumCorrected}")


if __name__ == "__main__":
    main()
