game_dict = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}


def prepare_input():
    input_data = open("input", "r")

    lines = input_data.read().split("\n")
    tactics = []
    for line in lines:
        tactics.append(line.split(' '))
    return tactics


def get_score(game):
    score = game_dict.get(game[1])
    opponent = game_dict.get(game[0])

    if (score - opponent) % 3 == 1:
        return score + 6
    elif (score - opponent) % 3 == 0:
        return score + 3
    else:
        return score


def get_score_task2(game):
    opponent = game_dict.get(game[0])
    if game[1] == 'X':
        result = opponent + 2
        if result > 3:
            return result % 3
        return result
    elif game[1] == 'Y':
        return opponent + 3
    else:
        result = opponent + 1
        if result > 3:
            return result % 3 + 6
        return result + 6

# --- Task 1 ---
final_score = 0
input_values = prepare_input()
for i in input_values:
    final_score += get_score(i)
print(final_score)

# --- Task 2 ---
final_score = 0
input_values = prepare_input()
for i in input_values:
    final_score += get_score_task2(i)
print(final_score)

