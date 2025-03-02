import math
import utils
import multiprocessing
import os
from itertools import islice
import time

class Combiner():
    
    def __init__(self, num_workers=None):
        self._words = utils.read_file_lines('filtered_words.txt')
        self.num_workers = num_workers if num_workers else os.cpu_count()
    
    def _process_chunk(self, args):
        chunk_id, word1_index = args
        num_words = len(self._words)
        num_processed = 0
        local_results = []
    
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
                        #if num_processed % 1000000 == 0:
                        #    print(f"Process {chunk_id}: Processed {num_processed} combinations")

                        # Check if we have enough alphabet letters
                        alphabet_letters = utils.count_used_alphabet_letters_without_qxy(word5_str)
                        if alphabet_letters >= 23:
                            result = f"{word1.upper()} {word2.upper()} {word3.upper()} {word4.upper()} {word5.upper()} ({alphabet_letters})"
                            local_results.append(result)
                            print(result)
        
        return local_results
    
            
    def bruteforce_mp(self):
        num_words = len(self._words)
        start_time = time.time()
        
        # Create chunks of word1 indices to distribute among workers
        all_word1_indices = range(0, num_words)
        chunks = all_word1_indices
        
        print(f"Starting multiprocessing search with {self.num_workers} workers")
        print(f"Total words: {num_words}, distributing into {len(chunks)} chunks")
        
        # Create process pool and distribute work
        with multiprocessing.Pool(processes=self.num_workers) as pool:
            # Create tasks with chunk_id and chunk data
            tasks = [(i, chunk) for i, chunk in enumerate(chunks)]
            # Process all chunks and collect results
            all_results = pool.map(self._process_chunk, tasks)
        
        # Flatten results from all processes
        flattened_results = [result for sublist in all_results for result in sublist]
        
        # Write results to file
        with open("results.txt", "w") as results_file:
            for result in flattened_results:
                results_file.write(result + "\n")
        
        elapsed_time = time.time() - start_time
        print(f"Multiprocessing search completed in {elapsed_time:.2f} seconds")
        print(f"Found {len(flattened_results)} matches")

if __name__ == "__main__":
    # This is important for Windows compatibility
    multiprocessing.freeze_support()
    
    combiner = Combiner()
    combiner.bruteforce_mp()