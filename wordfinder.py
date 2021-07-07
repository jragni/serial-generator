from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file):
        self.file = open(file, "r") # never accessed again after opening, can just be a local variable
        self.list_of_words = [] # just words is good enough, can set to result of calling read_file
        self.read_file()
        print(f"{len(self.list_of_words)} words read")

    def __repr__(self):
        return f"""WordFinder<file = {self.file} 
            list_of_words = {self.list_of_words}>"""

    def read_file(self):  # if we make opening file a variable, need to pass file in here
        """Parses the file that was passed in and appends it to 
           a new list called list_of_words
        """
        for line in self.file:                      # list comprehension
            self.list_of_words.append(line)         # just return list here

    def random(self):
        """ Chooses a random line in the list of words
            Returns it without the new line character at the end
        """
        line = choice(self.list_of_words)  # should only return the random line, not strip()
        return (line.strip())              # move strip() to read_file

class SpecialWordFinder(WordFinder):
    """Subclass of WordFinder 
        If the file contains symbols and empty lines, we will not return those lines"""
    
    def __init__(self, file):
        super().__init__(file)
        self.remove_special_chars()

    def __repr__(self):
        return f"""SpecialWordFinder<file = {self.file} 
            list_of_words = {self.list_of_words}>""" 

    def remove_special_chars(self):
        """ Removes "#" and blank lines from the list"""
        
        remove_comment = [line for line in self.list_of_words if "#" not in line]
        
        self.list_of_words = [line.strip() for line in remove_comment if line.strip() != ""]
        # call it read_file: determines how to read the file and puts it into list
        # POLYMORPHISM!

