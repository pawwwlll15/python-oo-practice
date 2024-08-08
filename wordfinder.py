"""Word Finder: finds random words from a list """
from random import randint

class WordFinder:
    
    def __init__(self,filename):
        """Creates a list of words from a file that has one word per line and prints the number of words read

            Parameters:
            filename(file) = the .txt file you would like to use to create the list

            Returns:
            String: "{number of words} words read"

           
            Example:
            >>> wf = WordFinder('fruits.txt')
                7 words read     
        """
        self.filename = filename
        self.word_list = []
        with open(self.filename,'r') as file:
            for line in file:
                self.word_list.append(line.rstrip('\n'))

        return f"{len(self.word_list)} words read"

    def random(self):
        """creates a random integer between 0 and length of self.word_list -1(-1 is to get last index)

            Returns:
            string with in random index of self.word_list

            Example:
            >>> wf = WordFinder('fruits.txt')
                wf.random()
                '# Fruits'
                wf.random()
                'grapes'
        
        """
        rand = randint(0,len(self.word_list) -1)
        return self.word_list[rand]
