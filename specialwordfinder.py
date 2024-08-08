"""Special Word Finder: finds random words from a list excluding the lines that arent strings and start with '#' and ' ' """


from wordfinder import WordFinder
from random import randint

class SpecialWordFinder(WordFinder):
    
    def __init__(self,filename):
        """inherits attributes and methods from parent class WordFinder"""
        super().__init__(filename)

    def random(self):
        """defines and uses filter_non_word to check each string in self.word_list(defined in WordFinder class).
            If string is a word that does not start with either '#' or a space, add word to self.filtered list
            pick a number between 0 and last index of filtered_list and return string within that random index.

            Examples:
            >>> wf = WordFinder('fruits.txt')
                wf.random()
                'apple'
                wf.random()
                'parsnips'

        """
        def filter_non_word(word):
            if word and word[0] != '#' and word[0] != ' ':
                return word
            return None
            
        self.filtered_list = list(filter(filter_non_word, self.word_list))
        rand = randint(0,len(self.filtered_list) -1)
        return self.filtered_list[rand]




        

    