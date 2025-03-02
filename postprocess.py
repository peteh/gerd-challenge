import utils

def filter_qxy(lines : list) -> list:
    filtered_list = []
    for line in lines:
        words = line.split(" ")
        words5 = "".join(words[:5]).lower()
        letter_limit = 23
        used_letters = utils.count_used_alphabet_letters_without_qxy(words5)
        if used_letters < letter_limit:
            print(f"Skipping {words5} because less than {letter_limit} (used: {used_letters})")
            continue
        filtered_list.append(f"{line} (qxy: {used_letters})")

    return filtered_list


if __name__ == "__main__":
    results = utils.read_file_lines("results.txt")
    results_qxy_filtered = filter_qxy(results)
    utils.write_file_lines("results_qxy_filtered.txt", results_qxy_filtered)