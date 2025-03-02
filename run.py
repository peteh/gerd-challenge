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
                if utils.count_used_alphabet_letters(word1+word2) < 10:
                    # skip if bad
                    continue
                
                for word3_index in range(word2_index+1, num_words):
                    word3 = self._words[word3_index]
                    if utils.count_used_alphabet_letters(word1+word2+word3) < 15:
                        # skip if bad
                        continue
                    
                    for word4_index in range(word3_index+1, num_words):
                        word4 = self._words[word4_index]
                        if utils.count_used_alphabet_letters(word1+word2+word3+word4) < 20:
                            # skip if bad
                            continue
                        for word5_index in range(word4_index+1, num_words):
                            word5 = self._words[word5_index]
                            eval_combined = word1 + word2 + word3 + word4 + word5
                            num_processed += 1
                            if num_processed % 1000000 == 0: 
                                print(f"Processed: {num_processed}/{num_combinations}")
                            alphabet_letters = utils.count_used_alphabet_letters(eval_combined)
                            if alphabet_letters >= 24:
                                line = f"{word1.upper()} {word2.upper()} {word3.upper()} {word4.upper()} {word5.upper()} ({alphabet_letters})\n" 
                                print(line)
                                results_file.write(line)
                                results_file.flush()
        results_file.close()

    def combine2(self, list_1, list_2, minimal_letters):
        num_combinations = len(list_1) * len(list_2)
        num_processed = 0
        new_list = []
        for word1_index in range(0, len(list_1)):
            for word2_index in range(0, len(list_2)):
                            word1 = self._words[word1_index]
                            word2 = self._words[word2_index]
                            eval_combined = word1 + word2
                            num_processed += 1
                            if num_processed % 1000000 == 0: 
                                print(f"Processed: {num_processed}/{num_combinations}")
                            alphabet_letters = utils.count_used_alphabet_letters(eval_combined)
                            if alphabet_letters >= minimal_letters:
                                new_list.append(word1 + word2)
                                #print(f"{word1.upper()} {word2.upper()}")
        return new_list

    def magic(self):
        list_2_words = self.combine2(self._words, self._words, 10)
        print(len(list_2_words))
        list_3_words = self.combine2(list_2_words, self._words, 15)
        print(len(list_2_words))
        print(len(list_3_words))
if __name__ == "__main__":
    
    combiner = Combiner()
    combiner.bruteforce()