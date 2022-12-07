input_data = open("input", "r")

signal = input_data.read()


def find_start_marker(_string):
    for i in range(len(_string) - 3):
        start_found = True
        for j in range(3):
            if compare_next_pos(_string, i+j, 3-j) is False:
                start_found = False
        if start_found is True:
            return i + 4


def compare_next_pos(_string, _pos, n):
    for i in range(n):
        if _string[_pos] == _string[_pos + 1 + i]:
            return False
    return True


def find_start_message(_string):
    for i in range(len(_string) - 3):
        start_found = True
        for j in range(13):
            if compare_next_pos(_string, i+j, 13-j) is False:
                start_found = False
                break
        if start_found is True:
            return i + 14


# --- Task 1 ---
print(find_start_marker(signal))

# --- Task 2 ---
print(find_start_message(signal))
