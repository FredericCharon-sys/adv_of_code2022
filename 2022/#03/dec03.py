def prepare_input():
    input_data = open("input", "r")

    lines = input_data.read().split("\n")
    rucksack = []
    for line in lines:
        rucksack.append((line[:int(len(line)/2)], line[int(len(line)/2):]))
    return rucksack

def prepare_input2():
    input_data = open("input", "r")

    lines = input_data.read().split("\n")
    return lines

def compare_compts(pair):
    for char in pair[0]:
        if char in pair[1]:
            return char


def find_badge(r1, r2, r3):
    for char in r1:
        if char in r2 and char in r3:
            return char


alph_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# --- Task 1 ---
result = 0
input = prepare_input()
for i in input:
    result += alph_list.index(compare_compts(i))+1
print(result)

# --- Task 2 ---
input = prepare_input2()
result = 0
for i in range(int(len(prepare_input()) / 3)):
    result += alph_list.index(find_badge(input[i*3], input[i*3+1], input[i*3+2]))+1
print(result)
