input_data = open("input", "r")

lines = input_data.read().split("\n\n")
elves = []
for line in lines:
    elves.append(line.split("\n"))


def _sum(arr):
    sum = 0
    try:
        for num in arr:
            sum += int(num)
    except:
        return arr
    return sum


def find_max(a_list):
    total_values = []
    for element in a_list:
        total_values.append(_sum(element))

    max_val = max(total_values)
    total_values.remove(max_val)
    return max_val, total_values


# --- task 1 ---
print(find_max(elves)[0])


# --- task 2 ---
top_three = []
for _ in range(3):
    _max_val, elves = find_max(elves)
    top_three.append(_max_val)
print(_sum(top_three))

