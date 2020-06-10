'''
    Class responsible for reading in the file for
        word_count_gen.py.
'''

import re

class FileParser():

    ###############
    ## VARIABLES ##
    ###############

    newMin = 11
    newMax = 48
    words_dict = {}

    ##########
    ## INIT ##
    ##########

    '''
    @desc
        Initialization for FileParser.
    @param path
        String path to file to parse.
    @requires
        [path] is a valid path to readable file.
    '''
    def __init__(self, path):
        self.path = path

    ############
    ## STATIC ##
    ############

    '''
    @desc
        Util method for counting number of words in a list.
    @param words_list
        List of words.
    @return
        Dictionary of words.
    '''
    @staticmethod
    def get_words_from_list(words_list):
        words_dict = {}
        for w in words_list:
            if w in words_dict:
                words_dict[w] += 1
            else:
                words_dict[w] = 1
        return words_dict

    '''
    @desc
        Util method for counting number of words in a line (unaltered).
    @param line
        Line to parse.
    @return
        Dictionary of words.
    '''
    @staticmethod
    def get_words_from_line(line):
        words_dict = {}
        words_list = re.findall(r'\w+', line)
        words_list = [w.lower() for w in words_list]
        words_dict = FileParser.get_words_from_list(words_list)
        return words_dict

    ##############
    ## INSTANCE ##
    ##############

    '''
    @desc
        Util method for added values from one Dictionary to another.
    @param d_update
        Dictionary from which to add from.
    '''
    def update_words_dict(self, d_update):
        keys = d_update.keys()
        for k in keys:
            if k in self.words_dict:
                self.words_dict[k] += d_update[k]
            else:
                self.words_dict[k] = d_update[k]

    '''
    @desc
        Parses the current path of words and loads them into [self.words_dict]
    '''
    def parse_file(self):
        with open(self.path, 'r') as sample:
            for line in sample:
                temp_dict = FileParser.get_words_from_line(line)
                self.update_words_dict(temp_dict)
