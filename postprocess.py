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

def filter_blacklist(lines, blacklist):
    blacklist = [word.lower() for word in blacklist]
    filtered_list = []
    for line in lines:
        blacklisted = False
        for word in line.split(" ")[:5]:
            if word.lower() in blacklist:
                print(f"Skipping {word} because in blacklist")
                blacklisted = True
                continue
        if not blacklisted:
            filtered_list.append(line)

    return filtered_list

if __name__ == "__main__":
    results = utils.read_file_lines("results.txt")
    results_qxy_filtered = filter_qxy(results)
    results_blacklist_filtered = filter_blacklist(results, utils.read_file_lines("words/blacklist/blacklist.txt"))
    utils.write_file_lines("results_after_blacklist.txt", results_blacklist_filtered)
    utils.write_file_lines("results_qxy_filtered.txt", results_qxy_filtered)