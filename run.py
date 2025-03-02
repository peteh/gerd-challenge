import math
import utils
class Combiner():
    
    def __init__(self):
        self._words = self._read_words('filtered_words.txt')

    def _read_words(self, file_path):
        with open(file_path, 'r') as file:
            words = file.read().splitlines()
        return words
    
    def bruteforce(self):
        num_words = len(self._words)
        r = 5  # Selecting and arranging 5 words
        num_combinations = math.factorial(num_words) // math.factorial(num_words - r)
        num_processed = 0
        results_file = open("results.txt", "w")

        for word1_index in range(0, num_words):
            word1 = self._words[word1_index]
            for word2_index in range(word1_index+1, num_words):
                word2 = self._words[word2_index]
                word2_str = word1 + word2
                
                if utils.count_used_alphabet_letters(word2_str) < 10:
                    # skip if bad
                    continue

                for word3_index in range(word2_index+1, num_words):
                    word3 = self._words[word3_index]
                    word3_str = word2_str + word3
                    if utils.count_used_alphabet_letters(word3_str) < 15:
                        # skip if bad
                        continue

                    for word4_index in range(word3_index+1, num_words):
                        word4 = self._words[word4_index]
                        word4_str = word3_str + word4
                        if utils.count_used_alphabet_letters(word4_str) < 20:
                            # skip if bad
                            continue

                        # last one we don't skip elements to allow come back for words we skipped due to high requirements
                        for word5_index in range(0, num_words):
                            word5 = self._words[word5_index]
                            word5_str = word4_str + word5

                            num_processed += 1
                            if num_processed % 1000000 == 0:
                                print(f"Processed: {num_processed}/{num_combinations}")

                            # Write words to file if we have enough alphabet letters
                            #alphabet_letters = utils.count_used_alphabet_letters(word5_str)
                            alphabet_letters = utils.count_used_alphabet_letters_without_qxy(word5_str)
                            if alphabet_letters >= 23:
                                line = f"{word1.upper()} {word2.upper()} {word3.upper()} {word4.upper()} {word5.upper()} ({alphabet_letters})\n" 
                                print(line)
                                results_file.write(line)
                                results_file.flush()
        results_file.close()

if __name__ == "__main__":
    
    combiner = Combiner()
    combiner.bruteforce()