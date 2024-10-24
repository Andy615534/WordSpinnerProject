# HeeSeo Lee(1527190), Andy Jeon (u1528909)

import random

class Spinner:
    def __init__(self, synonym_file):
        self.synonym_dict = self.load_synonyms(synonym_file)

    def load_synonyms(self, file_path):
        synonym_dict = {}
        with open(file_path, 'r') as file:
            for line in file:
                word, synonyms = line.strip().split(':')
                synonym_dict[word] = synonyms.split(',')
        return synonym_dict

    def spin_text(self, text, probability=50):
        words = text.split()
        spun_words = []
        for word in words:
            if word in self.synonym_dict and random.randint(1, 100) <= probability:
                synonyms = self.synonym_dict[word]
                spun_words.append(random.choice(synonyms))
            else:
                spun_words.append(word)
        return ' '.join(spun_words)
