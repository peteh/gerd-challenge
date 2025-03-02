def count_used_alphabet_letters(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for letter in alphabet:
        if letter in word:
            count += 1
    return count