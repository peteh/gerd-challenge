import utils 
import json

CHECK_WORD_DUDEN = False

def read_word_list(file_path: str, word_length: int, encoding: str = "utf-8") -> list:
    # Open the file in read mode
    with open(file_path, "r", encoding=encoding) as file:
        # Read each line in the file one by one
        lines = file.readlines()

    filtered_words = []

    for line in lines:
        word = (
            line.strip()
        )
        if len(word) == word_length:
            filtered_words.append(word)

    return filtered_words

def read_json_list(file_path: str, word_length: int) -> list:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    filtered_words = []

    for word in data:
        if len(word) == word_length:
            filtered_words.append(word)

    return filtered_words

filtered_words = []
word_lists = []
#word_lists.append(read_word_list("words/winedit/de_neu_utf8.dic", 5)) # this contains a lot of weird words but also stuff like xylem
word_lists.append(read_word_list("words/wortliste/wortliste.txt", 5))
word_lists.append(read_json_list("words/german-words-library/German-words-1600000-words-multilines.json", 5))

duden_checker = utils.DudenChecker()
for wordlist in word_lists:
    for wordlist_word in wordlist:
        # format the word to fit into the 5-letter wordlist
        wordlist_word_formatted = (wordlist_word.lower()
            .replace("ä", "ae")
            .replace("ö", "oe")
            .replace("ü", "ue")
            .replace("ß", "ss")
        )
        
        # Skip words that are not 5 letters long
        if len(wordlist_word_formatted) != 5:
            continue
        
        if utils.count_used_alphabet_letters(wordlist_word_formatted) < 5:
            continue
        
        # Skip words that are already in the filtered list
        if wordlist_word_formatted in filtered_words:
            continue

        if CHECK_WORD_DUDEN:
            # Check if the word is in the Duden
            if not duden_checker.check_word(wordlist_word):
                print(f"{wordlist_word} not in duden")
                continue
        
        filtered_words.append(wordlist_word_formatted)

print(len(filtered_words))

output_file_path = "filtered_words.txt"

with open(output_file_path, "w", encoding="utf-8") as output_file:
    for word in filtered_words:
        output_file.write(word + "\n")

print(f"Filtered words saved to {output_file_path}")