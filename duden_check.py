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
    
if __name__ == "__main__":
    duden_checker = DudenChecker()
    results_file = open("results_duden.txt", "w")
    with open("results.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(f"{line.strip()}: ")
            words = line.split(" ")
            in_duden = True
            for i in range(0, 5):
                word = words[i]
                if not duden_checker.check_word(word):
                    print(f" {word} not in duden")
                    in_duden = False
                    break
            if in_duden:
                results_file.write(line)
                results_file.flush()
    results_file.close()