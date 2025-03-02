import utils 

def read_word_list(file_path: str, word_length: int, encoding: str = "utf-8") -> list:
    # Open the file in read mode
    with open(file_path, "r", encoding=encoding) as file:
        # Read each line in the file one by one
        lines = file.readlines()

    filtered_words = []

    for line in lines:
        word = (
            line.strip()
            .lower()
            .replace("ä", "ae")
            .replace("ö", "oe")
            .replace("ü", "ue")
            .replace("ß", "ss")
        )
        min_alphabet_letters = 5
        if len(word) == word_length and utils.count_used_alphabet_letters(word) >= min_alphabet_letters:
            filtered_words.append(word)

    return filtered_words


filtered_words = []
word_list_files = ["words/winedit/de_neu_utf8.dic", "words/wortliste/wortliste.txt"]
#word_list_files = ["words/wortliste/wortliste.txt"]

for word_list_file in word_list_files:
    wordlist_words = read_word_list(word_list_file, 5)
    for wordlist_word in wordlist_words:
        if wordlist_word not in filtered_words:
            filtered_words.append(wordlist_word)

print(len(filtered_words))

output_file_path = "filtered_words.txt"

with open(output_file_path, "w", encoding="utf-8") as output_file:
    for word in filtered_words:
        output_file.write(word + "\n")

print(f"Filtered words saved to {output_file_path}")