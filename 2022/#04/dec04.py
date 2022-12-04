def prepare_input():
    input_data = open("input", "r")

    lines = input_data.read().split("\n")
    pairs = []
    for line in lines:
        pairs.append(line.split(','))
    return pairs


def see_if_contains(pair):
    a = pair[0].split('-')
    b = pair[1].split('-')
    if int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1]):
        return True
    elif int(b[0]) >= int(a[0]) and int(b[1]) <= int(a[1]):
        return True
    else:
        return False


def see_if_overlaps(pair):
    a = pair[0].split('-')
    b = pair[1].split('-')
    if int(b[0]) <= int(a[0]) <= int(b[1]):
        return True
    if int(a[0]) <= int(b[0]) <= int(a[1]):
        return True
    else:
        return False


# --- Task 1 ---
result = 0
for elf_pair in prepare_input():
    if see_if_contains(elf_pair):
        result += 1
print(result)

# --- Task 2 ---
result = 0
for elf_pair in prepare_input():
    if see_if_overlaps(elf_pair):
        result += 1
print(result)

