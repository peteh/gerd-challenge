import duden
class DudenChecker():
    def __init__(self):
        self._words = []
    
    def check_word(self, word):
        if word in self._words:
            return True
        w = duden.search(word, exact = False)
        if len(w) > 0:
            self._words.append(word)
            return True
        return False

def count_used_alphabet_letters(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for letter in alphabet:
        if letter in word:
            count += 1
    return count

def count_used_alphabet_letters_without_qxy(word):
    alphabet = 'abcdefghijklmnoprstuvwz'
    count = 0
    for letter in alphabet:
        if letter in word:
            count += 1
    return count

def read_file_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def write_file_lines(file_path, lines):
    with open(file_path, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")