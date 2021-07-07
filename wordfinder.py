from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path):
        
        file = open(file_path)
        self.words = self.read_file(file) # just words is good enough, can set to result of calling read_file
        
        print(f"{len(self.words)} words read")

    def __repr__(self):
        return f"""{self.__class__}
            words = {self.words}>"""

    def read_file(self, file):  
        """Parses the file that was passed in and appends it to 
           a new list called words
        """
        ## CHANGE to returns to words
         # copyy 
        return [line.strip() for line in file]    

    def random(self):
        """ Chooses a random line in the list of words
            Returns it without the new line character at the end
        """
        return choice(self.words)  # should only return the random line, not strip() --- COMPLETED
         # move strip() to read_file --- COMPLETED

class SpecialWordFinder(WordFinder):
    """Subclass of WordFinder 
        If the file contains symbols and empty lines, we will not return those lines"""
    
    # def __init__(self, file_path):
    #     super().__init__(file_path)
    #     self.read_file(file_path)
    #     self.words = super().words
        

    def read_file(self, file):
        """ Removes "#" and blank lines from the list"""
        remove_comment = [line for line in file if not line.startswith('#')]
        return [line.strip() for line in remove_comment if line.strip() != ""]
        # call it read_file: determines how to read the file and puts it into list
        # POLYMORPHISM!

