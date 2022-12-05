def prepare_input():
    input_data = open("input", "r")

    input = input_data.read().split("\n\n")
    crates = input[0].split('\n')
    stacks = [[]for _ in range(9)]
    for i in crates[:-1]:
        for j in range(int((len(i)+1)/4)):
            if i[j*4+1] != " ":
                stacks[j].insert(0, i[j*4+1])
    lines = input[1].split("\n")
    moves = []
    for i in lines:
        moves.append(i.replace("move ", "").replace(" from ", ",").replace(" to ", ",").split(","))
    return(stacks, moves)


def move_crate(stacks, _amount, _from, _to):
    for i in range(_amount):
        crate = stacks[_from].pop()
        stacks[_to].append(crate)
    return stacks


def move_multiple_crates(stacks, _amount, _from, _to):
    crates = []
    for i in range(_amount):
        crates.insert(0, stacks[_from].pop())
    for crate in crates:
        stacks[_to].append(crate)
    return stacks


# --- Task 1 ---
stack_list, all_moves = prepare_input()
for move in all_moves:
    (move_crate(stack_list, int(move[0]), int(move[1])-1, int(move[2])-1))

result = ""
for i in stack_list:
    result = result + str(i[-1])
print(result)


# --- Task 2 ---
stack_list, all_moves = prepare_input()
for move in all_moves:
    (move_multiple_crates(stack_list, int(move[0]), int(move[1])-1, int(move[2])-1))

result = ""
for i in stack_list:
    result = result + str(i[-1])
print(result)
